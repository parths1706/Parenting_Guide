import streamlit as st
from utils.session import init_session
from ui.style import load_css
from ui.home import render_home
from ui.india_questions import render_india_questions
from ui.traits import render_traits
from ui.result_view import render_result

# 1. Page Config
st.set_page_config(
    page_title="Know Your Child",
    page_icon="💜",
    layout="centered"
)

# 2. Load Styles
load_css()

# 3. Initialize Session
init_session()

# 4. Routing Logic
if st.session_state.screen == "home":
    render_home()

elif st.session_state.screen == "india":
    render_india_questions()

elif st.session_state.screen == "traits":
    render_traits()

elif st.session_state.screen == "result":
    render_result()
