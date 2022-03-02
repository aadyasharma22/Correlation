import plotly.express as px

import csv

with open("correlationProjecttt.csv") as csvFile:
    df=csv.DictReader(csvFile)
    fig=px.scatter(df,x="week",y="Coffee in ml")
    fig.show()