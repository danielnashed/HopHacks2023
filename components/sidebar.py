import streamlit as st

def display():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Page 1", "Page 2", "Page 3"])
    return page