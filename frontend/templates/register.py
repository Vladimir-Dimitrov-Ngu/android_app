import dash_core_components as dcc
import dash_html_components as html

layout_for_register = html.Div(
    [
        html.Div(
            [
                html.H2("Регистрация", style={"textAlign": "center"}),
                html.Div(
                    [
                        html.Label(
                            "Логин", style={"marginTop": 20, "marginBottom": 20}
                        ),
                        dcc.Input(id="username", type="text", style={"marginLeft": 23}),
                    ]
                ),
                html.Div(
                    [
                        html.Label("Пароль"),
                        dcc.Input(
                            id="password",
                            type="password",
                            style={
                                "marginTop": 20,
                                "marginBottom": 20,
                                "marginLeft": 10,
                            },
                        ),
                    ]
                ),
                html.Button(
                    "Войти",
                    id="login-button",
                    n_clicks=0,
                    style={"marginLeft": 130, "marginTop": 10},
                ),
                html.Div(id="login-status"),
                html.Div(id="hidden_div_for_redirect_callback"),
            ],
            style={
                "width": "21.5%",
                "margin": "auto",
                "padding": "20px",
                "border": "1px solid #ddd",
                "border-radius": "10px",
            },
        )
    ],
    style={
        "display": "flex",
        "align-items": "center",
        "justify-content": "center",
        "height": "100vh",
    },
)
