## IMPORTS #######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import State, Input, Output

import xlwings as xw


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



# a = str(wb.sheets['Sheet1'].range('a1').value)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Button(id='update-button', n_clicks=0, children='update'),

    html.Div(id = 'output_1')

])

@app.callback(
    Output(component_id='output_1', component_property='children'),
    [Input('update-button', 'n_clicks')],
)
def update_xl_values_f(n_clicks):
    if(n_clicks > 0):   
        return(n_clicks)
    else:
        return()
 

if __name__ == '__main__':
    app.run_server(debug=False)

)

if __name__ == '__main__':
    app.run_server()
