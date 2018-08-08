# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table_experiments as dt
import visdcc
from app import app
from apps import app1, app2, sql, sage_table
from index import layout

# uncomment to run cypher query directly from Neo4j
# Neo4j should be running
#from cypher import title

app.title = 'SAGE'
app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    # content will be rendered in this element
    html.Div(id='page-content'),
    # workaround to render table component in sage_table app
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'}),
    # workaround to render network viz component in app
    html.Div(visdcc.Network(id='net', data={'nodes':[],'edges':[]}))
])
index_page = layout

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return index_page
    if pathname == '/apps/app1':
         return app1.layout
    elif pathname == '/apps/app2':
         return app2.layout
    elif pathname == '/apps/sql':
         return sql.layout
    elif pathname == '/apps/sage_table':
         return sage_table.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
