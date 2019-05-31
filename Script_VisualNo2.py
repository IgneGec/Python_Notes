#needed libraries

import pandas as pd
from plotly import __version__
%matplotlib inline
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.offline import iplot
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 
init_notebook_mode(connected=True)

init_notebook_mode(connected=True)
cf.go_offline()


# import a file

df = pd.read_csv('map_data.csv')

# clean a file and extract only needed columns

df_new=df[['state_id','state_name','population']]   

# add population by states

n_df = df_new.groupby(['state_id','state_name'])['population'].sum().reset_index()

#add thousands separators into column 'population'

n_df['population2'] = n_df.apply(lambda x: "{:,}".format(x['population']), axis=1)

for col in n_df.columns:
    n_df[col] = n_df[col].astype(str)
    
# set colar palette
scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]

# set text for tooltip

n_df['text'] = n_df['state_name'] + '<br>' + \
'Population: '+ n_df['population2']

#map settings
data = [go.Choropleth(
    colorscale = scl,
    autocolorscale = True,
    locations = n_df['state_id'],
    z = n_df['population'].tolist(),    
    locationmode = 'USA-states',
    text = n_df['text'],
    hoverinfo='text',
     marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = '#262626',
            width = 2)),
    colorbar = go.choropleth.ColorBar(
        title = "Population",
        titlefont = dict(
                family='Courier New, monospace',
                size=18,
                color='#262626',))
    
 )]


layout = go.Layout(
    title = go.layout.Title(
        text = 'Largest States in USA by Population',
        font=dict(
                family='Courier New, monospace',
                size=22,
                color='#262626')
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
)


fig = go.Figure(data = data, layout = layout)
#pyo.iplot(fig, filename = 'd3-cloropleth-map')

url = pyo.plot(fig, filename='d3-cloropleth-map')


