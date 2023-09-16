import streamlit as st
from components import sidebar

st.set_page_config(
    page_title="Symptoms",
    page_icon="🤕",
    layout="wide"
)

sidebar.display()

st.markdown("# Plotting Demo")