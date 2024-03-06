import dash_core_components as dcc
import dash_html_components as html

HELP_FRONT = html.Div([
    html.H1("Помощь", style={'textAlign': 'center', 'marginBottom': 20, 'marginTop': 10}),
    html.Div([
        html.P('🔍', style={'font-size': '35px', 'margin-right': '20px'}),
        dcc.Input(id='search-input', type='text', placeholder='Введите запрос', style={'width': '50%'}),
    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div(id='search-output', style={'margin-top': '20px', 'text-align': 'center'}),
])