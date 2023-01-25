# create a web using streamlit 
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
from sentence_transformers.util import semantic_search
import pandas as pd
from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import json
import csv
import plost


model = SentenceTransformer('bert-base-cased')

df= pd.read_csv('Data.xlsx - Merged Dataset_1.csv')
df2 = pd.read_pickle('Embeddings.pkl')

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("BTS-Book Recommendation System")
# Row A
st.markdown('### Semantic Search')
col1, col2, col3 = st.columns(3)
col1.metric("Books", "1470")
col2.metric("Source", "Kaggel")
col3.metric("Accuracy","64%")

#dataset
data=pd.read_csv('Data.xlsx - Merged Dataset_1.csv')

query = st.text_input("Enter your query")
if st.button("Search"):
    query_embedding = model.encode(query, convert_to_tensor=True,device='cpu')
    top_k = 10
    results = semantic_search(query_embedding, df2['Embeddings_title'].to_list(), top_k=top_k)
    output ={}        
    
    for i in results[0]:
        id = i['corpus_id']
        score = i['score']
        title = df['title'][id]
        rating= df['rating'][id]
        output[id] = {"score": score, "title": title, "rating": rating}

    df_output = pd.DataFrame.from_dict(output, orient='index')
    st.write(df_output)

    #st.write(table1)  # score title and index
#2 columns
    c1, c2 = st.columns((6,4))

    with c1:
        st.markdown('### Bar Chart')
        fig = px.bar(df_output, x='title', y='score')
        fig.update_layout(xaxis={'categoryorder': 'total descending'}, yaxis={'title': 'score'},
                      xaxis_tickangle=-45, yaxis_title='title')
        fig.data[0].marker.color = ['red', 'blue', 'green', 'purple', 'yellow', 'violet', 'indigo', 'orange', 'navy',
                                'brown']
        st.plotly_chart(fig)

    with c2:
        st.markdown('### Pie Chart')
        fig2 = px.pie(df_output, values='rating', names='title',
                  color_discrete_sequence=['red', 'blue', 'green', 'purple', 'yellow', 'violet', 'indigo', 'orange',
                                           'navy',
                                           'brown'])
        st.plotly_chart(fig2)























