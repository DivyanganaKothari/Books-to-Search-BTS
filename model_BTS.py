import warnings
warnings.filterwarnings("ignore")
import uvicorn
from fastapi import FastAPI
import subprocess
import json
import csv
import datetime
import pandas as pd
import subprocess

from sentence_transformers.util import semantic_search
import pandas as pd
from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt

model = SentenceTransformer('bert-base-cased')

df= pd.read_csv('Data.xlsx - Merged Dataset_1.csv')
df2 = pd.read_pickle('Embeddings.pkl')
#filename= "test.csv"



# query = input('Enter your query: ')
# query_embedding = model.encode(query, convert_to_tensor=True,device='cpu')

# top_k = 10
# results = semantic_search(query_embedding, df2['Embeddings'].to_list(), top_k=top_k)

# print("Query:", query)
# print("Top 10 most similar sentences in corpus:")
# for i in results[0]:
#     id = i['corpus_id']
#     print('corpus_id:', id, "\t","score:", i['score'], "\t", df['title'][id])
    

# use fastapi to create a web app
app = FastAPI()

@app.get("/")
def read_root():
    return {"Heartly Welcome to BTS": "This is a web app for semantic search"}

# input query
@app.get("/query/{query}")
def read_item(query: str):
    query_embedding = model.encode(query, convert_to_tensor=True,device='cpu')
    top_k = 10
    results = semantic_search(query_embedding, df2['Embeddings'].to_list(), top_k=top_k)
    output ={}        
    
    print("Query:", query)
    print("Top 10 most similar sentences in corpus:")
    for i in results[0]:
        id = i['corpus_id']
        score = i['score']
        title = df['title'][id]
        output[id] = {"score": score, "title": title}
        ('corpus_id:', id, "\t","score:", i['score'], "\t", df['title'][id])
        with open("output.json", "w") as f:
            json.dump(output, f)
    return {"query": query, "output": output}
    #subprocess.run("python","vis.py",output)


'''  # Get current date and time
    now = datetime.datetime.now()

    # Create a filename using current date and time
    filename = f"output_{now.day}_{now.hour}.csv"

    # Open a file in write mode
    with open(filename, 'w', newline='') as csvfile:
        # Create a CSV writer
        csvwriter = csv.writer(csvfile)

        # Write the header row
        csvwriter.writerow(['Index', 'Title', 'Score'])

        # Iterate over the output and write each row
        for index, item in output.items():
            csvwriter.writerow([index, item['title'], item['score']])
            '''


#df = pd.DataFrame(output)
#df.to_csv('output.csv', index=False, header=True)


if __name__ == "__main__":

    uvicorn.run(app)


    

