import streamlit as st
import pandas as pd

#from streamlit_BTS import load_link
st.write("Link to buy book")
st.header("Link to Buy Book")
'''
df_output=load_link()
st.write(df_output)
'''

df=pd.read_csv('Data.xlsx - Merged Dataset_1.csv')
# select only title and link columns
data = df[['title', 'complete_link']]

    # Create interactive table using plotly
table = pd.DataFrame(data)

    # write the table
st.write(table)
