## ----knitr-options, echo=FALSE, message=FALSE, warning=FALSE---------------
#rm(list = ls())
rm(list = ls())
gc()
setwd("/Users/mac/Downloads/xujunlin/")
lpsdata<-read.table("uso_5.txt",header=T,row.names=1,sep="\t",check.names=F)
class.label<- read.table("uslabel.txt", header=T,sep="\t",check.names=F) 
class.label<-as.matrix(class.label)
lpsdata=as.matrix(lpsdata)
#lpsdata=log10(lpsdata+1)
yan1<-lpsdata
label<-class.label
## ----knitr-options, echo=FALSE, message=FALSE, warning=FALSE---------------
library(knitr)
opts_chunk$set(fig.align = 'center', fig.width = 6, fig.height = 5, dev = 'png')

## ---- message=FALSE, warning=FALSE-----------------------------------------
library(SingleCellExperiment)
library(SC3)
library(scater)
sce <- SingleCellExperiment(
  assays = list(
    counts = as.matrix(yan1),
   # logcounts = log2(as.matrix(yan1) + 1)
   logcounts = yan1
  ), 
  colData = label
)

# define feature names in feature_symbol column
rowData(sce)$feature_symbol <- rownames(sce)
# remove features with duplicated names
sce <- sce[!duplicated(rowData(sce)$feature_symbol), ]

# define spike-ins
isSpike(sce, "ERCC") <- grepl("ERCC", rowData(sce)$feature_symbol)

## --------------------------------------------------------------------------
plotPCA(sce, colour_by = "cell_type1")

## --------------------------------------------------------------------------
sce <- sc3(sce,gene_filter = FALSE, ks =4, biology = TRUE)

sc3_export_results_xls(sce)

