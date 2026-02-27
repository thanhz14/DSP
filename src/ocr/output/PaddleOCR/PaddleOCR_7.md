large-scale pre-training data related to seal recognition and text spotting during this alignment phase. Specifically, the maximum resolution for the spotting task is increased to  $ 2048 \times 28 \times 28 $ pixels, enabling the model to achieve more precise localization and recognition of text. By introducing these task-specific priors early in the training pipeline, the model establishes a robust foundation capable of capturing intricate visual patterns and effectively supporting the fine-grained localization and recognition tasks required in subsequent stages.

Post-training: Instruction Fine-tuning with New Capabilities. In this stage, we inherit the four fundamental instruction tasks from PaddleOCR-VL-0.9B—OCR, Table, Formula, and Chart Recognition—ensuring backward compatibility and high performance on standard document elements. The key innovation in PaddleOCR-VL-1.5-0.9B lies in the addition of two specialized tasks:

1. Seal Recognition: We introduce a specific instruction to handle official seals and stamps, addressing challenges such as curved text, blur images and background interference.

2. Text Spotting (Grounded OCR): Unlike standard OCR, which solely outputs textual content, the text spotting task requires the model to simultaneously predict the text and its precise spatial location following the natural reading order. To accommodate complex layouts found in real-world scenarios (e.g., rotated text, common scene, or dense forms), we adopt a 4-point quadrilateral representation rather than the traditional 2-point bounding box. The 4-point format defines a text region using four vertices: Top-Left (TL), Top-Right (TR), Bottom-Right (BR), and Bottom-Left (BL). This formulation provides superior flexibility in localizing inclined and irregular text shapes that a standard axis-aligned rectangle cannot tightly enclose.

Formally, for a given text instance, the target sequence is constructed by appending eight location tokens to the text tokens:

 $$ Y=Text\oplus<LOC\_{x}_{TL}><LOC\_{y}_{TL}>\cdots<LOC\_{y}_{BL}> $$ 

Here, we introduce a set of tokens { $ <LOC\_0> $,...,  $ <LOC\_1000> $} to the model's vocabulary to represent normalized coordinates. Unlike treating coordinates as plain numerical text, these dedicated special tokens allow the model to learn specific embeddings for spatial information and prevent tokenization fragmentation.

For example, a recognized instance of the word "DREAM" is represented as:

 $$ \begin{array}{l} DREAM<LOC\_{2}53><LOC\_{2}86><LOC\_{3}46><LOC\_{2}98><LOC\_{3}45><LOC\_{3}39><LOC\_{2}52>\\<LOC\_{3}30>\end{array} $$ 

This unified representation enables the model to perform end-to-end recognition and fine-grained localization within a single generation pass.

To enhance generalization and unify diverse label styles, we introduce a Reinforcement Learning stage leveraging Group Relative Policy Optimization(GRPO) [20]. By executing parallel rollouts and calculating relative advantages within each group, GRPO facilitates robust policy updates and mitigates style inconsistency. This process is supported by a dynamic data screening protocol that prioritizes challenging samples with high reward potential and entropy uncertainty, ensuring the model focuses on non-trivial, high-value learning cases.