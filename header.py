from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

header = html.Div([
            html.Div(className='row',
                     style={'backgroundColor': 'rgb(234, 249, 219)',
                            'color':'white', 'padding': 20},
                     children=[html.Div(className='nine columns',
                                        children=[
                                            html.H1("Sage",
                                                    style={'paddingBottom':0, 'font-weight':'bold'}),
                                            html.H6("is a Python library that extracts structured data from text and stores it as linked data in a graph database",
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
    html.Div([dcc.Link('Scatter', href='/apps/app1')],className='two columns'),
    html.Div([dcc.Link('Network Viz', href='/apps/app2')],className='two columns'),
    html.Div([dcc.Link('SQL', href='/apps/sql')],className='two columns'),
    html.Div([dcc.Link('Sage Table', href='/apps/sage_table')],className='two columns'),
    #html.Div([html.A('GitHub', href='https://github.com/DistrictDataLabs/sage', target='_blank')],className='three columns')
    ],className='container',style={'padding': 25, 'color':'#39536B'})
])
