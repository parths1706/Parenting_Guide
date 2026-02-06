import streamlit as st

def render_india_questions():
    # Wrapper removed for global centering
    
    
    st.markdown("<h2>Do you believe in horoscopes? If yes, please fill this out.</h2>", unsafe_allow_html=True)
    st.markdown("<p>Additional information to help us understand better</p>", unsafe_allow_html=True)
    
    birth_time = st.time_input("Birth-Time Of Your Child ? If You Remember ", value=None)
    horoscope = st.selectbox("Child's Horoscope (Zodiac Sign)", 
                            ["Unknown", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", 
                             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    
    # Back button (secondary)
    if st.button("← Back"):
        st.session_state.screen = "home"
        st.rerun()

    st.write("")  # spacing

    # Continue button (primary)
    if st.button("Continue", type="primary"):
        st.session_state.india_info = {
            "birth_time": str(birth_time) if birth_time else "Unknown",
            "horoscope": horoscope
        }
        st.session_state.screen = "traits"
        st.rerun()
