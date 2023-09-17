import os.path

import streamlit as st
from components import sidebar
from services import medicalForm

st.set_page_config(
    page_title="Family Medical History",
    page_icon="👪",
    layout="wide"
)

sidebar.display()

st.markdown("# Known Family Medical History")

# If session state does not have the family medical history keys, initialize them
if "parent_conditions" not in st.session_state:
    st.session_state.parent_conditions = []
if "sibling_conditions" not in st.session_state:
    st.session_state.sibling_conditions = []
if "grandparent_conditions" not in st.session_state:
    st.session_state.grandparent_conditions = []

# Form
with st.form(key="family_med_form"):
    st.write("Medical Conditions in Parents:")
    st.multiselect(label="", options=medicalForm.medical_conditions(), default=st.session_state.parent_conditions, key="parent_conditions",
                   placeholder="Known parent medical conditions")

    st.write("Medical Conditions in Siblings:")
    st.multiselect(label="", options=medicalForm.medical_conditions(), default=st.session_state.sibling_conditions, key="sibling_conditions",
                   placeholder="Known sibling medical conditions")

    st.write("Medical Conditions in Grandparents:")
    st.multiselect(label="", options=medicalForm.medical_conditions(), default=st.session_state.grandparent_conditions, key="grandparent_conditions",
                   placeholder="Known grandparent medical conditions")

    # Submit button
    submit = st.form_submit_button("Submit")
    if submit:
        st.write("Form Submitted!")

