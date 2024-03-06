import dash
import dash_bootstrap_components as dbc

from frontend.callback import (ARGUMENTS_FOR_BANK_BUTTON_MAIN_MENU,
                               ARGUMENTS_FOR_CHANGE_COLOR_BUTTON,
                               ARGUMENTS_FOR_GET_PREDICT, ARGUMENTS_FOR_RENDER,
                               ARGUMENTS_FOR_UPDATE_BALANCE,
                               ARGUMENTS_FOR_UPDATE_MODEL,
                               ARGUMENTS_FOR_UPDATE_PREDICT,
                               ARGUMENTS_FOR_UPDATE_SEARCH_RESULT,
                               ARGUMENTS_FOR_UPDATE_BUTTON_BALANCE,
                               bank_button_main_page, flash_predict_button,
                               test,

                               get_predict, render_page_content,
                               update_counter_balance, update_model,
                               update_predict_callback, update_search_results)
from frontend.config import UPLOAD_DIRECTORY
from frontend.controllers import create_dir
from frontend.templates import LAYOUT_SIDEBAR

create_dir(UPLOAD_DIRECTORY)

app_dash = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app_dash.layout = LAYOUT_SIDEBAR
app_dash.callback(*ARGUMENTS_FOR_RENDER)(render_page_content)
app_dash.callback(*ARGUMENTS_FOR_UPDATE_BALANCE)(update_counter_balance)
app_dash.callback(*ARGUMENTS_FOR_BANK_BUTTON_MAIN_MENU)(bank_button_main_page)
app_dash.callback(*ARGUMENTS_FOR_UPDATE_SEARCH_RESULT)(update_search_results)
app_dash.callback(*ARGUMENTS_FOR_UPDATE_MODEL)(update_model)
app_dash.callback(*ARGUMENTS_FOR_UPDATE_PREDICT)(update_predict_callback)
app_dash.callback(*ARGUMENTS_FOR_GET_PREDICT)(get_predict)
app_dash.callback(*ARGUMENTS_FOR_CHANGE_COLOR_BUTTON, prevent_initial_call=True)(flash_predict_button)

if __name__ == '__main__':
    app_dash.run_server(debug=True, port=8080)