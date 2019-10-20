# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:52:19 2019

@author: thisi
"""

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=";")
df.head()

# YOUR CODE HERE...
wine_target_name = "quality"
wine_target = df[wine_target_name]
wine_features = df.drop(wine_target_name, axis = 1)
wine_feature_names = wine_features.columns

corr = df.corr()

max = 0
max_feature = ' '

for i, feature_name in enumerate(wine_feature_names):
  corr_num = corr[feature_name][wine_target_name]
  if corr_num > max:
    max = corr_num
    max_feature = feature_name
  
# Set the following variable to the feature which has the highest correlation with 'quality'
most_correlated = feature_name  # e.g. most_correlated = 'sulphates'

# Build a model with the following features: ["alcohol", "density", "residual sugar"]
# Find the variable that is causing multicollinearity and is least correlated to the target
# YOUR CODE HERE...

wine_test_names = ["alcohol", "density", "residual sugar"]
wine_features = df[wine_test_names]

wine_model = LinearRegression().fit(wine_features, wine_target)
wine_score = wine_model.score(wine_features, wine_target)

correlation_matrix = wine_features.corr()

sns.heatmap(correlation_matrix, square=True, annot=True)

for i, feature_names in enumerate(wine_test_names):
  print(corr[feature_names][wine_target_name])

multicollinear_feature = "residual sugar"  # e.g. multicollinear_feature = "alcohol"

# Build a linear regression model with the features: ["alcohol", "density", "volatile acidity"]
# All other variables held constant, how much does 'quality' change with a one unit increase in 'alcohol'?
# Round your answer to 4 decimal places
# YOUR CODE HERE...
wine_test2_names = ["alcohol", "density", "volatile acidity"]
wine_features2 = df[wine_test2_names]

wine_model2 = LinearRegression().fit(wine_features2, wine_target)
wine_score2 = wine_model2.score(wine_features2, wine_target)

print(wine_score2)

coef2 = wine_model2.coef_
intercept2 = wine_model2.intercept_

print(coef2)
print(intercept2)

print("quality =", int(intercept2), "+", " + ".join(["{}*{:.0f}".format(f, c) for f, c in zip(wine_features2, coef2)]))
effect = coef2[0]  # e.g. effect = 1.1234