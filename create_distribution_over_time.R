library(tidyr)
library(ggplot2)
library(dplyr)
library(zoo)

data = read.csv("/users/dianaenggist/Documents/Advanced_Textmining/Project/textmining_teamblue/time_matrix.csv")
data$month = as.Date(as.yearmon(data$month))
data$X0 = as.factor(data$X0)
ggplot(data,aes(x=X0, y=month, fill=X0)) + geom_boxplot() + xlab('Cluster') + ylab('Time') + scale_fill_discrete(name='Assumed Sentiments',labels=c("0: Negative", "1: Positive", "2: Neutral") )

