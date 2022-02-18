# Imports from 3rd party libraries
import dash_bootstrap_components as dbc
from dash import dcc

# Imports from this application
from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            # Fish Weight Dataset and Analysis

            The "Fish Market" dataset is a small dataset found on *Kaggle.com* created by Aung Pyae. This dataset is a record of seven types of species commonly found in fish markets. The purpose of this project is to explore and analyze this dataset and fully understand its nature and relationships. Then build a simple linear regression pipeline to make predictions on fish weight. (This is a basic dataset where the outcomes are relatively predictable and intuitive. This project is much more about the understanding of how to use these statistical tools than to draw any real use from this dataset)

            **The Features of the dataset are:**
            - Species: The type of fish, dtype: 'O'/str
            - Weight: The recorded Weight of the fish in grams (g), dtype: 'int'
            - Length1: Vertical length in centimeters (cm), dtype: 'int'
            - Length2: Diagonal length in centimeters (cm), dtype: 'int'
            - Length3: Cross length in centimeters (cm), dtype: 'int'
            - Height: Height in centimeters (cm), dtype: 'int'
            - Width: Diagonal width in centimeters (cm), dtype: 'int'

            **Items to be explored**
            - Weight distribution in the dataset
            - Statistical significance between a species's population mean fish weight and our sample species' mean fish weight
                (Our sample is a collection of market fish, fish sold in markets may not be a reflection of fish in the ocean)
            - Statistical significance between different species mean weight
            - Feature analysis and engineering
            - Analysing the correlation between fish lengths and fish weights with Linear Regression
            - Inference on Linear Regression


            ## Initial Look of the Data

            **Analysis on weight distribution**

            ![Weight Distribution](./assets/weight_distribution.png "Weight Distribution")

            **Central Limit Theorem and effect on weight distribution**

            ![CLT](./assets/clt.png "CLT")

            ## Linear Regression and Feature Pipeline

            There are several features in the Fish Market Dataset that correlate strongly with the weight of an observed fish. We find that there is a strong linear relationship between a given fish's length measurements and their weight. Intuitively this makes sense and in the following cells, our findings will be demonstrated. Also, given the strong correlation found in this dataset, we can implement a relatively strong linear regression model.

            **Initial Hypothesis**

            Null Hypothesis:

            - The coefficient of our compared features to target will be equal to zero

            Alternative Hypothesis:

            - The coefficient of our compared features to target will **not** be equal to zero

            ### Feature Dimentionality Reduction

            By collapsing the Length3, Height, and Width variables on top of each other we create a more uniform relationship reducing the need for creating a separate model for each fish species.

            ![linear1](./assets/linear1.png "linear1")

            ![linear2](./assets/linear2.png "linear2")

            ### Visual Linear Regression and 95% Confidence Intervale

            ![ci](./assets/ci.png "ci")

            ### Inference for Linear Regression

            We find that our R2 and Adj. R2 values (the percentage of variation that can be explained by the feature) rank at 0.961 and 0.960 which is a notable improvement from the 0.88 Adj. R2 value before the volume dimension reduction feature. With a propper pipeline, this model can be used to predict the weights of fish based on length measurements with a high degree of certainty.

            Overall we reject the Null Hypothesis given that most of our p-values are equal to zero. However, for Volume, the p-value came to be zero...

            ```
                                        OLS Regression Results                            
            ==============================================================================
            Dep. Variable:                 Weight   R-squared:                       0.961
            Model:                            OLS   Adj. R-squared:                  0.960
            Method:                 Least Squares   F-statistic:                     629.7
            Date:                Tue, 07 Dec 2021   Prob (F-statistic):          1.22e-104
            Time:                        17:27:19   Log-Likelihood:                -901.52
            No. Observations:                 159   AIC:                             1817.
            Df Residuals:                     152   BIC:                             1839.
            Df Model:                           6                                         
            Covariance Type:            nonrobust                                         
            ==============================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
            ------------------------------------------------------------------------------
            Intercept   -102.8532     28.695     -3.584      0.000    -159.547     -46.160
            Volume         0.2009      0.012     17.288      0.000       0.178       0.224
            Length1       20.9835     23.545      0.891      0.374     -25.534      67.501
            Length2        8.5528     24.342      0.351      0.726     -39.539      56.645
            Length3      -13.9921     10.146     -1.379      0.170     -34.038       6.054
            Height       -17.1465      5.724     -2.995      0.003     -28.456      -5.837
            Width        -10.0436     12.015     -0.836      0.405     -33.782      13.695
            ==============================================================================
            Omnibus:                       59.346   Durbin-Watson:                   0.951
            Prob(Omnibus):                  0.000   Jarque-Bera (JB):              412.609
            Skew:                           1.131   Prob(JB):                     2.53e-90
            Kurtosis:                      10.561   Cond. No.                     1.33e+04
            ==============================================================================
            ```

            ### Building Fish Market Linear Regression Pipeline

            Overall performance is well except for the occasional negative weight prediction.

            Use the model on the Predictions page

            """
        ),
    ],
)

layout = dbc.Row([column1])