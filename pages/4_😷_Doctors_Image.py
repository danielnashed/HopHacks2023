
import numpy as np
import streamlit as st
import pandas as pd
import datetime
import os
from components import sidebar
import datetime
if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = 18
if "dob" not in st.session_state:
    st.session_state.dob = datetime.datetime.now()
if "gender" not in st.session_state:
    st.session_state.gender = ""
if "smoker" not in st.session_state:
    st.session_state.smoker = ""
if "med_conditions" not in st.session_state:
    st.session_state.med_conditions = []
if "allergies" not in st.session_state:
    st.session_state.allergies = ""
if "meds" not in st.session_state:
    st.session_state.meds = ""
if "parent_conditions" not in st.session_state:
    st.session_state.parent_conditions = []
if "sibling_conditions" not in st.session_state:
    st.session_state.sibling_conditions = []
if "grandparent_conditions" not in st.session_state:
    st.session_state.grandparent_conditions = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": prompts.startPrompt()}
    ]
st.session_state.name = st.session_state.name
st.session_state.age = st.session_state.age
st.session_state.dob = st.session_state.dob
st.session_state.gender = st.session_state.gender
st.session_state.smoker = st.session_state.smoker
st.session_state.med_conditions = st.session_state.med_conditions
st.session_state.allergies = st.session_state.allergies
st.session_state.meds =  st.session_state.meds
st.session_state.parent_conditions = st.session_state.parent_conditions
st.session_state.sibling_conditions = st.session_state.sibling_conditions
st.session_state.grandparent_conditions = st.session_state.grandparent_conditions
st.session_state.messages = st.session_state.messages


sidebar.display()

st.title("Overview")

if 'y' not in st.session_state:
    st.session_state.y = []




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
    st.markdown(f"**Patient:** {st.session_state.name}")
    st.write(f"**Age:** {st.session_state.age}")
    st.write(f"**Date of Birth:** {str(st.session_state.dob)}")
    st.write(f"**Known Medical Conditions:** {', '.join(st.session_state.med_conditions)}")
    st.write(f"**Allergies:** {st.session_state.allergies}")
    st.write(f"**Current Medication:** {st.session_state.meds}")
    st.write(f"**Parent Medical Conditions:** {', '.join(st.session_state.parent_conditions)}")
    st.write(f"**Sibling Medical Conditions:** {', '.join(st.session_state.sibling_conditions)}")
    st.write(f"**Grandparents Medical Conditions:** {', '.join(st.session_state.grandparent_conditions)}")

with st.expander("AI Suggestions"):
    st.write("Not finished yet")
    

with st.expander("Diagnoses/ Comments"):
    d = st.date_input("Date: ", datetime.datetime.now())
    t = st.time_input('Time:', datetime.datetime.now())
    title = st.text_input('Diagnostic:')
    recomendation = st.text_input('Recommended Treatment and Comments:')
    st.download_button('Download Report', 'Date: ' + str(d) + '\n\n' + 'Time: ' + str(t)  + '\n\n' + 'Diagnostic: ' + title + '\n\n' + 'Recommended Treatment and Comments: ' + recomendation) 
    

