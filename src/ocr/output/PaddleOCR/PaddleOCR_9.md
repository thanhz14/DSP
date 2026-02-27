extract high-dimensional semantic embeddings for all candidate images. For each task, we apply K-Means clustering to partition the dataset D into K distinct visual clusters  $ \{C_1, C_2, \ldots, C_K\} $. This step groups samples with similar visual structures (e.g., solid line tables vs. wireless tables) together.

2. Uncertainty Estimation. For each cluster  $ C_i $, we estimate its difficulty by measuring the model's prediction uncertainty. Specifically, we randomly sample a subset of images from  $ C_i $ and perform multiple inference passes with stochastic decoding using the pre-trained model from Stage 1. We calculate an uncertainty score  $ S_i $ based on the divergence of the generated outputs. A higher  $ S_i $ indicates that the model is inconsistent or unconfident regarding the samples in this cluster.

3. Weighted Sampling Plan. Based on the uncertainty score, we formulate a sampling plan to determine the number of samples  $ N_i $ to draw from each cluster  $ C_i $. Inspired by the principle of hard example mining, we adopt a polynomial weighting scheme to amplify the focus on harder clusters. Specifically, the allocated sample count  $ N_i $ for cluster  $ C_i $ is determined by:

 $$ N_{i}=\min\left(\left\lfloor\frac{(S_{i}+\alpha)^{\beta}}{\sum_{j=1}^{K}(S_{j}+\alpha)^{\beta}}\times N_{total}\right\rfloor,\left|C_{i}\right|\right) $$ 

where $S_i$ is the average uncertainty score of cluster $C_i$, and $|C_i|$ denotes the total number of available samples in that cluster. The parameters $\alpha$ and $\beta$ are the smoothing and power factors, respectively (set to $\alpha = 1.0$, $\beta = 2.0$ based on empirical observations). $N_{\text{total}}$ represents the total sampling budget. This strategy allows us to dynamically up-sample complex scenarios (e.g., distorted seals, dense tables) while maintaining a representative baseline for simpler cases.

As detailed in the previous section, we employ the Uncertainty-Aware Cluster Sampling (UACS) strategy to select the most effective training samples based on visual clustering and inference variance.

##### 3.2.2. Data Construction for New Capabilities

In addition to data quality control, we expanded the VLM's capabilities by integrating data spanning a wider array of tasks, languages, and document types. This expansion focuses on these key dimensions: Spotting, Specialized Text (Seals), OCR Enhancement, and Complex Tables, Formulas, and Chart.

Spotting: We collected a large-scale and diverse set of images covering a wide range of real-world scenarios, such as financial research reports, tabular documents, handwritten materials, classical texts, and other complex document and natural scene images. During the annotation process, we jointly employed PP-OCRv5 [22] to generate initial recognition results, followed by an IoU-based cross-filtering strategy to eliminate low-quality and inconsistent samples, while for a subset of samples with ambiguous or inaccurate labels, multimodal models including PaddleOCR-VL [9] and Qwen3-VL [6] were further leveraged for label refinement, thereby substantially improving the overall annotation quality and robustness of the dataset.

Seal: We combined synthetic and real-world images of contracts, invoices, and commemorative seals to build a high-quality dataset. Labels were generated using Qwen3-VL [6] and refined through a fine-tuning-based re-labeling process. Challenging cases were manually corrected to ensure final annotation accuracy and robustness.

OCR: We have significantly enhanced the model’s capabilities by refining the dataset’s