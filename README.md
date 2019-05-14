# 'Taking Data Visualisation to Another Level'

Testing what kind of amazing visualisations you can create by python.

## Project Goal: 

It is my first project with python. The main purpose is to learn new skills. 

- Start: 26/04/2019
- End: 28/05/2019

## First Visualisation 'Top 10 shoe brands'

### Data

- Import data from website: [Node.js](https://data.world/datafiniti/womens-shoe-prices)

### Data Summary

This is a list of 10,000 women's shoes and their product information provided by Datafiniti's Product Database.
The dataset includes shoe name, brand, price, and more. Each shoe will have an entry for each price found for it and some shoes may have > multiple entries.

> Dataset information
> LAST MODIFIED: April 24, 2017
> OWNER: @datafiniti
> CREATED: April 24, 2017
> SIZE:43.92 MB
> Displaying 47 columns, 19,045 rows in table

### Steps to get a final visualisation 

1. Clean and prepare data for visualisation. Use code below.

```#import file.csv as dataframe
import pandas as pd
df = pd.read_csv('https://query.data.world/s/rgxzfnoqy4kk35y2a4uloqq5cd4wna')
#create new dataframe just for column 'brand'
n_df = df[['brand']]
#count frequency of each brand
n=10
n1_df = n_df.merge(n_df['brand'].value_counts().to_frame(), how='left', left_on ='brand',
           right_index = True, suffixes =('','x')).rename(columns = {'brandx':'brand_count'})
#eliminate duplicates and get top 10
n2_df = n1_df.drop_duplicates(['brand','brand_count'])
final_df = n2_df.sort_values('brand_count',ascending=False).head(10)
#reset indexes
final_df = final_df.reset_index()
del final_df['index']
#to save dataframe as csv
final_df.to_csv('data_visual.csv', index=False)
```
2. Add manually column 'brand_logo' into file.
3. Create a visualisation
```
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Greys10
from bokeh.embed import components
output_file('index.html')
output_file("background.html")
df = pd.read_csv('data_visual.csv')
source = ColumnDataSource(df)

brand_list = source.data['brand'].tolist()

p = figure(
    y_range = brand_list,
    plot_width = 600,
    plot_height = 800,
    title='TOP 10 Shoe Brand',
    tools = 'pan, box_select, zoom_in, zoom_out,save, reset',
    
   )
p.hbar(
y = 'brand',
right = 'brand_count',
left = 0,
height = 0.4,
fill_color = factor_cmap('brand',
palette = Greys10,
 factors = brand_list),                     
fill_alpha = 10.0,
source = source,
legend = 'brand', 
)
p.xaxis.major_tick_line_color = None  # turn off x-axis major ticks
p.xaxis.minor_tick_line_color = None  # turn off x-axis minor ticks
p.title.text_font_size = '14pt'
p.outline_line_color = "black"
p.background_fill_color = "beige"
p.xaxis.major_label_text_font_size = '0pt'
p.yaxis.major_label_text_font_size = '12pt'
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'
hover = HoverTool()
hovertooltips =hover.tooltips = """
  <div>
    <h3>@brand</h3>
    <div><img src="@brand_logo" alt="" width="200" /></div>
  </div>
"""
p.add_tools(hover)
show(p)


```
