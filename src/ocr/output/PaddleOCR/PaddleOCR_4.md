high-fidelity recognition across diverse modalities, including text, complex tables, mathematical formulas, charts and seals. To conclude the pipeline, a lightweight post-processing engine orchestrates these outputs into structured formats such as Markdown and JSON, while providing advanced capabilities such as cross-page table merging and heading hierarchy refinement.

For the Spotting task, the framework simplifies its workflow by directly utilizing the PaddleOCR-VL-1.5-0.9B model for end-to-end text detection and recognition. This approach enables end-to-end text detection and recognition across a wide spectrum of domains—ranging from standard documents, identification cards, and ancient manuscripts to unconstrained scenarios like advertising posters, dialogue screenshots, signboards, and multilingual texts.

##### 2.1.1. PP-DocLayoutV3: Unified Layout Analysis

To address the challenges of complex physical distortions—including skew, warping, and illumination—and to overcome the high latency inherent in autoregressive Vision-Language Models (VLMs), we introduce PP-DocLayoutV3. This version represents a significant architectural evolution from its predecessor by transitioning from standard rectangular detection to a robust instance segmentation framework, while simultaneously integrating reading order prediction into a unified, end-to-end Transformer architecture.

Building upon the high-efficiency RT-DETR object detector [16], PP-DocLayoutV3 adopts a mask-based detection head. This allows the model to predict precise, pixel-accurate masks for layout elements rather than simple bounding boxes. Such a capability is critical for isolating document components in non-ideal scenarios, such as skewed or warped pages, where traditional axis-aligned boxes frequently overlap or capture excessive background noise.

Unlike the decoupled pointer network employed in PP-DocLayoutV2 [9], PP-DocLayoutV3 integrates Reading Order Prediction directly into the Transformer decoder layers. By merging detection, segmentation, and ordering into a single vision-centric model, PP-DocLayoutV3 eliminates the need for redundant post-processing and separates feature extraction steps.

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_974_1038_1225.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">Figure 3 | The unified architecture of PP-DocLayoutV3, featuring parallel heads for instance segmentation and relational reading order prediction.</div>


The core architectural innovation of PP-DocLayoutV3 is the integration of Reading Order Prediction directly into the Transformer decoder. Specifically, our model extends the RT-DETR framework to simultaneously optimize geometric localization and logical sequencing. Following the query-based paradigm, the decoder iteratively refines N object queries  $ Q = \{q_i\}_{i=1}^N \in \mathbb{R}^{N \times d} $. The reading order is then derived from the refined query embeddings of the final decoder layer through a Global Pointer Mechanism.