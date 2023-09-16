import streamlit as st
from components import sidebar

st.set_page_config(
	page_title="Home",
	page_icon="🏥",
	layout="wide"
)

sidebar.display()

st.title("⚕ Welcome to Medical Assistant")
st.write("Insert some information about what this thing actually does here")