import streamlit as st
from components import sidebar
from pages import famMedHistory, medHistory, symptomsQA


st.set_page_config(
	page_title="Med Application",
	layout="wide"
)
PAGES = {
    "Medical History": medHistory,
    "Family Medical History": famMedHistory,
    "Current Symptoms": symptomsQA
}



# helpers.sidebar.show()


st.markdown("Welcome to FinFriend, your AI-powered personal finance assistant!")
st.write("FinFriend is designed to help you explore and understand your personal finances.")


def main():
    choice = sidebar.display()

    if choice in PAGES:
        PAGES[choice].display()

if __name__ == "__main__":
    main()