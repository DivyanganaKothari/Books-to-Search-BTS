import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as offline
import json
import datetime
from datetime import datetime
import plotly.subplots as sp
import os

import json

with open("output.json", "r") as f:
    output = json.load(f)
   # print(output)
    table1 = pd.DataFrame.from_dict(output, orient='index')
    print(table1)



#data= pd.read_csv("output.csv")
#print(data)

merged_list=[]

with open('Data.xlsx - Merged Dataset_1.csv','r') as i:
   reader=csv.reader(i)
   next(reader)
   for row in reader:
       index=row[0]
       title=row[1]
       rating=row[3]
       #print(f"title:{title}")
       #print(f"rating:{rating}")
       merged_list.append(index)
       merged_list.append(title)
       merged_list.append(rating)
#print(merged_list)        #merged list contaning title index and rating

#creating dictionary
output = []
for i in range(0, len(merged_list), 3):
        output.append({
        "index": merged_list[i],
        "title": merged_list[i + 1],
        "rating": merged_list[i + 2]
     })
#print(output)

# Convert the list of dictionaries to a DataFrame
table2 = pd.DataFrame(output)

# Print the resulting table
#print(table2)  #all data in form of table-index title and rating from all data set

result = table2.loc[table2['index'].isin(table1.index), ['title', 'rating']]
print(result) #get title with same index no. from the merged list

fig = go.Figure(data=[go.Table(
    header=dict(values=list(result.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[result[col] for col in result.columns],
               fill_color='lavender',
               align='left'))
])
fig.show()

# Create a bar chart trace
trace = go.Bar(x=table1['title'], y=table1['score'],
              marker=dict(color='rgba(0,0,255,0.5)', line=dict(color='rgb(0,0,0)', width=1.5)))

# Create a Figure object
fig = go.Figure(data=[trace])

# Set the layout
fig.update_layout(title='Score by Title', xaxis=dict(title='Title'), yaxis=dict(title='Score'))

# Show the figure
fig.show()

