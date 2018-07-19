# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly
#from plotly import graph_objs as go
from plotly.graph_objs import *
import plotly.graph_objs as go
from flask import Flask
import pandas as pd
import numpy as np
import os
import copy
import json
import io
import urllib

from app import app

# Launch the application:
#app = dash.Dash()

file = os.path.abspath("./data/title.csv")
df = pd.read_csv(file, index_col=0)

# Boostrap CSS.
#app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})  # noqa: E501

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
layout = html.Div([
    html.Div(className='row',
             style={'backgroundColor': 'rgb(234, 249, 219)',
                    'color':'white', 'padding': 25},
             children=[html.Div(className='nine columns',
                                children=[
                                    html.H1("Sage - entities and titles",
                                            style={'paddingBottom':0, 'font-weight':'bold'}),
                                    html.H6("Exploration of names and sources using Plotly Dash",
                                            style={'paddingTop':0, 'paddingBottom':0, 'font-size':'100%'}),
                                    # html.P(children=[html.A('GitHub',
                                    #                          href='https://github.com/DistrictDataLabs/sage',
                                    #                          style={'color': 'black', 'textAlign': 'right'})])
                                ]),
                        html.Div(className='three columns',
                                 style={'float': 'right', 'paddingLeft': 20, 'padding-top': 20},
                                 children=[
                                    html.Img(src='https://static1.squarespace.com/static/55fdfa38e4b07a55be8680a4/t/55ff389ae4b0af0b2a73db12/1531951609241/?format=1500w',
                                             style={'maxWidth':'100%'}),
                        ])
    ]),
        html.Div([
            html.P('switch between apps',
                style={'position': 'absolute',
                        'background-color': '#f9f9f9c7',
                        'align-items': 'center',
                        'width': '100%',
                        'display': 'flex',
                        'justify-content': 'center',
                        })],className='container'),

        #links to apps
        html.Div([
        html.Div([dcc.Link('Scatter', href='/apps/app1')],className='three columns'),
        html.Div([dcc.Link('Network Viz', href='/apps/app2')],className='three columns'),
        html.Div([dcc.Link('Sage Table', href='/apps/sage_table')],className='three columns'),
        html.Div([dcc.Link('Sage Home', href='/')],className='three columns')
        ],className='container',style={'padding': 25, 'color':'#39536B'}),
#########PAGE#########
    # html.Div(
    #     [
    #         html.H1(
    #             'Sage in Dash',
    #             style={'font-family': 'Helvetica',
    #                    "margin-top": "25",
    #                    "margin-bottom": "0"},
    #             className='eight columns',
    #         ),
    #         html.P(
    #             'exploration of Sage in Dash',
    #             style={'font-family': 'Helvetica',
    #                    "font-size": "120%",
    #                    "width": "80%"},
    #             className='eight columns',
    #         ),
    #     ],
    #     className='row'
    # ),

html.Div(
    [
        html.Div(
            [
                dcc.Graph(id='pie-graph',
                        #  style={'margin-top': '20'},
                          figure={'data':[
                          go.Pie(
                          values=df['source_count'],
                          labels=df['title']
                          )],
                          'layout':go.Layout(
                          title='by %',
                          legend=dict(x=-.5, y=1.2)
                          )})
            ], className = "six columns"
        ),
        html.Div(
            [
                dt.DataTable(
                    rows=df.to_dict('records'),
                    columns=df.columns,
                    row_selectable=True,
                    filterable=True,
                    sortable=True,
                    selected_row_indices=[],
                    id='datatable'),

                html.A(
                    'Download Selected Data',
                    id='download-link',
                    download="sage_selected_data.csv",
                    href="",
                    target="_blank"
                ),
            ],
            #style=layout_right,
            className="six columns"
        ),

        html.Div(
            [
                dcc.Graph(id="histogram")
            ],className="twelve columns")
    ], className="row"
)
], #style={'background-color': '#fffff'}
#className='ten columns offset-by-one'
)

#filter data
def filter_data(selected_row_indices):
        dff = df.iloc[selected_row_indices]
        return dff
#callback to download data
@app.callback(
    Output('download-link', 'href'),
    [Input('datatable', 'selected_row_indices')])
def update_download_link(selected_row_indices):
    dff = filter_data(selected_row_indices)
    csv_string = dff.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string

@app.callback(
    Output('datatable', 'selected_row_indices'),
    [Input('histogram', 'selectedData')],
    [State('datatable', 'selected_row_indices')])
def update_selected_row_indices(selectedData, selected_row_indices):
    if selectedData:
        selected_row_indices = []
        for point in selectedData['points']:
            selected_row_indices.append(point['pointNumber'])
    return selected_row_indices

@app.callback(
    Output('histogram', 'figure'),
    [Input('datatable', 'rows'),
     Input('datatable', 'selected_row_indices')])
def update_figure(rows, selected_row_indices):
    dff = pd.DataFrame(rows)
    marker = {'color': ['#0074D9']*len(dff)}
    for i in (selected_row_indices or []):
        marker['color'][i] = '#1aff50'
    layout = go.Layout(
        bargap=0.05,
        bargroupgap=0,
        barmode='group',
        margin=Margin(l=50, r=10, t=50, b=100),
        showlegend=False,
        height=250,
        dragmode="select",
        xaxis=dict(
            showgrid=False,
            nticks=50,
            fixedrange=False
        ),
        yaxis=dict(
            showticklabels=True,
            showgrid=False,
            fixedrange=False,
            rangemode='nonnegative',
            zeroline=False
        )
    )

    data = Data([
         go.Bar(
             x=dff['Name'],
             y=dff['source_count'],
             marker = marker,
             hoverinfo=dff['title']
         )
     ])

    return go.Figure(data=data, layout=layout)
