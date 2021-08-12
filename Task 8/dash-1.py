# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
data = pd.read_csv("./owid-covid-data.csv")

data = data[data.astype(bool)]

countries = ["Italy", "United Kingdom", "United States", "India", "Bangladesh", "China", "Pakistan", "Sri Lanka"]
data_req = pd.DataFrame()

for i in countries:
    data_req = data_req.append(data[data["location"] == i][["location", "total_deaths", "total_cases"]])

fig1 = px.line(data_req, x = "total_cases", y="total_deaths", color="location")
fig2 = px.scatter(data_req, x = "total_cases", y="total_deaths", color="location")

app.layout = html.Div(children=[
    html.H1(children='CoVID Data Dashboard'),

    html.Div(children='''
        CoVID Dashboard
    '''),

    dcc.Graph(
        id='Line chart for CoVID deaths',
        figure=fig1
    ),

    dcc.Graph(
        id='Scatter chart for CoVID deaths',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)