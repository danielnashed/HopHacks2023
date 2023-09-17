import os.path

import streamlit as st
from components import sidebar
from services import medicalForm
import datetime
from services import prompts

st.set_page_config(
    page_title="Family Medical History",
    page_icon="👪",
    layout="wide"
)

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

st.markdown("# Known Family Medical History")

# st.write("Medical Conditions in Parents:")
# st.multiselect(label="parent_conditions", options=medicalForm.medical_conditions(), default=st.session_state.parent_conditions, key="parent_conditions",
#                placeholder="Known parent medical conditions")
#
# st.write("Medical Conditions in Siblings:")
# st.multiselect(label="sibling_conditions", options=medicalForm.medical_conditions(), default=st.session_state.sibling_conditions, key="sibling_conditions",
#                placeholder="Known sibling medical conditions")
#
# st.write("Medical Conditions in Grandparents:")
# st.multiselect(label="grandparent_conditions", options=medicalForm.medical_conditions(), default=st.session_state.grandparent_conditions, key="grandparent_conditions",
#                placeholder="Known grandparent medical conditions")
# Form
with st.form(key="family_med_form"):

    st.write("Medical Conditions in Parents:")
    st.multiselect(label="Parent Conditions", options=medicalForm.medical_conditions(), default=st.session_state.parent_conditions, key="parent_conditions",
                   placeholder="Known parent medical conditions")

    st.write("Medical Conditions in Siblings:")
    st.multiselect(label="Sibling Conditions", options=medicalForm.medical_conditions(), default=st.session_state.sibling_conditions, key="sibling_conditions",
                   placeholder="Known sibling medical conditions")

    st.write("Medical Conditions in Grandparents:")
    st.multiselect(label="Grandparent Conditions", options=medicalForm.medical_conditions(), default=st.session_state.grandparent_conditions, key="grandparent_conditions",
                   placeholder="Known grandparent medical conditions")
    # Submit button
    submit = st.form_submit_button("Submit")
    if submit:
        st.write("## Form Submitted!")
