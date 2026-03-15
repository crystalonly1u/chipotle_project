from dash import html, dcc
import plotly.express as px

def render(app, df):
    fig = px.bar(df, x='order_price', y='item_name', orientation='h')
    return html.Div(dcc.Graph(figure=fig), id = 'barh1')
