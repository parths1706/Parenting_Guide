import streamlit as st

def init_session():
    if "screen" not in st.session_state:
        st.session_state.screen = "home"
    
    if "basic_info" not in st.session_state:
        st.session_state.basic_info = {}
        
    if "india_info" not in st.session_state:
        st.session_state.india_info = {}
        
    if "traits" not in st.session_state:
        st.session_state.traits = []
        
    if "result" not in st.session_state:
        st.session_state.result = None

def reset_flow():
    st.session_state.screen = "home"
    st.session_state.basic_info = {}
    st.session_state.india_info = {}
    st.session_state.traits = []
    st.session_state.result = None
