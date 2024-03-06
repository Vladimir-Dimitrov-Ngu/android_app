import json
import time

import dash
import requests
from dash import Input, Output, dcc, html
from dash.exceptions import PreventUpdate

from frontend.config import URL_FOR_BANK, URL_FOR_PREDICT
from frontend.controllers import find_latest_file, save_file, uploaded_files
from frontend.templates import (BANK_FRONT, HELP_FRONT, MAIN_PAGE_FRONT,
                                PREDICT_FRONT)

from backend.database.models import Money as MoneyDB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.config import DB_PATH


engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)
session = Session()

ARGUMENTS_FOR_RENDER = [Output("page-content", "children"), Input("url", "pathname")]
ARGUMENTS_FOR_UPDATE_BALANCE = [Output("counter_bank", "children"), Input("button_bank", "n_clicks")]
ARGUMENTS_FOR_BANK_BUTTON_MAIN_MENU = [Output("hidden_div_for_redirect_callback", "children"), Input("button_main", "n_clicks")]
ARGUMENTS_FOR_UPDATE_SEARCH_RESULT = [Output("search-output", "children"), Input("search-input", "value")]
ARGUMENTS_FOR_UPDATE_MODEL = [Output("output-div", "children"), Input("my-dropdown", "value")]
ARGUMENTS_FOR_UPDATE_PREDICT = [Output("predict_h2", "children"), Output("upload-data", "children"),
    Input("upload-data", "filename"), Input("upload-data", "contents")]
ARGUMENTS_FOR_GET_PREDICT = [Output("file-list", "children"), Output("predict", "style"),
                             Input("predict", "n_clicks")]
ARGUMENTS_FOR_CHANGE_COLOR_BUTTON = [Output("predict", "style", allow_duplicate=True), 
                                     Input("predict", "n_clicks")]
ARGUMENTS_FOR_UPDATE_BUTTON_BALANCE =[Output("counter_bank", "children"),
    Output("button_bank", "n_clicks", allow_duplicate=True),
    Input("button_bank", "n_clicks"),]

def test(n_intervals):
    try: n_clicks = MoneyDB.get_money_by_username(session=session, username='admin') // 100
    except: 
        return 0
    return n_clicks

MODEL = None

def render_page_content(pathname):
    if pathname == "/":
        return MAIN_PAGE_FRONT
    elif pathname == "/page-1":
        return PREDICT_FRONT
    elif pathname == "/page-2":
        return BANK_FRONT
    elif pathname == "/page-3":
        return HELP_FRONT
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


def update_counter_balance(n_clicks):
    if n_clicks is None:
        counter_value = MoneyDB.get_money_by_username(session=session, username='admin')
    else:
        counter_value = MoneyDB.get_money_by_username(session=session, username='admin')
        counter_value += 100
        MoneyDB.add_money_by_username(session=session, username='admin')
    return counter_value



def bank_button_main_page(n_clicks):
    if n_clicks is not None and n_clicks > 0:
        return dcc.Location(
            href=URL_FOR_BANK, id="someid_doesnt_matter"
        )
    else:
        return dash.no_update
    
def update_search_results(search_query):
    if search_query is None or search_query == "":
        return "Введите запрос для поиска"
    else:
        return f"Пока что не реализован функционал поиска, просим прощения"
    

def update_model(selected_value):
    global MODEL
    MODEL = selected_value
    return

def update_predict_callback(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()
    if len(files) != 0:
        return [
            html.Button(
                "Predict",
                id="predict",
                n_clicks=0,
                style={
                    "background-color": "#4CAF50",
                    "color": "white",
                    "padding": "6px 17px",
                    "border": "none",
                    "border-radius": "4px",
                    "cursor": "pointer",
                    "marginTop": 20,
                },
            )
        ], [html.P(f"Вы загрузили файл {name}")]
    else:
        dash.no_update, dash.no_update

def get_predict(n_clicks):
    MONEY = MoneyDB.get_money_by_username(session=session, username='admin')
    if n_clicks >= 1:
        print('\n\n')
        print(MODEL), print(MONEY)
        print('\n\n')
        if (MODEL=='lr' and MONEY < 100) or (MODEL=='dt' and MONEY < 200) or (MODEL=='ct' and MONEY < 300):
            return html.P(
            "У вас недостаточно средств, пополните счет",
            style={"marginTop": 35, "marginLeft": -30, "fontSize": 25},
        ), {
            "background-color": "#4CAF50",
            "color": "white",
            "padding": "6px 17px",
            "border": "none",
            "border-radius": "4px",
            "cursor": "pointer",
            "marginTop": 20,
        }
        main_path = "/Users/vladimirdimitrov/My_dev/app_uploaded_files"
        csv_file_path = find_latest_file(main_path)
        with open(csv_file_path, 'rb') as file:
            files = {'file': ('file.csv', file, 'text/csv')}
            response = requests.post(URL_FOR_PREDICT, files=files, params={'model_name': MODEL})
        if MODEL == 'lr':
            MoneyDB.add_money_by_username(session=session, username='admin', amount=-100)
        elif MODEL == 'dt':
            MoneyDB.add_money_by_username(session=session, username='admin', amount=-200)
        else:
            MoneyDB.add_money_by_username(session=session, username='admin', amount=-300)
        metrics = json.loads(response.text)
        accuracy = round(metrics['accuracy'], 2)
        time.sleep(1)
        return html.P(
            "Ваша точность: " + str(accuracy),
            style={"marginTop": 35, "marginLeft": -30, "fontSize": 25},
        ), {
            "background-color": "#4CAF50",
            "color": "white",
            "padding": "6px 17px",
            "border": "none",
            "border-radius": "4px",
            "cursor": "pointer",
            "marginTop": 20,
        }
    else:
        dash.no_update, dash.no_update

def flash_predict_button(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    if n_clicks > 0:
        return {
            "background-color": "red",
            "color": "white",
            "padding": "6px 17px",
            "border": "none",
            "border-radius": "4px",
            "cursor": "pointer",
            "marginTop": 20,
        }
    else:
        dash.no_update