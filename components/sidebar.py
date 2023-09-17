import streamlit as st

def display():
    with st.sidebar:
        # st.title("Navigation")
        st.markdown('''
                <div style="display:table;margin-top:-18.6rem;margin-left:10%;color:black;text-decoration: none;">
                    <img src="/app/static/logo_noText.png" width="60"><span>    Panacea  </span>
                    <span style="font-size: 0.8em; color: grey">&nbsp;&nbsp;v0.1.0</span>
                    <br>
                    <span style="font-size: 0.8em">SLOGAN</span>
                </div>
            <br>
        
        ''', unsafe_allow_html=True)

        reload_button = st.button("↪︎  Reload Page")
        if reload_button:
            st.session_state.clear()
            st.experimental_rerun()