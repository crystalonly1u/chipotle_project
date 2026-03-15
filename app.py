from dash import Dash, html 
import dash_bootstrap_components as dbc
from util import get_data
from components import pie_component, bar_component, barh_component, scatter_component

PATH = 'chipotle.csv'
df = get_data(PATH)

app = Dash(external_stylesheets = [dbc.themes.COSMO])
app.layout = dbc.Container ([ #dbc has preset margins with 12 columns of space available
    html.H1("Top 10 Best Selling Items x Revenue"),
    dbc.Row([
        dbc.Col(pie_component.render(app, df), lg=6),
        dbc.Col(bar_component.render(app, df), lg=6)
    ]),  #exactly 2 rows and 2 columns
       dbc.Row([
        dbc.Col(barh_component.render(app, df), lg=6),
        dbc.Col(scatter_component.render(app, df), lg=6)
    ])   
   
    ]) 
app.run()