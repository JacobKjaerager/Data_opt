# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:12:58 2020

@author: Jacob Kjærager

This project seeks to implement functionality for the course E20 Optimization and Data Analycs run at the University of Aarhus in the fall of 2020.
The full project is implemented with supporting files from the folder : supporting_functions. 
Further the required libaries needed for this project is installed through the virtual enviroment. Which for this project is a Pipenv. 
Used a command prompt to run in the directory where the Pipfile is present "pipenv update"
The Python interpreter used is defaulted to Python 3.6 but this can be changed easily in the Pipfile to the desired version of Python 3. 
Visualization is through the Pythonbased webclient Dash which wires frontend view to a backend locally hosted server. Accessible on the IP: localhost:8050 

"""

import Path
import dash
from web_view.layout import layout
from web_view.callbacks import init_callback


if __name__ == '__main__':

    app = dash.Dash(
       __name__,
       assets_folder="{}/styling".format(Path(__file__).parent)
    )

    app = layout(app)
    init_callback(app)
    
    app.run_server(debug=True)