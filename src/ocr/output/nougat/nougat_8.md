Here  $ \ell $ is the signal of logits and x the index. Using this new signal we compute variances again but this time from the point x to the end of the sequence

 $$ \mathrm{Var}\mathrm{End}_{B}[\ell](x)=\frac{1}{S-x}\sum_{i=x}^{S}\left(\mathrm{Var}\mathrm{Win}_{B}[\ell](i)-\frac{1}{S-x}\sum_{j=x}^{S}\mathrm{Var}\mathrm{Win}_{B}[\ell](i)\right)^{2}. $$ 

If this signal drops below a certain threshold (we choose 6.75) and stays below for the remainder of the sequence, we classify the sequence to have repetitions.

During inference time, it is obviously not possible to compute the to the end of the sequence if our goal is to stop generation at an earlier point in time. So here we work with a subset of the last 200 tokens and a half the threshold. After the generation is finished, the procedure as described above is repeated for the full sequence.

### 5.5 Limitations & Future work

Utility The utility of the model is limited by a number of factors. First, the problem with repetitions outlined in section 5.4. The model is trained on research papers, which means it works particularly well on documents with a similar structure. However, it can still accurately convert other types of documents.

Nearly every dataset sample is in English. Initial tests on a small sample suggest that the model’s performance with other Latin-based languages is satisfactory, although any special characters from these languages will be replaced with the closest equivalent from the Latin alphabet. Non-Latin script languages result in instant repetitions.

Generation Speed On a machine with a NVIDIA A10G graphics card with 24GB VRAM we can process 6 pages in parallel. The generation speed depends heavily on the amount of text on any given page. With an average number of tokens of  $ \approx $ 1400 we get an mean generation time of 19.5s per batch for the base model without any inference optimization. Compared to classical approaches (GROBID 10.6 PDF/s [4]) this is very slow, but it is not limited to digital-born PDFs and can correctly parse mathematical expressions.

Future work The model is trained on one page at a time without knowledge about other pages in the document. This results in inconsistencies across the document. Most notably in the bibliography where the model was trained on different styles or section titles where sometimes numbers are skipped or hallucinated. Though handling each page separately significantly improves parallelization and scalability, it may diminish the quality of the merged document.

The primary challenge to solve is the tendency for the model to collapse into a repeating loop, which is left for future work.

## 6 Conclusion

In this work, we present Nougat, an end-to-end trainable encoder-decoder transformer based model for converting document pages to markup. We apply recent advances in visual document understanding to a novel OCR task. Distinct from related approaches, our method does not rely on OCR or embedded text representations, instead relying solely on the rasterized document page. Moreover, we have illustrated an automatic and unsupervised dataset generation process that we used to successfully train the model for scientific document to markup conversion. Overall, our approach has shown great potential for not only extracting text from digital-born PDFs but also for converting scanned papers and textbooks. We hope this work can be a starting point for future research in related domains.

All the code for model evaluation, training and dataset generation can be accessed at https://github.com/facebookresearch/nougat.

## 7 Acknowledgments

Thanks to Ross Taylor, Marcin Kardas, Iliyan Zarov, Kevin Stone, Jian Xiang Kuan, Andrew Poulton and Hugo Touvron for their valuable discussions and feedback.

Thanks to Faisal Azhar for the support throughout the project.

## References

[1] Sebastian Spiegler. Statistics of the Common Crawl Corpus 2012, June 2013. URL https://docs.google.com/file/d/1_9698uglerxB9nAglvaHkEgU-iZNm1TvVGucW7245-WGvZq47teNpb_uL5N9.