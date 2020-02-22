# ETL Project
## Authors: Jack Harvey, Mostafa Moamen, Matthew Richtmyer

# Overview
We are analyzing sports data from the NBA and NFL from 2000-2018. 

In this project, we are combining several disparate datasets, transforming/cleaning the data, and loading into a postgreSQL database. 

# Extract
* NFL data was acquired from a Kaggle dataset
  * https://www.kaggle.com/tobycrabtree/nfl-scores-and-betting-data#nfl_stadiums.csv

* NBA data was web-scraped using Pandas read_html function
  * Web site scraped: https://www.basketball-reference.com/friv/standings.fcgi?month=2&day=13&year=2019&lg_id=NBA
  * This was looped to scrape all data from the date range we are interested in. 
  
# Transform
* NFL data needed transformations to be calculate win percentage per team and year
  * [NFL Transformation](https://github.com/mrichtmyer/ETL_Project/blob/master/code/python/Full%20Data.ipynb)
* NBA data needed to be cleaned to combine all teams in the league. They were originally organized in divisions and could not be readily compared. 
  * [NBA Extraction and Transformation](https://github.com/mrichtmyer/ETL_Project/blob/master/code/python/nba_data.py)
* Both datasets needed to be combined with location data (e.g. city/state). 

# Load
* Table schema were created in PostgreSQL and all data was uploaded to create a sports database. 
  * [SQL Table Schmea](https://github.com/mrichtmyer/ETL_Project/blob/master/code/postgreSQL/sports_data.sql)
  
# Report
* Full report can be found here: [Final Report](https://github.com/mrichtmyer/ETL_Project/blob/master/report/ETL_report.pdf)
