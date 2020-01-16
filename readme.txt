This folder contains Matlab code related to the following paper:
CMF-Impute: an accurate imputation tool for single-cell RNA-seq data

Our Matlab (>= 2017) code admits a few experimental usages and has not been extensively tested. 

An example is illustrated in demo.m

The SC3 package was downloaded from R Bioconductor (http://bioconductor.org/packages/release/bioc/html/SC3.html).
To ensure consistency with other tools, the gene filtering option is turned off (gene.filter =FALSE). Other options are set to default values.

T-SNE: We used matlab's built-in function tsne(), where the parameter “perplexity” is set to 10.
Monocle 2 was downloaded from the R Bioconductor page (https://bioconductor.org/packages/release/bioc/html/monocle.html). 
