• Objectives. These stages are designed to enhance the model’s multilingual domain knowledge, translation capabilities, and adherence to translation instructions. For further details on the data curation and base training protocols, please refer to our previous work (Zheng et al., 2025).

### 2.2 Reinforcement Learning

To further align the model with human preferences and refine translation quality, we employ Reinforcement Learning. We adopt the GRPO (Group Relative Policy Optimization) (Shao et al., 2024) algorithm, which is also used in Hunyuan-MT-7B. GRPO updates the policy based on relative comparisons within groups of outputs, reducing training complexity while maintaining optimization stability.

We improve the reward modeling in the RL training of HY-MT1.5. Instead of relying on a single holistic score, we introduce a Rubrics-based Evaluation System. This multi-dimensional evaluation guides the LLM to evaluate translations with greater granularity.

We construct a structured scoring criterion set where an LLM-based evaluator scores translations across the following key dimensions:

• Accuracy: Evaluates whether the translation remains faithful to the original semantics, ensuring there are no omissions, mistranslations, or hallucinations.

- Fluency: Assesses whether the linguistic expression is natural and conforms to the grammar and idiomatic usage of the target language.

• Consistency: Checks for the consistent use of terminology, style, and context throughout the text.

• Cultural Appropriateness: Examines whether the translation adapts appropriately to the cultural background and expression habits of the target language.

- Readability: Evaluates how easy the text is to understand, ensuring clear sentence structures and distinct hierarchy.

Each dimension is assigned specific scoring standards and weights. The scores from these dimensions are aggregated to form the final reward signal. This fine-grained feedback mechanism provides the RL process with richer, more precise signals, enabling the model to improve simultaneously across multiple facets—resulting in translations that are not only correct but also natural, coherent, and culturally context-aware.

### 2.3 Strong-to-Weak On-Policy Distillation

While CPT and SFT significantly improve the 1.8B model’s performance, a performance gap relative to our larger HY-MT-7B model remains due to the inherent limitations imposed by its parameter size. To bridge this gap, we employ on-policy distillation.

Recent research (Agarwal et al., 2024; Gu et al., 2025; Lu & Lab, 2025) suggests that on-policy distillation is more effective than off-policy methods for improving student models. Consequently, we adopt this approach after SFT.

• Teacher Model. We utilize the fully trained HY-MT1.5-7B as the teacher model.

• Data. We collect approximately 1 million monolingual samples, covering all 33 supported languages, including specific ethnic minority languages and dialects.

• Loss Function. We employ per-token reverse KL divergence to align the student’s output distribution with the teacher’s. The loss function is defined as:

 $$ KL(\pi_{\theta}\parallel\pi_{teacher})=\mathbb{E}_{x\sim\pi_{\theta}}\left[\log\pi_{\theta}(x_{t+1}\mid x_{1..t})-\log\pi_{teacher}(x_{t+1}\mid x_{1..t})\right] $$ 

This process enables the 1.8B model to inherit the 7B model’s superior translation performance. Upon completion of this phase, we employ the same reinforcement learning approach utilized in the third stage to optimize the model, yielding the final model.

### 2.4 Quantization

Recent advancements in large language models (LLMs) have demonstrated remarkable success across a wide range of applications, from conversational chatbots to creative writing. However, growing concerns over data privacy, the need for offline functionality, and the high costs of large-scale cloud deployment necessitate the direct deployment of these models on edge devices, which are typically resource-constrained. Quantization has emerged as a promising technique to achieve this goal by