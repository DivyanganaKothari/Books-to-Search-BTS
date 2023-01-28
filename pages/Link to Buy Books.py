import streamlit as st
import pandas as pd

# Style
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
# Title
st.title("Link to Buy top 10 recommended Books")

df = st.cache.df_output_link
table = pd.DataFrame(df).from_dict(df, orient='index')

def make_clickable(val):
    return f'<a target="_blank" href="{val}">{val}</a>'
  # Create interactive table using plotly

# Convert the 'link' column to clickable links

# Display the table with the clickable links
for _, row in table.iterrows():
    st.markdown(f"[{row['title']}]({row['link']})")
table['link'] = table['link'].apply(lambda x: f'<a href="{x}">{x}</a>')
st.dataframe(table)
