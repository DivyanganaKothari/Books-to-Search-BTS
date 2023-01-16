import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.graph_objs as go
import plotly.offline as offline
import json


import plotly.subplots as sp
import os

import json

with open("output.json", "r") as f:
    output = json.load(f)
   # print(output)
    table1 = pd.DataFrame.from_dict(output, orient='index')
    print(table1) #score title and index

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

# Create a subplots figure
fig = sp.make_subplots(rows=1, cols=2, specs=[[{'type': 'bar'}, {'type': 'pie'}]])

# Add the first chart (bar chart)
fig.add_trace(go.Bar(x=table1['title'], y=table1['score'], name='Score distribution of Books',marker=dict(color='rgb(158,202,225)', line=dict(color='rgb(8,48,107)',width=1.5))), row=1, col=1)

# Add the second chart (pie chart)
fig.add_trace(go.Pie(labels=result['title'], values=result['rating'], name='Book title-Rating distribution'), row=1, col=2)

# Update the layout
fig.update_layout(title='Books Distribution', showlegend=True)
fig.update_xaxes(title_text="Book Title", row=1, col=1)
fig.update_yaxes(title_text="Score", row=1, col=1)
fig.show()
