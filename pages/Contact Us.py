import streamlit as st
# Style
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# Title
st.title("Contact Us")