import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from backend.database.models import Money as MoneyDB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.config import DB_PATH
import requests


engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)
session = Session()
# n_clicks = MoneyDB.get_money_by_username(session, 'admin') // 100

data = {"username": "admin", "password": "god"}


url = "http://127.0.0.1:9002/api/money"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
try:
    response = requests.get(url, headers=headers, json=data)
    result_data = response.json()
    initial_counter_value = result_data.get("money", 0)
    n_clicks = initial_counter_value // 100
except:
    n_clicks = MoneyDB.get_money_by_username(session, "admin") // 100

BANK_FRONT = html.Div(
    [
        html.H1("Баланс", style={"font-size": 40, "marginBottom": 30}),
        html.P(
            "Здесь вы можете пополнить свой счет",
            style={"font-size": 20, "marginBottom": 30},
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button(
                        [html.I(className="fas fa-plus"), " Пополнить"],
                        id="button_bank",
                        color="success",
                        className="mr-3",
                        n_clicks=None,
                    ),
                    width="auto",
                ),
                dbc.Col(
                    html.H3(id="counter_bank", children=0),
                    width="auto",
                    style={"marginTop": 10, "marginLeft": 25},
                ),
            ],
            className="mt-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="/assets/payment.png",
                        height="150px",
                        style={
                            "position": "absolute",
                            "bottom": "0",
                            "marginLeft": 350,
                        },
                    ),
                    width=4,
                )
            ]
        ),
        dcc.Interval(id="interval-component", interval=500, n_intervals=0),
    ],
)
