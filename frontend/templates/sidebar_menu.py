import dash_bootstrap_components as dbc
from dash import dcc, html

from frontend.static import CONTENT_STYLE, SIDEBAR_STYLE

content = html.Div(id="page-content", style=CONTENT_STYLE)

sidebar = html.Div(
    [
        html.H2("Меню", className="display-10"),
        html.Hr(),
        html.P(
            "Приложения для предсказания вирусного ПО на Android", style={'fontSize': 17}
        ),
        dbc.Nav(
            [
                dbc.NavLink("Домашняя страница", href="/", active="exact", style={'marginTop': 7, 'marginBottom': 7, 'marginLeft': 0}),
                dbc.NavLink("Предсказания", href="/page-1", active="exact", style={'marginTop': 7, 'marginBottom': 7}),
                dbc.NavLink("Баланс", href="/page-2", active="exact", style={'marginTop': 7, 'marginBottom': 7}),
                dbc.NavLink("Помощь", href="/page-3", active="exact", style={'marginTop': 7, 'marginBottom': 7}),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


LAYOUT_SIDEBAR = html.Div([dcc.Location(id="url"), sidebar, content])