# TranslateGemma Technical Report

Google Translate Research Team

We present TranslateGemma, a suite of open machine translation models based on the Gemma 3 foundation models. To enhance the inherent multilingual capabilities of Gemma 3 for the translation task, we employ a two-stage fine-tuning process. First, supervised fine-tuning is performed using a rich mixture of high-quality large-scale synthetic parallel data generated via state-of-the-art models and human-translated parallel data. This is followed by a reinforcement learning phase, where we optimize translation quality using an ensemble of reward models, including MetricX-QE and AutoMQM, targeting translation quality. We demonstrate the effectiveness of TranslateGemma with human evaluation on the WMT25 test set across 10 language pairs and with automatic evaluation on the WMT24++ benchmark across 55 language pairs. Automatic metrics show consistent and substantial gains over the baseline Gemma 3 models across all sizes. Notably, smaller TranslateGemma models often achieve performance comparable to larger baseline models, offering improved efficiency. We also show that TranslateGemma models retain strong multimodal capabilities, with enhanced performance on the Vistra image translation benchmark. The release of the open TranslateGemma models aims to provide the research community with powerful and adaptable tools for machine translation.

### 1. Introduction

In an increasingly interconnected world, machine translation (MT) plays a pivotal role in bridging language barriers, facilitating global communication, and democratizing access to information. The development of large language models (LLMs) has significantly advanced the state-of-the-art in MT. However, progress is greatly benefitted by the availability of strong, open models that allow for transparency, reproducibility, and community-driven innovation.

To this end, we present TranslateGemma, an open variant of the Gemma 3 foundation model (Gemma Team, 2025), specifically enhanced for machine translation. While Gemma 3 is already a potent multilingual LLM, TranslateGemma has been further refined to deliver superior translation quality. This improvement is achieved through a two-stage process: Supervised Fine-tuning (SFT) on a diverse corpus of parallel data (Section 3) and Reinforcement Learning (RL) from human and model-based feedback (Section 4).

Our SFT approach leverages a blend of human-translated and synthetically-generated parallel texts, carefully curated to improve translation quality without compromising the model's general capabilities. The RL phase employs a combination of reward models designed to optimize translation quality. We demonstrate the efficacy of TranslateGemma on the WMT25 and WMT24++ datasets, showing substantial gains across 55 language pairs.



Furthermore, TranslateGemma retains the inherent multimodal capabilities of the original Gemma 3 model. Our experiments on the Vistra corpus (Salesky et al., 2024) indicate that the enhancements in text translation also positively impact image translation performance, showcasing the model's versatility. We believe the release of TranslateGemma will provide a valuable resource for researchers and practitioners in the field of machine translation.

### 2. Training data

We use two types of data for the training of the models, most of it shared between the SFT and RL phases.

#### 2.1. Synthetic Gemini-Generated Translation Data

Our goal is to generate high-quality synthetic data for each language, as this has been shown