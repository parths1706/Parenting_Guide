import streamlit as st
from ai.prompts import analysis_prompt
from ai.llm_client import ask_llm
from utils.session import reset_flow

def render_result():
    # Header on purple background (OUTSIDE card)
    st.markdown('<div class="app-header"><h1>Know About Your Child</h1><p>Personalized insights for your child\'s growth 💕</p></div>', unsafe_allow_html=True)

  

    if not st.session_state.result:
        # Loading screen - everything inside white card
        st.markdown('<div class="thinking-emoji">🧸</div>', unsafe_allow_html=True)
        st.markdown('<h2 style="text-align: center; color: #3730a3; margin-bottom: 1rem;">AI is Analyzing...</h2>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; color: #6b7280; margin-bottom: 2rem;">Creating a personalized profile for your child based on the traits you selected.</p>', unsafe_allow_html=True)
        
        data = {
            **st.session_state.basic_info,
            "india_info": st.session_state.india_info,
            "traits": st.session_state.traits
        }

        with st.spinner(""):
            prompt = analysis_prompt(data)
            try:
                st.session_state.result = ask_llm(prompt)
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
                if st.button("RETRY", type="primary"): st.rerun()

    else:
        # Result screen - everything inside white card
        st.markdown('<div class="result-emoji">🎓</div>', unsafe_allow_html=True)
        st.markdown('<h2 style="text-align: center; color: #3730a3; margin-bottom: 2rem;">Know About Your Child</h2>', unsafe_allow_html=True)
        
        st.markdown(st.session_state.result)
        
        st.write("")
        st.write("")
        if st.button("START OVER 🔄", type="primary"):
            reset_flow()
            st.session_state.welcomed = False
            st.rerun()
