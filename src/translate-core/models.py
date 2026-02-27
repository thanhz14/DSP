from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from transformers import AutoTokenizer, AutoModel
class ModelLoader:

    def __init__(self, model_name, load_4bit=True):
        self.model_name = model_name
        self.load_4bit = load_4bit

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            trust_remote_code=True
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map="auto",
            torch_dtype=torch.float16,
            load_in_4bit=self.load_4bit,
            trust_remote_code=True
        )

        return self.model, self.tokenizer
def dowload_model(model_name):


    model_name = "google/translategemma-4b-it"

    save_dir = "./models/translategemma-4b-it"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    tokenizer.save_pretrained(save_dir)
    model.save_pretrained(save_dir)

    print("Đã lưu về local:", save_dir)
if __name__ == "__main__":
    # Ví dụ: tải model về local
    model_name = "google/translategemma-4b-it"      
    dowload_model(model_name)