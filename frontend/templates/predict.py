import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

PREDICT_FRONT = dbc.Container(
    fluid=True,
    children=[
        html.H1(
            "Предсказания",
            className="display-10",
            style={
                "textAlign": "center",
                "minHeight": "70px",
                "marginBottom": 20,
                "marginTop": 20,
            },
        ),
        html.H2("Выбор модели", style={"marginBottom": 10, "marginTop": 40}),
        dcc.Dropdown(
            id="my-dropdown",
            options=[
                {"label": "Логистическая регрессия [100]", "value": "lr"},
                {"label": "Дерево решений [200]", "value": "dt"},
                {"label": "Катбуст [300]", "value": "ct"},
            ],
            value="lr",
            style={"marginBottom": 20, "marginTop": 40},
        ),
        html.Div(id="output-div"),
        html.H2(
            "Добавить файл", id="upload", style={"marginBottom": 20, "marginTop": 40}
        ),
        dcc.Upload(
            id="upload-data",
            children=html.Div(["Перетащите файл сюда или нажмите, чтобы выбрать."]),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "marginBottom": "20px",
            },
            multiple=True,
        ),
        html.H2(id="predict_h2", style={"marginBottom": 10}),
        html.Ul(id="file-list"),
    ],
)
