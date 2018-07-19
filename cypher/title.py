import py2neo
from py2neo import Graph
import pandas as pd
import os


graph = py2neo.Graph(user='neo4j',password='Neo4j')

#Return Nodes that are Persons with a Title and that Title has at least 1 source
query= """MATCH (n:Person)-[r:title]-(p)
        WHERE SIZE(r.sources)>3
        RETURN n.name as Name,p.name as title, r.sources as sources"""
#df = pd.DataFrame(graph.data(query))
#df = pd.DataFrame(cyPandas(query, graph=graph))
result = graph.run(query).data()
df = pd.DataFrame(result)
# count the number of non-repeating values
df = df.assign(sources=df.sources.apply(lambda x: list(set(x))))
#stripping sources column from brackets and convert to list
sources = pd.DataFrame(df.sources.tolist(), )
#convert source # to 1, nan to 0
sources = sources.notnull().astype('int')
# sum columns
sources['source_count'] = sources.select_dtypes(int).sum(1)
sources_sum = sources[['source_count']]
# combine df with sources_sum
df = df.drop('sources',axis=1)
df1 = pd.concat([df, sources_sum], axis=1)
df1.drop_duplicates(keep=False, inplace=True)
# save to file
file = os.path.abspath("./data/title.csv")
df1.to_csv(file)
