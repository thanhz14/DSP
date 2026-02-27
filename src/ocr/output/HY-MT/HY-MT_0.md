# HY-MT1.5 Technical Report

Tencent Hunyuan Team

## Abstract

In this report, we introduce our latest translation models, HY-MT1.5-1.8B and HY-MT1.5-7B, a new family of machine translation models developed through a holistic training framework tailored for high-performance translation. Our methodology orchestrates a multi-stage pipeline that integrates general and MT-oriented pre-training, supervised fine-tuning, on-policy distillation, and reinforcement learning. HY-MT1.5-1.8B, the 1.8B-parameter model demonstrates remarkable parameter efficiency, comprehensively outperforming significantly larger open-source baselines (e.g., Tower-Plus-72B, Qwen3-32B) and mainstream commercial APIs (e.g., Microsoft Translator, Doubao Translator) in standard Chinese-foreign and English-foreign tasks. It achieves approximately 90% of the performance of ultra-large proprietary models such as Gemini-3.0-Pro, while marginally trailing Gemini-3.0-Pro on WMT25 and Mandarin-minority language benchmarks, it maintains a substantial lead over other competing models. Furthermore, HY-MT1.5-7B establishes a new state-of-the-art for its size class, achieving 95% of Gemini-3.0-Pro's performance on Flores-200 and surpassing it on the challenging WMT25 and Mandarin-minority language test sets. Beyond standard translation, the HY-MT1.5 series supports advanced constraints, including terminology intervention, context-aware translation, and format preservation. Extensive empirical evaluations confirm that both models offer highly competitive, robust solutions for general and specialized translation tasks within their respective parameter scales.

HY-MT1.5-1.8B: https://huggingface.co/tencent/HY-MT1.5-1.8B

HY-MT1.5-7B: https://huggingface.co/tencent/HY-MT1.5-7B

Code Repository: https://github.com/Tencent-Hunyuan/HY-MT

<div style="text-align: center;"><img src="imgs/img_in_chart_box_144_931_1038_1482.jpg" alt="Image" width="75%" /></div>


<div style="text-align: center;">Figure 1: Benchmark performance of HY-MT1.5 models and state-of-the-art baselines.</div>
