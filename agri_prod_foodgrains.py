from dash import Dash, html, dcc, Input , Output
import pandas as pd
import plotly.express as px

url = "C:\\Users\\user\\Desktop\\datasets\\rbi\\Agricultural_Production_-_Foodgrains.xlsx"
url2 = "C:\\Users\\user\\Desktop\\datasets\\rbi\\Agricultural_Production_-_Major_Commercial_Crops.xlsx"
url3 = "C:\\Users\\user\\Desktop\\datasets\\rbi\\Area_Under_Cultivation_-_Foodgrains.xlsx"

df = pd.read_excel(url, usecols="B:H")
df2 = pd.read_excel(url2, usecols="C:M", header=6, nrows=71)
df3 = pd.read_excel(url3, usecols="C:I", header=5, nrows=71)
#print(df2.head())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.Div([
        dcc.Markdown("""

        ## Food Grains Time Series (India)
        
        """),

        dcc.Dropdown(
            df.columns,
            'Rice',
            id='col'
            ),
        ]),
    
    html.Div([

        dcc.Graph(id='type')
        ], style={'width':'50%', 'display':'inline-block'}),

      html.Div([

        dcc.Graph(id='auc-type')
        ], style={'width':'50%', 'display':'inline-block', 'float':'right'}),
    
    html.Hr(),

    html.Div([
        dcc.Markdown("""

        ## Food Grains(Major Commercial crops) Time Series (India)
        
        """),

        dcc.Dropdown(
            df2.columns,
            'Groundnut',
            id='mcc'
            ),

        dcc.Graph(id='mcc-type')
        ])
    ])


@app.callback(
    Output('type', 'figure'),
    Input('col', 'value'))
def update_graph(grain):
    fig = px.line(df, x='year', y=grain)
    fig.update_layout(
        title=f"{grain} production in India(in Lakh Tonnes)",
        yaxis_title="Production")
    return fig

@app.callback(
    Output('auc-type', 'figure'),
    Input('col', 'value'))
def update_graph(grain):
    fig = px.line(df3, x='year', y=grain)
    fig.update_layout(
        title=f"Area used for {grain} production in India(in Lakh hectares)",
        yaxis_title="Area")
    return fig


@app.callback(
    Output('mcc-type', 'figure'),
    Input('mcc', 'value'))
def update_graph(grain):
    fig = px.line(df2, x='year', y=grain)
    fig.update_layout(
        title=f"{grain} production in India(in Lakh Tonnes)",
        yaxis_title="Production")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)



