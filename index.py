# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table_experiments as dt
import visdcc
from app import app
#from cypher import title
from apps import app1, app2
from apps import sage_table


app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    # content will be rendered in this element
    html.Div(id='page-content'),
    # workaround to render table component in sage_table app
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'}),
    html.Div(visdcc.Network(id='net', data={'nodes':[],'edges':[]}))
])
#main page
index_page = html.Div([
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
    html.Div([html.A('GitHub', href='https://github.com/DistrictDataLabs/sage', target='_blank')],className='three columns')
    ],className='container',style={'padding': 25, 'color':'#39536B'}),
#########PAGE#########


    #markdown text
    html.Div([
    dcc.Markdown('''
        ***
        # Introduction to Sage
        ***
        `sage` uses [several named entity extraction](https://en.wikipedia.org/wiki/Named-entity_recognition)
        libraries to extract over **15 classes of entities** from text. As a follow on task, `sage` leverages \
        [set math operations](https://www.probabilitycourse.com/chapter1/1_2_2_set_operations.php) to assign \
        confidence measures to named entitiy extractions, which produces a *linked data repository that can be \
        filtered/analyzed* using various measures of reliability.
        ***
    '''.replace('  ', '')),
    #image
    html.Img(
        src='https://camo.githubusercontent.com/d1d9fdfda4cfa0ab9107c09677727e0aa81f8d25/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f332f33612f477261706844617461626173655f50726f706572747947726170682e706e67',
        alt='Nodes Example',
        style={}),
    dcc.Markdown('''
        ***
        # Setting up the Knowledge Builder Environment
        ***
        This notebook is a walkthrough of the dependencies needed
        to run the knowledge builder code.  I recommend using Anaconda
        to manage your Python environment as it makes things easier.
        There are automated scripts in the zipped file for this project
        that should install most dependencies and mirror the file
        structure to support all imports. Here is a visualization of the
        directory and included files.
        File structure:
        ***
        ```
        knowledge_sample/
        │   README.md
        │   builderprep.py
        │   entityextractors.py
        │   knowledge.py
        │   kbp_mapping.json
        │   environment.yml
        │    kbtest.py
        │
        │
        └─── corenlp_setup/
        │   │   sample-server.properties
        │
        │
        └─── images/
        │   │   coreNLP.png
        │   │   corenlp_models.png
        │   │   sampleOutput_noweighting.png
        │
        │
        └─── scripts/
        │   │   polyglot_install.sh
        │   │   nlpModelDownloads.sh
        │
        │
        └─── data/
        │   │   ensembleSourceData_file1_new.parquet
        │   │   ensembleSourceData_file2_new.parquet
        │
        │
        ```

    '''.replace('  ', ''))
    ],className='container'),

])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return index_page
    if pathname == '/apps/app1':
         return app1.layout
    elif pathname == '/apps/app2':
         return app2.layout
    elif pathname == '/apps/sage_table':
         return sage_table.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
