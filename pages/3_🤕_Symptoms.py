import streamlit as st
from components import sidebar
from services import prompts

st.set_page_config(
    page_title="Symptoms",
    page_icon="🤕",
    layout="wide"
)

sidebar.display()

st.markdown("# Plotting Demo")


prompts.initialRole()