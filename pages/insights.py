# Imports from 3rd party libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc

# Imports from this application
from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Hypothesis Testing Market Fish Versus Wild Fish

            **Initial Hypothesis**

            Null Hypothesis:

            - The species market sample weight will be related to the species population as a whole weight

            Alternative Hypothesis:

            - The species market sample weight will **not** be related to the species population sample weight

            Setting a p-value threshold of 5%, 0.05

            Using only Perch and Bream fish since their samples are each over 30

            **T-test on species weights results**

            In the case of the Bream Fish sample weight versus the Bream Fish population weight:
            - t-score: ~ -25.22
            - p-value: ~ 1.34e-23
            - The p-value was less than 0.05. We reject the null hypothesis showing there is a statistically significant difference between the mean weights

            In the case of the Perch Fish sample weight versus the Perch Fish population weight:
            - t-score: ~ -14.48
            - p-value: ~ 0.00049
            - The p-value was less than 0.05. We reject the null hypothesis showing there is a statistically significant difference between the mean weights

            In the case of the Perch Fish sample weight versus the Bream Fish sample weight:
            - t-score: ~ -3.61
            - p-value: ~ 0.00049
            - The p-value was less than 0.05. We reject the null hypothesis showing there is a statistically significant difference between the mean weights

            **Hypothesis Testing Market Fish Versus Wild Fish Conclusion**

            The fish captured for use in markets is statistically different from the fish found in the ocean(wild). The consequence of this is that the work that is to be done following this hypothesis testing such as (Linear Regression and Prediction Pipeline) will not have a use case in the population of fish as a whole but only for fish found in fish markets similar to where Aung Pyae's fish market data was collected.


            ### Graphing of Feature Relationships

            When graphing there are very strong linear relationship between features

            **ideas**
            - Is there a way to combine features to reduce the dimensionality
            - Is there a way to combine features to create a more linear overall relationship

            **concerns**
            - In some comparisons, there seems to be branching or clustering(This is possibly due to different species)
            - Pipeline may have to separate fish species and we will need a separate model for each kind of species

            ![pairplot](./assets/pairplot.png "pairplot")

            """
        ),
    ],
)

layout = dbc.Row([column1])