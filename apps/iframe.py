import os
import dash
import flask
from flask import request, Flask, send_from_directory
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from dash.dependencies import Input, Output, State, Event

# Defining the dash/flask app/server
server = flask.Flask(__name__)
app = dash.Dash(sharing=True, server=server, static_folder='static')


@server.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(os.path.join(root_dir, 'static'), path)

def serve_layout():
    return html.Div([
        html.Iframe(src='static/networkviz.html',
                    style={'width':'800px',
                           'height':'600px',
                           'margin':'auto',
                           'display':'block'},
                    id='networkviz'),
        ])

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)
