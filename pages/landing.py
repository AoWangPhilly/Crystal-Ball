import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.P(
        className="landing-header",
        children="Make Desicions with Predictions",
    ),

    html.P(
        className="landing-subheader",
        children="Powerful modeling predictions based on key financial indicators to help you make investment decisions",
    ),

    html.Div(
        className="text-center",
        children=[
            dbc.Button(
                className="landing-sign-up-btn shadow",
                children="Sign up",
                href="/register"
            ),
        ]
    ),

    html.Div(
        className="d-flex justify-content-center",
        children=[
            html.P(
                className="d-inline p-1",
                children="Have an account?"
            ),
            dcc.Link(
                className="d-inline p-1",
                children=f"Log in", href="/login"
            )
        ]
    ),
    html.Div(
        className="d-flex justify-content-center",
        children=[
            html.Img(
                className="landing-mockup",
                src=r'assets/images/Macbook.png',
                alt='macbook'
            )
        ]
    )

])
