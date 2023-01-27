import streamlit as st
import graphviz
st.write("about us")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Row A for for adding 3 description boxes
st.markdown('### Semantic Search')
col1, col2, col3 = st.columns(3)
col1.metric("Books", "1470")
col2.metric("Source", "Kaggel")
col3.metric("Accuracy","64%")


graph= graphviz.Digraph()
graph.edge('User','Input')
graph.edge('Input','Semantic Search','Word Embedding')
graph.edge('Semantic Search','Similarity Score')
graph.edge('Similiarity Score','Recommendation','Rating')
graph.edge('Recommendation','Visualization')
graph.edge('Visualization','Input')

st.graphviz_chart(graph)
