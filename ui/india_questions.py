import streamlit as st

def render_india_questions():
    # Wrapper removed for global centering
    
    st.markdown('<div class="app-header"><h1>Know Your Child</h1><p>Personalized insights for your child\'s growth 💕</p></div>', unsafe_allow_html=True)
    
    st.markdown("<h2>Additional Information</h2>", unsafe_allow_html=True)
    st.markdown("<p>If You Believe in Horoscope please fill this...</p>", unsafe_allow_html=True)
    
    birth_time = st.time_input("Birth-Time Of Your Child ? If You Remember ", value=None)
    horoscope = st.selectbox("Child's Horoscope (Zodiac Sign) ? If You Know ", 
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
