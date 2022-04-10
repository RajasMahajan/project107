import pandas as pd
import plotly.express as px
import csv 

dataone = pd.read_csv("data.csv")

mean = dataone.groupby(["student_id","level"], as_index= False)["attempt"].mean()

print(mean)

fig = px.scatter(mean,x = "student_id",y = "level", size = 'attempt', color ='attempt')
fig.show()