WMT25, indicating that moderate model scaling boosts translation quality. As open-source models, they enable broader academic and industrial adoption than closed-source alternatives such as Gemini 3.0 Pro.

### 3.2 Human Evaluation

<div style="text-align: center;">Table 2: Human evaluation of translation quality for the Chinese-to-English (ZH ⇒ EN) and English-to-Chinese (EN ⇒ ZH) directions. The highest scores are shown in bold.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Model</td><td style='text-align: center; word-wrap: break-word;'>ZH $ \rightarrow $EN</td><td style='text-align: center; word-wrap: break-word;'>EN $ \rightarrow $ZH</td><td style='text-align: center; word-wrap: break-word;'>Avg.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Baidu-Translator</td><td style='text-align: center; word-wrap: break-word;'>2.75</td><td style='text-align: center; word-wrap: break-word;'>2.46</td><td style='text-align: center; word-wrap: break-word;'>2.55</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>iFLYTEK-Translator</td><td style='text-align: center; word-wrap: break-word;'>2.88</td><td style='text-align: center; word-wrap: break-word;'>2.54</td><td style='text-align: center; word-wrap: break-word;'>2.65</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Doubao-Translator</td><td style='text-align: center; word-wrap: break-word;'>2.97</td><td style='text-align: center; word-wrap: break-word;'>2.48</td><td style='text-align: center; word-wrap: break-word;'>2.64</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Microsoft-Translator</td><td style='text-align: center; word-wrap: break-word;'>2.94</td><td style='text-align: center; word-wrap: break-word;'>2.57</td><td style='text-align: center; word-wrap: break-word;'>2.69</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Google-Translator</td><td style='text-align: center; word-wrap: break-word;'>2.84</td><td style='text-align: center; word-wrap: break-word;'>2.10</td><td style='text-align: center; word-wrap: break-word;'>2.34</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HY-MT1.5-1.8B</td><td style='text-align: center; word-wrap: break-word;'>3.01</td><td style='text-align: center; word-wrap: break-word;'>2.61</td><td style='text-align: center; word-wrap: break-word;'>2.74</td></tr></table>

To address the limitations of automatic evaluation (Lavie et al., 2025), we conduct human evaluation in which multilingual experts rate translations on a 0–4 scale, focusing on pre-annotated error-prone points and considering accuracy, fluency, and idiomaticity.

As shown in Table 2, the evaluated models are divided into two tiers: the lightweight specialized model HY-MT1.5-1.8B and mainstream commercial translation systems. HY-MT1.5-1.8B achieves the highest average score (2.74), outperforming all commercial systems, which is consistent with automatic evaluation. Most systems perform better in  $ ZH \Rightarrow EN $ than  $ EN \Rightarrow ZH $, mainly due to the complexity of Chinese syntax generation.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_278_764_908_1227.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">Figure 4: Average response time versus translation quality for different translation models.</div>


#### 3.3 Efficiency of HY-MT1.5 Models

To evaluate the translation efficiency of the HY-MT1.5 models, a standardized speed test was conducted: 100 Chinese texts (average length 50 tokens, covering daily and general business scenarios) were sequentially translated into English, with the average response time used as the primary metric.

As shown in Figure 4, the HY-MT1.5 models exhibit a superior balance between translation quality and response efficiency. Specifically, HY-MT1.5-1.8B achieves an FLORES-200 quality score of approximately 78% while maintaining an average response time of 0.18 seconds, indicating a clear speed advantage. The length of the test texts aligns with practical translation needs in daily communication, office work, and quick information retrieval, and the 0.18-second instant response time eliminates user waiting.