import streamlit as st
import graphviz
import pandas as pd
import plotly.express as px


# Style
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# Title
st.markdown(' ### Here you can get to know more about our dataset')

# Row A for for adding 3 description boxes
col1, col2, col3 = st.columns(3)
col1.metric("Books", "1470")
col2.metric("Source", "Kaggle")
col3.metric("Accuracy","64%")

df= pd.read_csv('Data.xlsx - Merged Dataset_1.csv')

#Average rating distribution for all books
st.markdown('### Average rating distribution for all books')
df.rating = df.rating.astype(float)
fig3 = px.histogram(df, x='rating', nbins=50)#The number of bins (also known as intervals or classes) determines the granularity of the histogram.

fig3.update_layout( xaxis_title='Average rating',
                   font=dict(size=20))
fig3.update_traces(marker=dict(color='#C58059'))
st.plotly_chart(fig3)

option = st.selectbox(
    'How would you like to be view the flow?',
     ('Simple Flow of our Model', 'Detailed Flow of our Model'))
if option== 'Simple Flow of our Model':
    graph= graphviz.Digraph()
    graph.edge('User','Input')
    graph.edge('Input','Semantic Search','Word Embedding')
    graph.edge('Semantic Search','Recommendation','Similarity Score')
    graph.edge('Recommendation','Visualization')
    graph.edge('Visualization','Input')

    st.graphviz_chart(graph)
else:
    graph2= graphviz.Digraph()
    graph2.edge('MySQL(Database)','Backend')
    graph2.edge('Backend','Data Cleaning','Model')
    graph2.edge('Data Cleaning','Pre-Trained Model(BERT)')
    graph2.edge('Pre-Trained Model(BERT)','Embeddings')
    graph2.edge('Embeddings','Semantic Search','Similarity Score')
    graph2.edge('Semantic Search','Recommendations','Top 10')
    graph2.edge('User','Input')
    graph2.edge('Input','Embeddings')
    graph2.edge('Embeddings','Semantic Search')
    graph2.edge('Recommendations', 'Visualization')
    graph2.edge('Visualization', 'Input')

    st.graphviz_chart(graph2)


