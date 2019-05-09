# 'How Much Do Women's Shoes Cost?'

An interactive plot on web-browsers which helps you immediately to get some useful insights from a dataset of 10,000 women's shoes and their product information. Using the plot you can easily get answers to those questions below:

- What is the most popular shoes' brand?
- What is the average price of each distinct brand listed?
- Which brands have the highest prices?
- Which ones have the widest distribution of prices?
- Is there a typical price distribution (e.g., normal) across brands or within specific brands?

## Project Goal: 

It is my first project with python. The main purpose is to learn new skills. 

- Start: 26/04/2019
- End: 28/05/2019

## Stages

The project is divided into 2 main stages:

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

## Do you want to create the similar visualisation? If the answer is 'YES', follow steps below:

### Import file into python:

1. Install Pandas. Write in your terminal pip install pandas. 
Panda is a python package for data analysis, time series, and statistics. VERY USEFUL TOOL IN THE DATA WORLD!!

2. Open dataset. Use a script below:

```import pandas as pd
df = pd.read_csv('https://query.data.world/s/rgxzfnoqy4kk35y2a4uloqq5cd4wna')



