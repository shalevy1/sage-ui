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

layout = html.Div([ #opening layout
    header, #page header from header.py
#########PAGE START#########
        html.Div([
        html.Div([
        dcc.Dropdown(id='title_dropdown',
                     multi=True,
                     value=tuple(),
                     options=[{'label': c, 'value': c}
                              for c in sorted(titles)]),
        ], style={'width': '50%', 'margin-left': '25%'}),
        dcc.Graph(id='source_graph',
                  config={'displayModeBar': False}),

                  ], style={'background-color': 'rgb(234, 249, 219)'})


#########PAGE END#########

]) #closing layout

#callbacks

@app.callback(Output('source_graph', 'figure'),
            [Input('title_dropdown', 'value')])
def plot_titles(title_func):
    df1 = df[df['title'].isin(title_func)]
    return {
        'data': [go.Scatter(x=df['title'],
                            y=df['source_count'],
                            mode='markers',
                            showlegend=False,
                            legendgroup='one',
                            name='',
                            hoverinfo='text',
                            text= df['Name'] + ' - ' + df['title'],
                            hoverlabel={'font': {'size': 20}},
                            marker={'color': '#bbbbbb'})] +
                [go.Scatter(x=df1[df1['title']==c]['title'],
                            y=df1[df1['title']==c]['source_count'],
                            #mode='markers',
                            marker={'size': 15},
                            #hovertext={'font': {'size': 30}},
                            hoverlabel={'font': {'size': 15}},
                            name=c)
                     for c in sorted(title_func)],
        'layout': go.Layout(title='Titles by source count: ' + ', '.join(title_func),
                            xaxis={'title': 'Titles', 'zeroline': False,
                                   'showticklabels': False},
                            yaxis={'title': 'Sources #', 'zeroline': False},
                            font={},
                            paper_bgcolor='',
                            plot_bgcolor=''),
        }
