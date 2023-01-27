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
    graph2.edge('Embeddings','Semantic Search')
    graph2.edge('Semantic Search','Recommendations','Top 10')
    graph2.edge('User','Input')
    graph2.edge('Input','Embeddings')
    graph2.edge('Embeddings','Semantic Search','Similarity Score')
    graph2.edge('Recommendations', 'Visualization')
    graph2.edge('Visualization', 'Input')

    st.graphviz_chart(graph2)


