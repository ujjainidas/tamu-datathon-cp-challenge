# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:25:24 2019

@author: thisi
"""
import pandas as pd
from matplotlib import pyplot as plt
# ENTER YOUR CODE HERE
cars_data = pd.read_csv("https://cosmos-api-prod-datasetsbucket-iuph41amgzfj.s3.amazonaws.com/cars_data.csv", sep = ",")

data = cars_data["symboling"]

# Set this variable equal to your answer
symboling_descriptive = data.describe()

# ENTER YOUR CODE HERE
cars_data_to_mean = cars_data.fillna(cars_data.mean())
losses_data = cars_data_to_mean["losses"]
# Set this variable equal to your answer
losses_descriptive = losses_data.describe()

# ENTER YOUR CODE HERE
plt.scatter(cars_data_to_mean["weight"], cars_data_to_mean["price"])
# Set this variable equal to your answer (Hint: It should be a string)
price_weight_relationship = "positive exponential"