import streamlit as st
from components import sidebar
from services import medicalForm


st.set_page_config(
    page_title="Medical History",
    page_icon="🧑",
    layout="wide"
)

sidebar.display()

st.markdown("# Known Medical Conditions:")

# If session state does not have the medical history keys, initialize them
if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = 0
if "gender" not in st.session_state:
    st.session_state.gender = ""
if "smoker" not in st.session_state:
    st.session_state.smoker = ""
if "med_conditions" not in st.session_state:
    st.session_state.med_conditions = []
if "allergies" not in st.session_state:
    st.session_state.allergies = ""

# Form
with st.form("medical_history_form"):
    st.text_input("Full Name:", value=st.session_state.name, key="name")
    st.number_input("Age:", value=st.session_state.age, key="age")
    # st.radio("Gender: ", options=["Male", "Female", "Other", "Prefer not to say"], key="gender",horizontal=True)
    # st.radio("Smoker: ", options=["Yes", "No"], key="smoker", horizontal=True)

    st.multiselect(label="", options=medicalForm.medical_conditions(), default=st.session_state.med_conditions, key="med_conditions",
                   placeholder="Known medical conditions")

    st.text_area("Allergies:", value=st.session_state.allergies, key="allergies")

    submit = st.form_submit_button("Submit")

    if submit:
        st.markdown("## Form Submitted!")
