# 'Taking Data Visualisation to Another Level'

Testing what kind of amazing visualisations you can create by python.

## Project Goal: 

It is my first project with python. The main purpose is to learn new skills. 

- Start: 26/04/2019
- End: 28/05/2019

## First Visualisation 'Top 10 shoe brands'

## Data

- Import data from website: [Node.js](https://data.world/datafiniti/womens-shoe-prices)

# Data Summary

This is a list of 10,000 women's shoes and their product information provided by Datafiniti's Product Database.
The dataset includes shoe name, brand, price, and more. Each shoe will have an entry for each price found for it and some shoes may have > multiple entries.

> Dataset information
> LAST MODIFIED: April 24, 2017
> OWNER: @datafiniti
> CREATED: April 24, 2017
> SIZE:43.92 MB
> Displaying 47 columns, 19,045 rows in table

# Steps to get a final visualisation 

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
final_df.to_csv('data1_visual.csv', index=False)
```

