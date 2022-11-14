import dash
from dash import html, dcc

dash.register_page(__name__, path='/login')

layout = html.Div(children=[
    html.H1(children='This is our Login page'),

    html.Div(children='''
        This is our Login page content.
    '''),

])