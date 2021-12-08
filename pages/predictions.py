# Imports from 3rd party libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
from statsmodels.formula.api import ols

# Imports from this application
from app import app


# Importing data and fitting the model
df = pd.read_csv('./data/Fish.csv')
df['Volume'] = df['Length3'] * df['Height'] * df['Width']
model = ols('Weight ~ Volume + Length1 + Length2 + Length3 + Height + Width', data=df).fit()


# Creating sliders for data input
length1_slider = html.Div(
    [
        dbc.Label("Vertical Length (cm)", html_for="slider"),
        dcc.Slider(id="length1_slider", min=8, max=60, step=1, value=20, tooltip={"placement": "bottom", "always_visible": True}),  
    ]
)

length2_slider = html.Div(
    [
        dbc.Label("Diagonal Length (cm)", html_for="slider"),
        dcc.Slider(id="length2_slider", min=9, max=65, step=1, value=25, tooltip={"placement": "bottom", "always_visible": True}),  
    ]
)

length3_slider = html.Div(
    [
        dbc.Label("Length (cm)", html_for="slider"),
        dcc.Slider(id="length3_slider", min=9, max=70, step=1, value=30, tooltip={"placement": "bottom", "always_visible": True}),  
    ]
)

height_slider = html.Div(
    [
        dbc.Label("Height (cm)", html_for="slider"),
        dcc.Slider(id="height_slider", min=2, max=20, step=1, value=11, tooltip={"placement": "bottom", "always_visible": True}),  
    ]
)

width_slider = html.Div(
    [
        dbc.Label("Width (cm)", html_for="slider"),
        dcc.Slider(id="width_slider", min=1, max=9, step=1, value=4, tooltip={"placement": "bottom", "always_visible": True}),  
    ]
)


column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions

            This application allows you to predict fish weight (g) given length (cm) measurements.
            The predictive model used is a Linear Regression model in this case Ordinary Least Squares.

            """
        ),
        
        length1_slider,
        length2_slider,
        length3_slider,
        height_slider,
        width_slider
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.H1("Estimated Fish Weight...", style={"text-align": "center", "color": "rgb(108,108,108)"}),
        html.H1(id="example-output", style={"text-align": "center", "color": "rgb(17,157,255)"}),
    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output("example-output", "children"),
    [Input("length1_slider", "value"),
     Input("length2_slider", "value"),
     Input("length3_slider", "value"),
     Input("height_slider", "value"),
     Input("width_slider", "value")],
)
def display_page(length1, length2, length3, height, width):

    volume = length3 * height * width
    data = {'Length1': [length1],
            'Length2': [length2],
            'Length3': [length3],
            'Height': [height],
            'Width': [width],
            'Volume': [volume]}

    # Predicts on user input
    output = model.predict(data)

    return str(output[0].round(2)) + " grams"
