# Fish Dimensions Regression Analysis

Introduction

The Fish Dimension Regression Analysis repo aims to preform statistical analysis on the given fish market dataset. The analysis involves hypothesis testing and preforming a multi-dimentional linear regression on the dataset.



The Dataset

The dataset includes seven features containing categorical and numerical data on the fish species, weight, and five length measurements. The dataset was created by Aung Pyae and is hosted on the website kaggle.com. The dataset is optimal for regression modeling as there is strong correlation between fish length and fish weight. During linear regression analysis the “Weight” feature is used as the target feature.

Features

Species (str): The type of fish
Weight (int): The recorded Weight of the fish in grams (g)
Length1 (int): Vertical length in centimeters (cm)
Length2 (int): Diagonal length in centimeters (cm)
Length3 (int): Cross length in centimeters (cm)
Height (int): Height in centimeters (cm)
Width (int): Diagonal width in centimeters (cm)

 **Analysis on weight distribution**

 ![Weight Distribution](assets/weight_distribution.png "Weight Distribution")

**Central Limit Theorem and effect on weight distribution**

![CLT](assets/clt.png "CLT")



Dimensionality Reduction

Using the features “Length3”, ”Height”, and “Width” a feature “Volume” can be created that has a stronger correlation to fish weight. Additionally, a higher R2 score is achieved with the addition of the “Volume” feature as it explains more variation around the mean when compared to the other features individually.

Hypothesis Testing

Null Hypothesis:
The coefficient of our compared features to target will be equal to zero
Alternative Hypothesis:
The coefficient of our compared features to target will not be equal to zero

Inference for Linear Regression



 


