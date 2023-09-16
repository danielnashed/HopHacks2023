import streamlit as st
from components import sidebar

st.set_page_config(
    page_title="Medical History",
    page_icon="🧑",
    layout="wide"
)

sidebar.display()

st.markdown("# Plotting Demo")