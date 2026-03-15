from dash import html, dcc
import pandas as pd
import plotly.express as px

def render(app, df):  #app to bind output to, plus the dataset
    fig = px.scatter(df, x='item_name', y='order_price', 
                     color = 'item_name',
                     size = 'order_price')
    return html.Div(dcc.Graph(figure=fig), id = 'scatter1')