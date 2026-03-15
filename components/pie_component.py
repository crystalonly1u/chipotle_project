from dash import html, dcc #dash core components to convert data to js and html
import plotly.express as px 


def render(app, df):    
    fig = px.pie(df, values = 'order_price', names = 'item_name')
    return html.Div(dcc.Graph(figure = fig), id = 'pie_chart') #Div = generic HTML container
