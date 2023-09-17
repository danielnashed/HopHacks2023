
import numpy as np
import streamlit as st
import pandas as pd
import datetime
import os


st.title("Dashboard")

if 'y' not in st.session_state:
    st.session_state.y = []

print(st.session_state)

with st.expander("Patient Vitals"):
    path = os.path.join("data","healthkit_data.csv")
    print(os.path.exists(path))
    dataframe = pd.read_csv(path) 
    st.multiselect(label="", options = list(dataframe.columns)[1:], default = st.session_state.y, key="y")
    st.title("Patient Vitals")
    st.line_chart(
    dataframe,
    x = 'Date',
    y = st.session_state.y,
)


with st.expander("Medical and Family History"):
    st.write("Not finished yet")

with st.expander("AI Suggestions"):
    st.write("Not finished yet")
    

with st.expander("Diagnoses/ Comments"):
    d = st.date_input("Date: ", datetime.datetime.now())
    t = st.time_input('Time:', datetime.datetime.now())
    title = st.text_input('Diagnostic:')
    recomendation = st.text_input('Recommended Treatment and Comments:')
    st.download_button('Download Report', 'Date: ' + str(d) + '\n\n' + 'Time: ' + str(t)  + '\n\n' + 'Diagnostic: ' + title + '\n\n' + 'Recommended Treatment and Comments: ' + recomendation) 
    

