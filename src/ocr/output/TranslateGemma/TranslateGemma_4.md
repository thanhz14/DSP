each of the 55 language pairs, presented in Appendix A, reveals that the improvements of TranslateGemma are consistent across all 55 language pairs evaluated. Some example improvements for specific languages are

• English to German: 1.63 down to 1.19.

• English to Spanish: 2.54 down to 1.88,

• English to Hebrew: 3.90 down to 2.72,

• English to Swahili: 5.92 down to 4.45,

• English to Lithuanian: 6.01 down to 4.39,

• English to Estonian: 6.40 down to 4.61 and

• English to Icelandic: 8.31 down to 5.69.

These examples highlight the model's improved ability to handle a diverse range of languages, both for high-resource languages (e.g. German, English) as well as low-resource ones (e.g. Icelandic, Swahili).

We also hypothesize that the 27B model, with its higher capacity, will have benefited more from the vast amount of languages seen during the SFT phase (detailed in Appendix C), although we do not have direct experimental confirmation of this.

#### 5.2. Prompting the Model

The model has been trained using the prompt shown in Figure 3, which is also the prompt we used in our evaluations. We recommend using the same prompt for producing new translations. Tools for automatically wrapping the text with it are provided in the model repository.

#### 5.3. Image Translation

We used the Vistra benchmark (Salesky et al., 2024) to assess whether the models retained their ability to translate text within images after our additional training steps. Note that no multimodal training data was used in the SFT or RL steps reported in this work. In order to simplify the evaluation protocol, we selected only images that, according to the reference, contained a single instance of text. This resulted in a set of 264 images. An example is shown in Figure 4. The input to the model was just the image together with a

<div style="text-align: center;">Table 2 | Automatic evaluation results using MetricX and CoMET22 (C22) for image translation performance, on the Vistra corpus. The scores are the average of translating from English into German, Spanish, Russian and Chinese.</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Size</td><td style='text-align: center; word-wrap: break-word;'>System</td><td style='text-align: center; word-wrap: break-word;'>MetricX $ \downarrow $</td><td style='text-align: center; word-wrap: break-word;'>C22 $ \uparrow $</td></tr><tr><td rowspan="2">27B</td><td style='text-align: center; word-wrap: break-word;'>Gemma 3</td><td style='text-align: center; word-wrap: break-word;'>2.03</td><td style='text-align: center; word-wrap: break-word;'>76.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TranslateGemma</td><td style='text-align: center; word-wrap: break-word;'>1.58</td><td style='text-align: center; word-wrap: break-word;'>77.7</td></tr><tr><td rowspan="2">12B</td><td style='text-align: center; word-wrap: break-word;'>Gemma 3</td><td style='text-align: center; word-wrap: break-word;'>2.33</td><td style='text-align: center; word-wrap: break-word;'>74.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TranslateGemma</td><td style='text-align: center; word-wrap: break-word;'>2.08</td><td style='text-align: center; word-wrap: break-word;'>72.8</td></tr><tr><td rowspan="2">4B</td><td style='text-align: center; word-wrap: break-word;'>Gemma 3</td><td style='text-align: center; word-wrap: break-word;'>2.60</td><td style='text-align: center; word-wrap: break-word;'>69.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>TranslateGemma</td><td style='text-align: center; word-wrap: break-word;'>2.58</td><td style='text-align: center; word-wrap: break-word;'>70.7</td></tr></table>

prompt asking it to translate the text in it. $ ^{2} $ In particular, we did not include any other information about the text, like its location in the image or a previous OCR pass.

The results, presented in Table 2, show that TranslateGemma retains the image processing capabilities of the base Gemma 3 models. The improvements in translation quality attained by TranslateGemma carry over for this task, with the exception of the 12B model measured in CoMET22. We see MetricX score improvements of nearly 0.5 points in the case of the 27B model, or 0.25 for the 12B model.

The smaller 4B model obtains only small improvements when compared to the baseline, probably due to its limited capacity.

### 6. Human Evaluation

We conduct an additional human evaluation on a limited set of language directions to measure TranslateGemma's translation performance. We do so using MQM (Freitag et al., 2021; Lommel et al., 2014), a human evaluation framework where professional translators highlight error spans in translations, with document context, assigning a severity and category to each, with a score being automatically derived by counting