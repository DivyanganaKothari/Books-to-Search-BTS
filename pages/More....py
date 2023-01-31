import streamlit as st
import pandas as pd
from config import SetStyle
#style
# Style
SetStyle(st)

if not hasattr(st.cache, 'df_output_link'):
    st.cache.df_output_link = []

df = st.cache.df_output_link


# Title

title="Link to Buy top " + str(len(df)) + " recommended Books"
st.markdown("<h1 style='text-align:center; padding:20px;' >" + title + "</h1>", unsafe_allow_html=True)

st.write( "Here you can get link to buy the top Recommended books, please enter your search first so we can recommend the book")

table = pd.DataFrame(df).from_dict(df, orient='index')

def make_clickable(val):
    return f'<a target="_blank" href="{val}">{val}</a>'
  # Create interactive table using plotly

# Convert the 'link' column to clickable links

# Display the table with the clickable links
if len(df):
    for _, row in table.iterrows():
        st.markdown(f"[{row['title']}]({row['link']})")
    table['link'] = table['link'].apply(lambda x: f'<a href="{x}">{x}</a>')
    st.dataframe(table)


