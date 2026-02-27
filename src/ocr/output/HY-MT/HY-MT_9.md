<div style="text-align: center;">Table 4: Translation performance metrics of different quantization schemes. The highest and second-best scores are shown in bold and underlined, respectively.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Models</td><td rowspan="2">Metrics</td><td colspan="3">FLORES-200</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ZH  $ \Leftrightarrow $ XX</td><td style='text-align: center; word-wrap: break-word;'>EN  $ \Leftrightarrow $ XX</td><td style='text-align: center; word-wrap: break-word;'>XX  $ \Leftrightarrow $ XX</td></tr><tr><td rowspan="2">HY-MT1.5-1.8B</td><td style='text-align: center; word-wrap: break-word;'>XCOMET-XXL</td><td style='text-align: center; word-wrap: break-word;'>0.8361</td><td style='text-align: center; word-wrap: break-word;'>0.8942</td><td style='text-align: center; word-wrap: break-word;'>0.7840</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CometKiwi</td><td style='text-align: center; word-wrap: break-word;'>0.7655</td><td style='text-align: center; word-wrap: break-word;'>0.8411</td><td style='text-align: center; word-wrap: break-word;'>0.7182</td></tr><tr><td rowspan="2">HY-MT1.5-1.8B-FP8</td><td style='text-align: center; word-wrap: break-word;'>XCOMET-XXL</td><td style='text-align: center; word-wrap: break-word;'>0.8379</td><td style='text-align: center; word-wrap: break-word;'>0.8905</td><td style='text-align: center; word-wrap: break-word;'>0.7794</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CometKiwi</td><td style='text-align: center; word-wrap: break-word;'>0.7659</td><td style='text-align: center; word-wrap: break-word;'>0.8396</td><td style='text-align: center; word-wrap: break-word;'>0.7156</td></tr><tr><td rowspan="2">HY-MT1.5-1.8B-Int4</td><td style='text-align: center; word-wrap: break-word;'>XCOMET-XXL</td><td style='text-align: center; word-wrap: break-word;'>0.8060</td><td style='text-align: center; word-wrap: break-word;'>0.8665</td><td style='text-align: center; word-wrap: break-word;'>0.7336</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CometKiwi</td><td style='text-align: center; word-wrap: break-word;'>0.7462</td><td style='text-align: center; word-wrap: break-word;'>0.8234</td><td style='text-align: center; word-wrap: break-word;'>0.6884</td></tr></table>

the original model while reducing resource consumption, facilitating application on resource-constrained devices.

Future work will focus on three directions: 1) Expanding language coverage to more low-resource and underrepresented languages, enhancing the inclusivity of MT technology; 2) Optimizing the training framework with more efficient knowledge distillation and reinforcement learning to improve the performance-efficiency ratio of small and medium-sized models; 3) Deepening customized translation research by integrating advanced prompt engineering and domain adaptation to better meet industry-specific needs. The HY-MT1.5 models are expected to provide high-quality, efficient, and flexible translation solutions for academic and industrial communities, advancing the development and popularization of MT technology.

## 5 Contributions

### 5.1 Core Contributors

Mao Zheng, Zheng Li, Tao Chen, Mingyang Song, Di Wang

### 5.2 Contributors

Feng Zhang, Tinghao Yu, Chengcheng Xu, Zhenyu Huang, Liya Zhan, Jun Xia, Jiaqi Zhu, Xingwu Sun, Yufei Wang, Can Xu, Liang Dong, Huxin Peng, Fei Cheng, Zheng Zhang, Liqi He, Huashuo Li, Decheng Wu, Guanghua Yu, Kai Wang, Haozhao Kuang

## References

Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr Stanczyk, Sabela Ramos, Matthieu Geist, and Olivier Bachem. On-policy distillation of language models: Learning from self-generated mistakes, 2024. URL https://arxiv.org/abs/2306.13649.

Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate. In Yoshua Bengio and Yann LeCun (eds.), 3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings, 2015. URL http://arxiv.org/abs/1409.0473.

Peter F. Brown, John Cocke, Stephen Della Pietra, Vincent J. Della Pietra, Frederick Jelinek, John D. Lafferty, Robert L. Mercer, and Paul S. Roossin. A statistical approach to machine translation. Comput. Linguistics, 16(2):79–85, 1990.

Peter F. Brown, Stephen Della Pietra, Vincent J. Della Pietra, and Robert L. Mercer. The mathematics of statistical machine translation: Parameter estimation. Comput. Linguistics, 19(2):263–311, 1993.

Shanbo Cheng, Yu Bao, Qian Cao, Luyang Huang, Liyan Kang, Zhicheng Liu, Yu Lu, Wenhao Zhu, Jingwen Chen, Zhichao Huang, Tao Li, Yifu Li, Huiying Lin, Sitong Liu, Ningxin Peng, Shuaijie She, Lu Xu, Nuo Xu, Sen Yang, Runsheng Yu, Yiming Yu, Liehao Zou, Hang Li, Lu Lu, Yuxuan Wang, and Yonghui Wu. Seed-x: Building strong multilingual translation llm with 7b parameters, 2025. URL https://arxiv.org/abs/2507.13618.