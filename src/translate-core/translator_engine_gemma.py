# from openai import OpenAI


# class TranslationEngineGemma:
#     def __init__(
#         self,
#         base_url="http://127.0.0.1:8001/v1",
#         model_name="Infomaniak-AI/vllm-translategemma-4b-it",
#     ):
#         self.client = OpenAI(base_url=base_url, api_key="unused")
#         self.model_name = model_name
#         print(f"TranslateGemma client ready -> {base_url} (model: {model_name})")

#     def translate(self, text, source_lang="en", target_lang="vi"):
#         if not text or not text.strip():
#             return ""

#         # Infomaniak delimiter format
#         messages = [
#             {
#                 "role": "user",
#                 "content": f"<<<source>>>{source_lang}<<<target>>>{target_lang}<<<text>>>{text}",
#             }
#         ]

#         try:
#             response = self.client.chat.completions.create(
#                 model=self.model_name,
#                 messages=messages,
#                 max_tokens=2048,
#                 temperature=0,
#             )
#             return response.choices[0].message.content.strip()
#         except Exception as e:
#             print(f"Gemma Translation error: {str(e)}")
#             return text

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


class TranslationEngineGemma:
    def __init__(
        self,
        model_path=r"D:\Acer\Code\DSP\DSP\models\translategemma-4b-it",
        device="cuda",  # "cuda" | "cpu" | "auto"
    ):
        print("Loading Gemma model from local...")

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map=device,
            torch_dtype="auto",
        )

        self.model.eval()

        print("Gemma local model ready!")

    def translate(self, text, source_lang="en", target_lang="vi"):
        if not text or not text.strip():
            return ""

        # Prompt theo format Gemma / Instruct
        prompt = f"""
You are a professional translator.

Translate the following text from {source_lang} to {target_lang}.

Text:
{text}

Translation:
"""

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=4096,
        )

        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=512,
                temperature=0,
                do_sample=False,
            )

        result = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True,
        )

        # Lấy phần sau "Translation:"
        if "Translation:" in result:
            result = result.split("Translation:")[-1]

        return result.strip()
# Singleton instance
_engine = None


def get_translator():
    global _engine
    if _engine is None:
        _engine = TranslationEngineGemma()
    return _engine
