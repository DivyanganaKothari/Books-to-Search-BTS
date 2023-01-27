import streamlit as st
import plotly.express as px
import pandas as pd

df= pd.read_csv('Data.xlsx - Merged Dataset_1.csv')

st.markdown('### Scatter chart')
chart_type = st.selectbox('Select chart type', options=['Scatter', 'Line'])
col1, col2 = st.columns(2)

x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

if chart_type == 'Scatter':
    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)

else:
    plot = px.line(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)

#plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
#st.plotly_chart(plot, use_container_width=True)