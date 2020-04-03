# COVID-19 Notebooks
* `base-builder.ipynb` is run to produce the base build of merged and cleaned-up CSV file from [JHU CSSE daily reports](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports). `jhu-daily-reports.csv` has the following columns:

| Country | State | County | Date    | Confirmed | Deaths | Recovered | Confirmed_New | Deaths_New | Recovered_New | 
|---------|-------|--------|---------|-----------|--------|-----------|---------------|------------|---------------| 
|         |       |        |         |           |        |           |               |            |               | 

* `incremental-builder.ipynb` is run everyday to incrementally merge in new data into `jhu-daily-reports.csv`.
* `visualization.ipynb` reads this CSV and generates the following visualizations.

World-wide daily new cases broken up by top 10 contributing countries.
![Global Spread](https://storage.googleapis.com/atreya/global-covid-spread.png)

US daily new cases broken up by top 10 contributing states.
![US Spread](https://storage.googleapis.com/atreya/us-covid-spread.png)

Comparing New Case growth in India against other leading countries.
![India Growth](https://storage.googleapis.com/atreya/india-growth.png)

Comparing New Case growth of top 10 US states against each other.
![India Growth](https://storage.googleapis.com/atreya/us-state-growth.png)
