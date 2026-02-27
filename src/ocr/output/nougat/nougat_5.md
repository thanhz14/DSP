In addition, the splitting algorithm of the source code will in some cases include text from the previous page or cut off words from the end. This is especially true for “invisible” characters used for formatting, like italic, bold text or section header.

For PMC papers the inline math is written as Unicode or italic text, while display math equations or tables are often included in image format and will therefore be ignored.

Each of these issues reduces the overall data quality. However, the large number of training samples compensates for these small errors.

## 5 Results & Evaluation

<div style="text-align: center;"><img src="imgs/img_in_image_box_128_416_1040_978.jpg" alt="Image" width="76%" /></div>


 $$ \frac{R-\rho\cos\theta}{\sin^{2}\theta}=\frac{\alpha}{\pi\Lambda}\Biggl\langle\int_{-\infty}^{\infty}d t\;\exp\left(-\frac{\Delta(t,z)}{2\Lambda^{2}}\right)\left(\kappa-t\right)\Biggr\rangle_{s} $$ 

 $$ 1-\frac{\rho^{2}+R^{2}-2\rho R\cos\theta}{\sin^{2}\theta}=2\alpha\Biggl\langle\int_{-\infty}^{\infty}d t\frac{e^{-\frac{(\alpha-\mu_{0})^{2}}{2}}}{\sqrt{2\pi}\sqrt{1-\rho^{2}}}H\left(\frac{\Gamma(t,z)}{\sqrt{1-\rho^{2}}\Lambda}\right)(\kappa-t)^{2}\Biggr\rangle, $$ 

 $$ \frac{\rho-R\cos\theta}{\sin^{2}\theta}=2\alpha\bigg(\int_{-\infty}^{\infty}dt\frac{e^{-\frac{t-p\alpha}{2(1-p\alpha)^{2}}}}{\sqrt{2\pi}\sqrt{1-p^{2}}}H\bigg(\frac{\Gamma(t,z)}{\sqrt{1-p^{2}}\Lambda}\bigg)\bigg(\frac{z-\rho t}{1-\rho^{2}}\bigg)(\kappa-t) $$ 

 $$ +\frac{1}{2\pi\Lambda}\exp\left(-\frac{\Delta(t,z)}{2\Lambda^{2}}\right)\left(\frac{\rho R-\cos\theta}{1-\rho^{2}}\right)\left(\kappa-t\right)\Biggr)_{s} $$ 

<div style="text-align: center;">Figure 5: Example of a page with many mathematical equations taken from [41]. Left: Image of a page in the document, Right: Model output converted to LaTeX and rendered to back into a PDF. Examples of scanned documents can be found in the appendix B.</div>


In this section we discuss the results and performance of the model. For an example see Fig. 5 or go to Sec. B. The model focuses only on the important content relevant features of the page. The box around the equations is skipped.

### 5.1 Metrics

We report the following metrics on our test set.

Edit distance The edit distance, or Levenshtein distance [39], measures the number of character manipulations (insertions, deletions, substitutions) it takes to get from one string to another. In this work we consider the normalized edit distance, where we divide by the total number of characters.

BLEU The BLEU [42] metric was originally introduced for measuring the quality of text that has been machine-translated from one language to another. The metric computes a score based on the number of matching n-grams between the candidate and reference sentence.

METEOR Another machine-translating metric with a focus on recall instead of precision, introduced in [43].

F-measure We also compute the F1-score and report the precision and recall.