# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import os

from app import app
from header import header

file = os.path.abspath("./data/title.csv")
df = pd.read_csv(file, index_col=0)
names = pd.unique(df['Name'])
titles = pd.unique(df['title'])
sources = pd.unique(df['source_count'])

layout = html.Div([
    header,
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
