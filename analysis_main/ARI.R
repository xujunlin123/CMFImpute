#rm(list = ls()) 
setwd("/Users/mac/Downloads/uso/")
data1 <- read.table("sc3_results_label.txt",header=T,sep="\t",check.names=F) 
data2 <- read.table("us_label.txt",header=T,sep="\t",check.names=F) 
data1<- as.matrix(data1)
data2<- as.matrix(data2)
#c<-cor(data1,data2,method="kendall")
adjustedRandIndex <- function (x, y)
{
  x <- as.vector(x)
  y <- as.vector(y)
  if (length(x) != length(y))
    stop("arguments must be vectors of the same length")
  tab <- table(x, y)
  if (all(dim(tab) == c(1, 1)))
    return(1)
  a <- sum(choose(tab, 2))
  b <- sum(choose(rowSums(tab), 2)) - a
  c <- sum(choose(colSums(tab), 2)) - a
  d <- choose(sum(tab), 2) - a - b - c
  ARI <- (a - (a + b) * (a + c)/(a + b + c + d))/((a + b + a + c)/2 - (a + b) * (a + c)/(a + b + c + d))
  return(ARI)
}
Output_S <- adjustedRandIndex(data1,data2)
adjustedRandIndex(data1, data2) 


