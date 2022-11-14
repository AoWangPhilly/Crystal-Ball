import dash
from dash import html, dcc

dash.register_page(__name__, path='/register')

layout = html.Div(children=[
    html.H1(children='This is our Register page'),

    html.Div(children='''
        This is our Register page content.
    '''),

])