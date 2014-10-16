# Vito D'Orazio
# explore.R
# script for loading data and plotting one survey question from Worker Representation and Participation dataset on Dataverse

# remove objects from current environment
rm(list=ls())

# set working directory
setwd("/Users/vjdorazio/Desktop/IQSS/eyeData/study_GITCZNWZYE")

# read data
mydata <- read.delim("data/wrps1.tab")

# table the data
plottable <- table(mydata$q1)

# plot a barplot
barplot(plottable)