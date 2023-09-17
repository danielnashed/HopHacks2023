import streamlit as st
from components import sidebar
from services import prompts
import asyncio
from services import llm
import datetime

# set page layout
st.set_page_config(
    page_title="Symptoms",
    page_icon="🤕",
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
if "report" not in st.session_state:
    st.session_state.report = ""

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
st.session_state.report = st.session_state.report


# Sidebar - let user clear the current conversation
sidebar.display()
clear_button = st.sidebar.button("Clear Conversation", key="clear")

st.markdown("<h1 style='text-align: center;'>Chatbox to share your symptoms.</h1>", unsafe_allow_html=True)

# Initialise session state variables
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": prompts.startPrompt()}
    ]
# reset everything
if clear_button:
    st.session_state['messages'] = [
        {"role": "system", "content": prompts.startPrompt()}
    ]

# Print all messages in the session state
for message in [m for m in st.session_state.messages if m["role"] != "system"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat with the LLM, and update the messages list with the response, updating UI
async def chat(messages):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        messages = await llm.run_conversation(messages, message_placeholder)
        st.session_state.messages = messages
    return messages

# React to the user prompt
if prompt := st.chat_input("How are you feeling today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    asyncio.run(chat(st.session_state.messages))
# st.write(st.session_state)





