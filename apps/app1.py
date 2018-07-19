# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import os

from app import app

file = os.path.abspath("./data/title.csv")
df = pd.read_csv(file, index_col=0)
names = pd.unique(df['Name'])
titles = pd.unique(df['title'])
sources = pd.unique(df['source_count'])

layout = html.Div([
    html.Div(className='row',
             style={'backgroundColor': 'rgb(234, 249, 219)',
                    'color':'white', 'padding': 25},
             children=[html.Div(className='nine columns',
                                children=[
                                    html.H1("Sage - scatter for entities and titles",
                                            style={'paddingBottom':0, 'font-weight':'bold'}),
                                    html.H6("scatter for entities and titles by sources count",
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
#########PAGE START#########
    html.Div([
        dcc.Graph(
            id='scatter',
            figure={
                'data': [go.Scatter(
                    x = df['title'],
                    y = df['source_count'],
                    text = df['Name'] + ' - ' + df['title'],
                    hoverinfo = 'text',
                    mode = 'markers',
                    marker=dict(size=1.5*df['source_count'])
                )],
                'layout': go.Layout(
                    title = 'Titles by Sources Count',
                    xaxis = {},
                    yaxis = {'title': 'sources #'},
                    hovermode='closest'
                )
            }
        )


    ])
#########PAGE END#########

]) #closing layout

#callbacks
