## ---- include = FALSE------------------------------------------------------
rm(list = ls())
gc()
setwd("/Users/mac/Downloads/")
knitr::opts_chunk$set(
  collapse = TRUE,
  comment = "#>"
)

## ----setup-----------------------------------------------------------------
library("splatter")
library("scater")
library("ggplot2")


# Five groups
## ----nGenes----------------------------------------------------------------
# Set the number of genes to 1000
params = newSplatParams()

params = setParams(params, list(batchCells = 1000,
                                nGenes =10000,
                                group.prob = c(0.30, 0.3,0.4),
                                de.prob = c(0.05, 0.08, 0.01),
                                de.facLoc = 0.5,
                                de.facScale = 0.8)
)

# Set up the vector of dropout.mid
#dropout_mid = c(4, 5, 5.5)

# determine if it is a good parameter


# Generate the simulation data using Splatter package
sim = splatSimulateGroups(params,
                          dropout.shape =c(-0.05,-0.05,-0.05),
                          dropout.mid = c(0,0,0),
                          dropout.type = "group",
                          )
sim <- normalize(sim)
plotPCA(sim, colour_by = "Group")
X <- assays(sim)$count
X.log <- log10(X+ 1)
simlabel<-sim$Group
write.csv(X.log,file = "sim.csv",row.names = T)
#write.csv(simlabel,file = "simlabel_05.csv",row.names = T)
