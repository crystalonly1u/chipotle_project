from dash import html, dcc
import plotly.express as px

def render(app, df):  #app to bind output to, plus the dataset
    fig = px.bar(df, x='item_name', y='order_price')
    return html.Div(dcc.Graph(figure=fig), id = 'bar1')