fully meeting real-time interaction requirements. Overall, HY-MT1.5-1.8B's high efficiency, supported by optimized model design and inference logic, makes it well-suited for high-throughput, real-time translation scenarios such as instant messaging, intelligent customer service, and mobile translation applications.

For HY-MT1.5-7B, its quality score exceeds 80% (exceeding that of most models in the figure), and its average response time is 0.45 seconds. This response time is comparable to that of Microsoft-Translator, whereas its translation quality is distinctly higher than that of Microsoft-Translator. This result confirms that the HY-MT1.5 models combine high translation accuracy with fast inference speed, making them suitable for scenarios requiring both high-quality translation and real-time responsiveness.

### 3.4 Practical Distinctive Features

To address the core limitations of existing translation systems—overreliance on basic text translation and inadequate support for customized requirements via flexible prompts—we propose three distinctive features, validated through scenario-based case studies in Table 3. These features target terminology accuracy, context-aware disambiguation, and format preservation, which are critical for real-world scenario adaptation but underexplored in current frameworks.

First, terminology-guided translation resolves inaccurate rendering of cultural or domain-specific terms via a term-anchored prompt template. As shown in Scenario 1, the term “混元珠” is transliterated as the semantically ambiguous “Hunyuan” without terminology prompts; with the authorized mapping “Chaos Pearl” injected into the prompt, the model generates a precise, consistent translation.

Second, context-aware translation mitigates lexical ambiguity in contextualized tasks using a context-integrated prompt template. For the phrase "The Educational and Inspirational Poetics of Pilots" in Scenario 2, the model misinterprets "pilot" as "飞行员" in the absence of contextual cues; when TV series context is provided, it correctly identifies "pilot" as "试播集" and produces a contextually coherent result.

Third, format-preserving translation preserves the structural integrity of tagged text by using a format-constrained prompt template. In Scenario 3, the model outputs disorganized tags (e.g., <1>instead of <s1>) without format prompts. With explicit rules to preserve <sn>tags and to wrap outputs in <target>tags, it generates translations that maintain both semantic fidelity and structural consistency.

Collectively, these prompt-driven features enable the model to transcend basic translation tasks, delivering customized solutions for terminology-sensitive, context-dependent, and format-constrained scenarios.

### 3.5 Quantization Experiment

Large Language Models (LLMs) have achieved significant success across a range of applications, but high resource demands hinder their deployment on resource-constrained edge devices. Quantization, which reduces model size and computational cost by using low-precision weight representations, is a key solution (Kulkarni et al., 2022). For the HY-MT1.5-1.8B model, we tested two quantization strategies (Int4 and FP8) and adopted the GPTQ algorithm (Frantar et al., 2023a) for Post-Training Quantization (PTQ) to minimize errors. GPTQ processes weights layer-wise with small calibration data, avoiding retraining and improving deployment efficiency.

Table 4 presents the performance of different quantization schemes (original, Int4, FP8) on multiple translation tasks, evaluated by XCOMET-XXL and CometKiwi metrics. It shows that FP8 quantization preserves accuracy close to the original model (e.g., ZH ⇔ XX XCOMET-XXL score: 0.8379 for FP8 vs. 0.8361 for the original), whereas Int4 quantization reduces model size but causes noticeable accuracy degradation.

## 4 Conclusion

This report introduces the HY-MT1.5 models (1.8B and 7B) and a dedicated machine translation training framework that effectively addresses two core challenges: the quality-efficiency trade-off and inadequate support for customized translation needs. By integrating general pre-training, MT-oriented pre-training, supervised fine-tuning, on-policy distillation, and reinforcement learning with a rubrics-based evaluation system, the models achieve a superior balance of performance and efficiency, as well as strong adaptability to practical scenarios.

Experimental results on key benchmarks (Flores-200, WMT25, Mandarin-minority languages) confirm the competitiveness of HY-MT1.5 models. The 1.8B model outperforms mainstream medium-sized open-source models and commercial APIs, achieving performance comparable to that of ultra-large