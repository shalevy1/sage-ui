import dash
import os
from flask import send_from_directory

import flask
# Defining the dash/flask app/server
server = flask.Flask(__name__)
app = dash.Dash(sharing=True, server=server, static_folder='static')
# app = dash.Dash()
# server = app.server
app.config.suppress_callback_exceptions = True

app.css.config.serve_locally = False
#adding remote and local css
external_css = [
    #'https://codepen.io/amyoshino/pen/jzXypZ.css',
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css',
    '/static/base.css',
    '/static/custom.css'
]
for css in external_css:
    app.css.append_css({"external_url": css})

# @app.server.route('/static/<path:path>')
# def static_file(path):
#     static_folder = os.path.join(os.getcwd(), 'static')
#     return send_from_directory(static_folder, path)

@server.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(os.path.join(root_dir, 'static'), path)
