import streamlit as st
import plotly.express as px
import pandas as pd

# Style
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# Title
#######
st.title('Here you can get wto know more about our dataset')
df= pd.read_csv('Data.xlsx - Merged Dataset_1.csv')
#Average rating distribution for all books
st.markdown('### Average rating distribution for all books')
df.rating = df.rating.astype(float)
fig3 = px.histogram(df, x='rating', nbins=50)#The number of bins (also known as intervals or classes) determines the granularity of the histogram.

fig3.update_layout( xaxis_title='Average rating',
                   font=dict(size=20))
fig3.update_traces(marker=dict(color='#C58059'))
st.plotly_chart(fig3)

st.markdown('### Select a chart type in which you want to visualize the data')
chart_type = st.selectbox('Select chart type', options=['Scatter', 'Line'])
col1, col2 = st.columns(2)

x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

if chart_type == 'Scatter':
    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color='#C58059'))
    st.plotly_chart(plot, use_container_width=True)

else:
    plot = px.line(df, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color='#C58059'))
    st.plotly_chart(plot, use_container_width=True)


#plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
#st.plotly_chart(plot, use_container_width=True)