import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event, State

import visdcc

from app import app


layout = html.Div([
    html.Div(className='row',
             style={'backgroundColor': 'rgb(234, 249, 219)',
                    'color':'white', 'padding': 25},
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
        html.Div([dcc.Link('Scatter', href='/apps/app1')],className='three columns'),
        html.Div([dcc.Link('Network Viz', href='/apps/app2')],className='three columns'),
        html.Div([dcc.Link('Sage Table', href='/apps/sage_table')],className='three columns'),
        html.Div([dcc.Link('Sage Home', href='/')],className='three columns')
        ],className='container',style={'padding': 25, 'color':'#39536B'}),
#########PAGE#########

    html.H1('Network Viz'),

    html.Div([
            visdcc.Network(id='net',
                     data={'nodes':[{'id': 23, 'label': 'Russia', 'title': 'Class:Country<br>Name:Russia<br>Confidence:high', 'group': 'Country', 'color':'#00ffff'},
                    {'id': 24, 'label': 'Ukraine', 'title': 'Class:Country<br>Name:Ukraine<br>Confidence:high', 'group': 'Country'},
                    {'id': 32, 'label': 'U.S.', 'title': 'Class:Country<br>Name:U.S.<br>Confidence:medium', 'group': 'Country'},
                    {'id': 51, 'label': 'Russian', 'title': 'Class:Country<br>Name:Russian<br>Confidence:low', 'group': 'Country'},
                    {'id': 52, 'label': 'British', 'title': 'Class:Country<br>Name:British<br>Confidence:low', 'group': 'Country'},
                    {'id': 33, 'label': 'British', 'title': 'Class:Nationality<br>Name:British<br>Confidence:medium', 'group': 'Nationality'},
                    {'id': 34, 'label': 'Russian', 'title': 'Class:Nationality<br>Name:Russian<br>Confidence:medium', 'group': 'Nationality'},
                    {'id': 35, 'label': 'Ukrainian', 'title': 'Class:Nationality<br>Name:Ukrainian<br>Confidence:medium', 'group': 'Nationality'},
                    {'id': 25, 'label': 'Washington', 'title': 'Class:StatesOrProvinces<br>Name:Washington<br>Confidence:high', 'group': 'StatesOrProvinces'},
                    {'id': 40, 'label': 'consultant', 'title': 'Class:Title<br>Name:consultant<br>Confidence:low', 'group': 'Title'},
                    {'id': 41, 'label': 'candidate', 'title': 'Class:Title<br>Name:candidate<br>Confidence:low', 'group': 'Title'},
                    {'id': 42, 'label': 'actress', 'title': 'Class:Title<br>Name:actress<br>Confidence:low', 'group': 'Title'},
                    {'id': 43, 'label': 'lawmaker', 'title': 'Class:Title<br>Name:lawmaker<br>Confidence:low', 'group': 'Title'},
                    {'id': 44, 'label': 'president', 'title': 'Class:Title<br>Name:president<br>Confidence:low', 'group': 'Title'},
                    {'id': 45, 'label': 'businessman', 'title': 'Class:Title<br>Name:businessman<br>Confidence:low', 'group': 'Title'},
                    {'id': 46, 'label': 'attorney', 'title': 'Class:Title<br>Name:attorney<br>Confidence:low', 'group': 'Title'},
                    {'id': 47, 'label': 'spokesman', 'title': 'Class:Title<br>Name:spokesman<br>Confidence:low', 'group': 'Title'},
                    {'id': 48, 'label': 'security adviser', 'title': 'Class:Title<br>Name:security adviser<br>Confidence:low', 'group': 'Title'},
                    {'id': 49, 'label': 'chairman', 'title': 'Class:Title<br>Name:chairman<br>Confidence:low', 'group': 'Title'},
                    {'id': 50, 'label': 'intelligence officer', 'title': 'Class:Title<br>Name:intelligence officer<br>Confidence:low', 'group': 'Title'},
                    {'id': 37, 'label': 'Trump', 'title': 'Class:Facility<br>Name:Trump<br>Confidence:low', 'group': 'Facility'},
                    {'id': 38, 'label': 'Trump Organization', 'title': 'Class:Facility<br>Name:Trump Organization<br>Confidence:low', 'group': 'Facility'},
                    {'id': 2, 'label': 'Christopher Steele', 'title': 'Class:Person<br>Name:Christopher Steele<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 3, 'label': 'Cohen', 'title': 'Class:Person<br>Name:Cohen<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 4, 'label': 'Flynn', 'title': 'Class:Person<br>Name:Flynn<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 5, 'label': 'Michael Cohen', 'title': 'Class:Person<br>Name:Michael Cohen<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 6, 'label': 'Michael Flynn', 'title': 'Class:Person<br>Name:Michael Flynn<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 7, 'label': 'Mueller', 'title': 'Class:Person<br>Name:Mueller<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 8, 'label': 'Paul Manafort', 'title': 'Class:Person<br>Name:Paul Manafort<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 9, 'label': 'Stormy Daniels', 'title': 'Class:Person<br>Name:Stormy Daniels<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 10, 'label': 'Trump', 'title': 'Class:Person<br>Name:Trump<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 11, 'label': 'Vladimir Putin', 'title': 'Class:Person<br>Name:Vladimir Putin<br>Confidence:very_high', 'group': 'Person'},
                    {'id': 15, 'label': 'Manafort', 'title': 'Class:Person<br>Name:Manafort<br>Confidence:high', 'group': 'Person'},
                    {'id': 16, 'label': 'Daniels', 'title': 'Class:Person<br>Name:Daniels<br>Confidence:high', 'group': 'Person'},
                    {'id': 17, 'label': 'Michael', 'title': 'Class:Person<br>Name:Michael<br>Confidence:high', 'group': 'Person'},
                    {'id': 18, 'label': 'Robert S. Mueller III', 'title': 'Class:Person<br>Name:Robert S. Mueller III<br>Confidence:high', 'group': 'Person'},
                    {'id': 26, 'label': 'Andrew Harnik/AP', 'title': 'Class:Person<br>Name:Andrew Harnik/AP<br>Confidence:medium', 'group': 'Person'},
                    {'id': 27, 'label': 'Democrat', 'title': 'Class:Person<br>Name:Democrat<br>Confidence:medium', 'group': 'Person'},
                    {'id': 28, 'label': 'Steele', 'title': 'Class:Person<br>Name:Steele<br>Confidence:medium', 'group': 'Person'},
                    {'id': 36, 'label': '130,000', 'title': 'Class:Money<br>Name:130,000<br>Confidence:medium', 'group': 'Money'},
                    {'id': 39, 'label': '$130,000', 'title': 'Class:Money<br>Name:$130,000<br>Confidence:low', 'group': 'Money'},
                    {'id': 12, 'label': 'BBC', 'title': 'Class:Organization<br>Name:BBC<br>Confidence:very_high', 'group': 'Organization'},
                    {'id': 13, 'label': 'Trump', 'title': 'Class:Organization<br>Name:Trump<br>Confidence:very_high', 'group': 'Organization'},
                    {'id': 14, 'label': 'Trump Organization', 'title': 'Class:Organization<br>Name:Trump Organization<br>Confidence:very_high', 'group': 'Organization'},
                    {'id': 19, 'label': 'New York Times', 'title': 'Class:Organization<br>Name:New York Times<br>Confidence:high', 'group': 'Organization'},
                    {'id': 29, 'label': 'Democrat', 'title': 'Class:Organization<br>Name:Democrat<br>Confidence:medium', 'group': 'Organization'},
                    {'id': 30, 'label': 'Senate Intelligence Committee', 'title': 'Class:Organization<br>Name:Senate Intelligence Committee<br>Confidence:medium', 'group': 'Organization'},
                    {'id': 20, 'label': 'Manhattan', 'title': 'Class:City<br>Name:Manhattan<br>Confidence:high', 'group': 'City'},
                    {'id': 21, 'label': 'Prague', 'title': 'Class:City<br>Name:Prague<br>Confidence:high', 'group': 'City'},
                    {'id': 22, 'label': 'Moscow', 'title': 'Class:City<br>Name:Moscow<br>Confidence:high', 'group': 'City'},
                    {'id': 31, 'label': 'New York City', 'title': 'Class:City<br>Name:New York City<br>Confidence:medium', 'group': 'City'},
                    {'id': 1, 'label': 'Article:Why Michael Cohen is poss', 'title': 'Class:Reports<br>Title:Why Michael Cohen is possibly the biggest threat to Trump', 'group': 'Reports'},
                    {'id': 0, 'label': 'Provider:washingtonpost', 'title': 'Class:Sources<br>Source:washingtonpost', 'group': 'Sources'}],
                             'edges':[{'from': 0, 'to': 1, 'title': 'created'},
                                    {'from': 10, 'to': 44, 'title': 'title'},
                                    {'from': 5, 'to': 46, 'title': 'title'},
                                    {'from': 10, 'to': 13, 'title': 'employee_or_member_of'},
                                    {'from': 5, 'to': 13, 'title': 'employee_or_member_of'},
                                    {'from': 11, 'to': 34, 'title': 'origin'},
                                    {'from': 11, 'to': 51, 'title': 'origin'},
                                    {'from': 11, 'to': 44, 'title': 'title'},
                                    {'from': 9, 'to': 42, 'title': 'title'},
                                    {'from': 5, 'to': 42, 'title': 'title'},
                                    {'from': 2, 'to': 33, 'title': 'origin'},
                                    {'from': 2, 'to': 52, 'title': 'origin'},
                                    {'from': 2, 'to': 50, 'title': 'title'},
                                    {'from': 6, 'to': 48, 'title': 'title'},
                                    {'from': 5, 'to': 44, 'title': 'title'},
                                    {'from': 5, 'to': 31, 'title': 'cities_of_residence'},
                                    {'from': 5, 'to': 32, 'title': 'countries_of_residence'},
                                    {'from': 3, 'to': 32, 'title': 'countries_of_residence'},
                                    {'from': 5, 'to': 45, 'title': 'title'},
                                    {'from': 8, 'to': 49, 'title': 'title'},
                                    {'from': 5, 'to': 49, 'title': 'title'},
                                    {'from': 5, 'to': 41, 'title': 'title'}]
                     },
                     options=dict(height='600px', width='100%')),
]),

]) #closing layout
