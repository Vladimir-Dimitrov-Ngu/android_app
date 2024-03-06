import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from frontend.config import URL_FOR_AUTHENTICATE_TRUE
from frontend.controllers import mylogin

ARGUMENTS_FOR_AUTHENTICATE = [
    Output("hidden_div_for_redirect_callback", "children"),
    Input('login-button', 'n_clicks'),
    State('username', 'value'),
    State('password', 'value')
]


def authenticate(n_clicks, username, password, id=None):
    if n_clicks > 0:
        check, response = mylogin(username, password)
        if check:
            return dcc.Location(href=URL_FOR_AUTHENTICATE_TRUE, 
                                id="someid_doesnt_matter")
        

