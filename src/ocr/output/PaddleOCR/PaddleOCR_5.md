We project the refined queries into a shared relational space to compute the pairwise precedence score  $ S_{i,j} $:

 $$ S_{i,j}=\frac{f(q_{i},q_{j})-f(q_{j},q_{i})}{\sqrt{d_{h}}},\quad\mathrm{w h e r e}f(q_{i},q_{j})=(W_{q}q_{i})^{\top}(W_{k}q_{j}) $$ 

where  $ W_q, W_k \in \mathbb{R}^{d \times d_h} $ are learnable projection matrices and  $ d_h $ denotes the hidden dimension. The resulting relation matrix  $ S \in \mathbb{R}^{N \times N} $ is constrained to be anti-symmetric such that  $ S_{i,j} = -S_{j,i} $, where  $ S_{i,j} > 0 $ implies element  $ i $ precedes element  $ j $.

During inference, to derive a globally consistent sequence from these pairwise relations, we implement a Voting-based Ranking strategy. We first apply the sigmoid function  $ \sigma(\cdot) $ to the relation matrix S and mask the diagonal elements. The absolute precedence votes  $ V_j $ for each element j is computed by aggregating the probabilities of other elements preceding it:

 $$ V_{j}=\sum_{i=1,i\neq j}^{N}\sigma(S_{i,j}). $$ 

The final reading order is determined by sorting the elements in ascending order of their total votes  $ V_{j} $. This joint optimization ensures that the logical sequence is highly sensitive to the refined object features, leading to superior performance on complex, multi-column, and non-standard document layouts.

By merging detection, segmentation, and ordering into a single vision-centric model, PP-DocLayoutV3 eliminates the need for redundant post-processing and separates feature extraction. The model produces the complete document structure in a single forward pass, where the multi-head system concurrently outputs classification labels, bounding box coordinates, pixel-accurate segments, and the logical reading sequence.

####### 2.1.2. PaddleOCR-VL-1.5-0.9B: Element-level Recognition and Text Spotting

The PaddleOCR-VL-1.5-0.9B inherits the lightweight architecture of PaddleOCR-VL-0.9B [9], integrating a Native Resolution Visual Encoder [17], an Adaptive MLP Connector, and the Lightweight ERNIE-4.5-0.3B Language Model [5]. In this update, the model's capabilities have been expanded to include Seal Recognition and Text Spotting. Consequently, the model now supports a comprehensive set of six core tasks: OCR, Formula Recognition, Table Recognition, Chart Recognition, Seal Recognition, and Text Spotting.

Compared to its predecessor, PaddleOCR-VL-1.5-0.9B demonstrates significant enhancements in recognition accuracy for complex tables and mathematical formulas. Furthermore, the model incorporates finer-grained optimizations for rare characters, ancient Chinese texts, multilingual tables, and text decorations such as underlines and emphasis marks.

#### 2.2. Training Recipe

The following sections introduce the training details of these two modules: PP-DocLayoutV3 for layout analysis and PaddleOCR-VL-1.5-0.9B for element recognition and text spotting.