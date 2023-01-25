import streamlit as st
import pandas as pd


st.write("Link to buy book")
st.header("Link to Buy Book")
df=pd.read_csv('Data.xlsx - Merged Dataset_1.csv')
# select only title and link columns
data = df[['title', 'complete_link']]

    # Create interactive table using plotly
table = pd.DataFrame(data)

    # write the table
st.write(table)