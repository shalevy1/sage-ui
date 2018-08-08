# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from app import app
from header import header

from sqlalchemy import create_engine
import sqlite3
import re

# ProgrammingError: SQLite objects created in a thread
# can only be used in that same thread
# so adding check_same_thread = False
# connect to database
conn = sqlite3.connect('./data/sage.db', check_same_thread = False)

# generating table
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

# create regex function for sqlite
def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

# add our regex function above to sqlite
conn.create_function("REGEXP", 2, regexp)

# create a cursor to use the database
cur = conn.cursor()

# print out the table names in your database
#tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print_tables = print("The table names are {}, {}, {}, and {}".format(*tables.fetchall()))

# Dash App opening layout
layout = html.Div([
    header,
#########PAGE START#########
    html.Div([
        html.H2('SAGE SQL Dash query'),
        html.P('SQL Tables: entities, relationships, sources, reports'),
        dcc.Input(
            id='sql-query',
            value='SELECT * FROM relationships',
            style={'width': '80%'},
            type='text'
        ),
        html.Button('Run Query', id='run-query'),

        html.Hr(),

        html.Div([
            html.H3('SQL Datatable'),
            html.Div(id='table-container', className="ten columns"),

            html.Div([
                html.H3('Datagraph: select dropdowns'),
                html.Div([
                    html.Div([
                        html.Label('Select X'),
                        dcc.Dropdown(
                            id='dropdown-x',
                            clearable=False,
                        )
                    ], className="five columns"),
                    html.Div([
                        html.Label('Select Y'),
                        dcc.Dropdown(
                            id='dropdown-y',
                            clearable=False,
                        )
                    ], className="five columns")
                ], className="row"),
                html.Div(dcc.Graph(id='graph'), className="ten columns")
            ], className="twelve columns")
        ], className="row"),

        # hidden table element
        html.Div(id='table-store', style={'display': 'none'})
        ])

#########PAGE END#########

]) #closing layout

#callbacks
@app.callback(
    dash.dependencies.Output('table-store', 'children'),
    [dash.dependencies.Input('run-query', 'n_clicks')],
    state=[dash.dependencies.State('sql-query', 'value')])
def sql(number_of_times_button_has_been_clicked, sql_query):
    dff = pd.read_sql_query(
        sql_query,
        conn
    )
    return dff.to_json()


@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('table-store', 'children')])
def dff_to_table(dff_json):
    dff = pd.read_json(dff_json)
    return generate_table(dff)


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('table-store', 'children'),
     dash.dependencies.Input('dropdown-x', 'value'),
     dash.dependencies.Input('dropdown-y', 'value')])
def dff_to_table(dff_json, dropdown_x, dropdown_y):
    dff = pd.read_json(dff_json)
    return {
        'data': [{
            'x': dff[dropdown_x],
            'y': dff[dropdown_y],
            'type': 'bar'
        }],
        'layout': {
            'margin': {
                'l': 20,
                'r': 10,
                'b': 60,
                't': 10
            }
        }
    }


@app.callback(
    dash.dependencies.Output('dropdown-x', 'options'),
    [dash.dependencies.Input('table-store', 'children')])
def create_options_x(dff_json):
    dff = pd.read_json(dff_json)
    return [{'label': i, 'value': i} for i in dff.columns]


@app.callback(
    dash.dependencies.Output('dropdown-y', 'options'),
    [dash.dependencies.Input('table-store', 'children')])
def create_options_y(dff_json):
    dff = pd.read_json(dff_json)
    return [{'label': i, 'value': i} for i in dff.columns]
