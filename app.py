# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:56:06 2020

@author: ODsLaptop
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'NYS Teacher Pay vs Student Success by School District'
myheading='Analysis of teachers salaries vs students educational success in New York State'
#neighborhood='Columbia Heights'
color1='#04F9E6'
color2='#1B03B1'
githublink = 'https://github.com/odonnell31/NYS_Educational_Success'
sourceurl = 'https://data.nysed.gov/downloads.php'
#image_name = 'dc-flag.jpg'

########### Prepare the dataframe
df = pd.read_csv('data/Merged_dataset/NYS_Education_2019_v3.csv')

########### Set up the chart
trace = go.Scatter(
    x = df['Median_Teachers_Pay'],
    y = df['Graduation_Rate'],
    mode = 'markers',
    marker=dict(
        size=8,
        color = color1, # set color equal to a third variable
        #color = df['District_description'], # set color equal to a third variable
        colorscale=[color1, color2],
        colorbar=dict(title='District_description'),
        showscale=True
    )
)

data = [trace]
layout = go.Layout(
    title = f'NYS Teacher Pay vs Student Success by School District', # Graph title
    xaxis = dict(title = 'Median Teacher Salary ($)'), # x-axis label
    yaxis = dict(title = 'Student Graduation Rate'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)
fig = go.Figure(data=data, layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()