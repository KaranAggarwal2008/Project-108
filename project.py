import statistics
import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
df = pd.read_csv("project-data.csv")
dataList = df["Avg Rating"].tolist()

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist=False)
fig.show()