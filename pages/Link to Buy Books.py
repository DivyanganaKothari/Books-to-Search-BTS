import streamlit as st
import pandas as pd

import streamlit_BTS
st.write("Link to buy book")
st.header("Link to Buy top 10 recommended Books")

df = st.cache.df_output_link

    # Create interactive table using plotly
table = pd.DataFrame(df).from_dict(df, orient='index')
st.write(table)
