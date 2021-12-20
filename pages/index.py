# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Looking into Hypothesis Testing and Regression

            In this web application using the Fish Market Dataset created by Aung Pyae, we explore the key concepts of hypothesis testing as well as linear regression and understanding the R-squared value 

            This application walks you through the process of how the linear regression model was created. Describe the insights that were found. As well as provide an interactive tool for viewing model predictions
            
            """
        ),
        dcc.Link(dbc.Button('View Model', color='primary'), href='/predictions')
    ],
    md=4,
)

df = pd.read_csv('./data/Fish.csv')
fig = px.scatter(df, x='Length3', y='Weight', labels={
                                                "Weight": "Fish Weight (grams)",
                                                "Length3": "Fish Cross Length (cm)"
                                            },)


column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])