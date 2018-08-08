from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app
from header import header

layout = html.Div([
        header,
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
                ],className='container')

])
