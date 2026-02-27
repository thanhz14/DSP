language test sets, while maintaining efficient deployment capabilities that facilitate widespread practical application.

2. Holistic and effective training scheme: We develop a tailored training framework for machine translation, integrating general pre-training, MT-oriented pre-training, supervised finetuning, on-policy distillation, and reinforcement learning. This framework enables the models to excel in both general and low-resource translation scenarios, laying a solid foundation for the superior performance of the HY-MT1.5 models.

3. Practical distinctive features: Addressing the limitation of insufficient customized translation support in existing systems, the HY-MT1.5 models are equipped with practical features including terminology intervention, contextual translation, and formatted translation. These capabilities enable flexible response to customized translation demands through prompt interactions, significantly enhancing adaptability to diverse real-world application scenarios and bridging the gap between academic performance and industrial needs.

The remainder of this report is organized as follows: we first elaborate on the holistic training framework and development details of the HY-MT1.5 models. Subsequently, we present extensive experimental evaluations to validate the models' performance across various representative translation benchmarks, focusing on their performance-efficiency balance and customized translation capabilities. Finally, we discuss key findings and outline future research directions.

## 2 Methodology

<div style="text-align: center;"><img src="imgs/img_in_image_box_158_690_1029_1059.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">Figure 3: Training pipeline of HY-MT1.5-1.8B and HY-MT1.5-7B.</div>


Our training framework for HY-MT1.5-1.8B follows a multi-stage pipeline designed to maximize the performance of smaller-parameter models through knowledge transfer and rigorous alignment. The overall pipeline consists of four main stages: MT-oriented Pre-training, Supervised Fine-Tuning (SFT), On-Policy Distillation, and Reinforcement Learning (RL).

### 2.1 MT-oriented Pretraining and Supervised Fine-Tuning

The initial phases of our training strategy align with the methodology described in our previous Hunyuan-MT Technical Report (Zheng et al., 2025). We use the HY-1.8B-Base $ ^{1} $ and HY-7B-Base $ ^{2} $ models as our base model to obtain HY-MT1.5-1.8B-preview and HY-MT1.5-7B.

• Data Strategy. We curate a massive dataset comprising high-quality multilingual monolingual corpora and parallel texts.

• Process. The base model undergoes Continuous Pretraining (CPT) followed by Supervised Fine-Tuning (SFT).