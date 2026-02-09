import streamlit as st
from ai.trait_generator import generate_traits

def render_traits():
    age = st.session_state.basic_info.get("age", 0)
    country = st.session_state.basic_info.get("country")

    st.markdown(
        '<div class="app-header"><h1>Know Your Child</h1>'
        '<p>Personalized insights for your child\'s growth 💕</p></div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="main-card-container">', unsafe_allow_html=True)

    # -------------------------------
    # Dynamic Title
    # -------------------------------
    if age < 3:
        title = "Early Tendencies & Temperament 🌱"
        subtitle = (
            "These are gentle, editable tendencies based on age, culture"
            + (" and astrology." if country == "India" else ".")
        )
    else:
        title = "Personality Traits 🌟"
        subtitle = "Select or edit traits that reflect your child."

    st.markdown(
        f"""
        <h2 style="text-align:center;color:#3730a3;">{title}</h2>
        <p style="text-align:center;color:#6b7280;">{subtitle}</p>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------
    # AI-GENERATED TOKENS (AGE < 3)
    # -------------------------------
    if age < 3:
        if "ai_traits" not in st.session_state:
            with st.spinner("Understanding your child..."):
                st.session_state.ai_traits = generate_traits(
                    {
                        **st.session_state.basic_info,
                        "india_info": st.session_state.get("india_info", {})
                    }
                )

        ai_traits = st.session_state.ai_traits

        # Editable chips
        selected = st.multiselect(
            "Suggested traits (you can add or remove)",
            options=ai_traits,
            default=ai_traits
        )

        # Extra traits user can add
        extra_traits = st.multiselect(
            "Add more traits if you feel they apply",
            [
                "Calm", "Alert", "Affectionate", "Observant", "Adaptive",
                "Sensitive", "Expressive", "Independent", "Socially curious"
            ]
        )

        final_traits = list(set(selected + extra_traits))

    # -------------------------------
    # AGE ≥ 3
    # -------------------------------
    else:
        trait_options = [
            "Shy", "Extrovert", "Introvert", "Playful", "Creative",
            "Curious", "Active", "Sensitive", "Independent", "Focused",
            "Empathetic", "Observant", "Confident", "Fast Learner",
            "Emotional", "Disciplined", "Imaginative", "Competitive"
        ]

        final_traits = st.multiselect(
            "Select traits (editable)",
            trait_options
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # -------------------------------
    # NAVIGATION
    # -------------------------------
    st.markdown('<div class="bottom-actions">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Back"):
            st.session_state.screen = "india" if country == "India" else "home"
            st.rerun()

    with col2:
        if st.button("Analyze ✨", type="primary"):
            if not final_traits:
                st.error("Please keep at least one trait.")
            else:
                st.session_state.traits = final_traits
                st.session_state.screen = "result"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
