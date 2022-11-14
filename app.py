from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash

external_stylesheets = [
    "https://fonts.googleapis.com/css?family=Inter",
    dbc.themes.PULSE
]
app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)
