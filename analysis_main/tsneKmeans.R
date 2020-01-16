rm(list = ls())
library(devtools)
library(mclust)
library(Rtsne)
# before imputation
setwd("/Users/mac/Desktop/")
lpsdata<-read.table("uso_CFM.txt",header=T,row.names=1,sep="\t",check.names=F)
class.label<- read.table("us_label.txt", header=T,sep="\t",check.names=F) 
class.label<-as.matrix(class.label)
lpsdata=as.matrix(lpsdata)
adjustedRandIndex(kmeans(Rtsne(t(as.matrix(lpsdata)))$Y, centers = 9)$cluster, class.label)
# after imputation
#adjustedRandIndex(kmeans(Rtsne(t(as.matrix(X.imp)))$Y, centers = 4)$cluster, class.label)

