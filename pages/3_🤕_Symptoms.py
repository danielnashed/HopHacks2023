import openai
import os
import streamlit as st
# from streamlit_chat import message
from components import sidebar
from services import prompts
import asyncio
from services import llm


# Set org ID and API key
openai.organization = "org-3I5fILcDiX79DQpjuWTbt184"
openai.api_key = "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"

# set page layout
st.set_page_config(
    page_title="Symptoms",
    page_icon="🤕",
    layout="wide"
)

# Sidebar - let user clear the current conversation
sidebar.display()
clear_button = st.sidebar.button("Clear Conversation", key="clear")

st.markdown("<h1 style='text-align: center;'>Chatbox to share your symptoms.</h1>", unsafe_allow_html=True)

# Initialise session state variables
# if 'generated' not in st.session_state:
#     st.session_state['generated'] = []
# if 'past' not in st.session_state:
#     st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": prompts.initialRole()}
    ]
# reset everything
if clear_button:
    # st.session_state['generated'] = []
    # st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": prompts.initialRole()}
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

print(st.session_state.messages)
# generate a response
# def generate_response(prompt):
#     st.session_state['messages'].append({"role": "user", "content": prompt})
#
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         temperature = 0.9,
#         top_p = 0.9,
#         messages=st.session_state['messages']
#     )
#     response = completion.choices[0].message.content
#     st.session_state['messages'].append({"role": "assistant", "content": response})
#     return response


# # container for chat history
# response_container = st.container()
# # container for text box
# container = st.container()
#
# with container:
#     with st.form(key='my_form', clear_on_submit=True):
#         user_input = st.text_area("You:", key='input', height=100)
#         submit_button = st.form_submit_button(label='Send')
#
#     if submit_button and user_input:
#         output = generate_response(user_input)
#         st.session_state['past'].append(user_input)
#         st.session_state['generated'].append(output)
#
#
# if st.session_state['generated']:
#     with response_container:
#         for i in range(len(st.session_state['generated'])):
#             message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
#             message(st.session_state["generated"][i], key=str(i))
#
#





