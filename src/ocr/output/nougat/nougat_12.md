## A Dataset


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Name</td><td style='text-align: center; word-wrap: break-word;'>Number of Pages</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>arXiv</td><td style='text-align: center; word-wrap: break-word;'>7,511,745</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PMC</td><td style='text-align: center; word-wrap: break-word;'>536,319</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IDL</td><td style='text-align: center; word-wrap: break-word;'>446,777</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Total</td><td style='text-align: center; word-wrap: break-word;'>8,204,754</td></tr></table>

<div style="text-align: center;">Table A.1: Dataset composition</div>


The most important data source is arXiv, making up > 91.5% of the corpus. On arXiv most research documents are paired with the LaTeX source code provided by the authors. The LaTeX source offers more information and is left unprocessed, unlike the XML format from PMC where equations and tables are frequently substituted with images. This allows us to select exactly which information we need to build the dataset.

## B Examples

In this section we converted some pages from old text books using the Nougat base model. The text books from the Internet Archive $ ^{11} $ and Project Gutenberg $ ^{12} $ and are in public domain.

The performance for these scanned pages is noticeable worse than for digital-born documents. However, the model does generate sensible text for each page with few errors. For example see the first row of Fig. B.1. Here the model mistakes the almost illegible exponent n for *. In the second row of the same figure the model falls into a repetitive loop after predicting another comma instead of a dot. Similar problems can be seen in Fig. B.2.

In Fig. B.3 we present pages, scanned with a mobile device, from a printed master thesis and the Nougat output. The model is robust to the artifacts that arise when hand-scanning a document.

Explore the examples in this section on the project page: https://facebookresearch.github.io/nougat.