# Vito D'Orazio
# explore.R
# script for loading data and plotting one survey question from Worker Representation and Participation dataset on Dataverse

library(rjson)

# remove objects from current environment
rm(list=ls())

# set working directory
setwd("Projects/eyeData/data")

# read data
mydata <- read.delim("WorkerRepresentation/Data/wrps1.tab")

# table the data
plottable <- table(mydata$s5)

str(plottable)

# plot a barplot
barplot(plottable)

test <- toJSON(plottable)

sink("worker.json")
cat(toJSON((plottable)))
sink()

file.show("worker.json")