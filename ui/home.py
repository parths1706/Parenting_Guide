import streamlit as st
from utils.helpers import calculate_age
from datetime import date

def render_home():

    if "welcomed" not in st.session_state:
        st.session_state.welcomed = False

    # 🔹 Header (purple background)
    st.markdown("""
        <div class="app-header">
            <h1>Know About Your Child</h1>
            <p>Personalized insights for your child's growth 💕</p>
        </div>
    """, unsafe_allow_html=True)

    if not st.session_state.welcomed:
        st.markdown('<div class="splash-emoji">👋</div>', unsafe_allow_html=True)

        st.markdown("""
            <h2 style="text-align:center; color:#3730a3;">
                Welcome!
            </h2>
            <p style="text-align:center; color:#6b7280; margin-bottom:2rem;">
                Discover personalized AI insights to help your child thrive.
                It only takes a minute!
            </p>
        """, unsafe_allow_html=True)

        if st.button("START MY JOURNEY ✨", type="primary"):
            st.session_state.welcomed = True
            st.rerun()

    else:
        st.markdown("""
            <h2 style="text-align:center; color:#3730a3;">
                Let’s get started! 🎈
            </h2>
            <p style="text-align:center; color:#6b7280; margin-bottom:2rem;">
                Tell us a few details about your little one.
            </p>
        """, unsafe_allow_html=True)

        st.markdown("**Where are you from?**")
        country = st.selectbox(
            "",
            ["India", "USA", "UK", "Canada", "Other"],
            label_visibility="collapsed"
        )

        st.markdown("**Child’s Birthday**")
        birthdate = st.date_input(
            "",
            value=None,
            min_value=date(2009, 1, 1),
            max_value=date.today(),
            label_visibility="collapsed"
        )

        st.markdown("**Gender**")
        gender = st.radio(
            "",
            ["👦 Male", "👧 Female", "🌟 Other"],
            horizontal=True,
            label_visibility="collapsed"
        )

        if st.button("CONTINUE", type="primary"):
            if birthdate is None:
                st.error("Please select a birthday")
            else:
                age = calculate_age(birthdate)
                st.session_state.basic_info = {
                    "country": country,
                    "birthdate": str(birthdate),
                    "age": age,
                    "gender": gender.split()[1]
                }
                st.session_state.screen = "india" if country == "India" else "traits"
                st.rerun()

