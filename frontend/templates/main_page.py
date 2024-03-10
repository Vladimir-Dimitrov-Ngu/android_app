import dash_html_components as html

MAIN_PAGE_FRONT = html.Div(
    children=[
        html.H1(
            "Приложение для обнаружения вирусного ПО на Android",
            className="display-10",
            style={
                "textAlign": "center",
                "minHeight": "70px",
                "marginBottom": 1,
                "marginTop": 20,
            },
        ),
        html.H3(
            "Надежный инструмент для защиты вашего устройства от вредоносных атак",
            style={
                "textAlign": "center",
                "marginBottom": 70,
                "marginTop": 5,
                "fontSize": 20,
            },
        ),
        html.H5(
            "Функции:",
            style={
                "textAlign": "justified",
                "marginBottom": 45,
                "marginTop": 40,
                "fontSize": 23,
            },
        ),
        html.Ul(
            [
                html.P(
                    "Тройная защита. Используются сразу 3 метода машинного обучения для определения вредоносного ПО",
                    style={
                        "textAlign": "center",
                        "marginBottom": 30,
                        "marginTop": 30,
                        "fontSize": 22,
                    },
                ),
                html.P(
                    "Предсказания в реальном времени. В среднем на 1 предсказание уходит меньше минуты",
                    style={
                        "textAlign": "center",
                        "marginBottom": 20,
                        "marginTop": 30,
                        "fontSize": 22,
                    },
                ),
                html.P(
                    "Персонализированный анализ. Для вас мы подберем персонализированные рекомендации",
                    style={
                        "textAlign": "center",
                        "marginBottom": 20,
                        "marginTop": 30,
                        "fontSize": 22,
                    },
                ),
            ],
            style={"listStyleType": "none", "textAlign": "justified"},
        ),
        html.Button(
            "Пополнить счет и начать сканирование",
            id="button_main",
            style={
                "padding": "10px 20px",
                "fontSize": 16,
                "backgroundColor": "#4CAF50",
                "color": "white",
                "border": "none",
                "borderRadius": 5,
                "cursor": "pointer",
                "marginLeft": 430,
                "marginTop": 80,
            },
        ),
        html.Div(id="hidden_div_for_redirect_callback"),
        html.P(
            "Не жертвуйте безопасностью своего устройства – выбирайте наше приложение и будьте уверены в его эффективности!",
            style={"textAlign": "center", "marginTop": 530},
        ),
    ]
)
