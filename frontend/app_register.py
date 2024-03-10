import dash
import dash_bootstrap_components as dbc

from frontend.callback import ARGUMENTS_FOR_AUTHENTICATE, authenticate
from frontend.templates import layout_for_register

app_dash = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])


app_dash.layout = layout_for_register

app_dash.callback(*ARGUMENTS_FOR_AUTHENTICATE)(authenticate)

if __name__ == "__main__":
    app_dash.run_server(debug=True)
