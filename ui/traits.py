import streamlit as st
from ai.trait_generator import generate_traits

def render_traits():
    age = st.session_state.basic_info.get("age", 0)
    country = st.session_state.basic_info.get("country")

    st.markdown(
        '<div class="app-header"><h1>Know About Your Child</h1>'
        '<p>Personalized insights for your child\'s growth 💕</p></div>',
        unsafe_allow_html=True
    )

    # Wrap the content in a custom class
    st.markdown('<div class="main-card-container">', unsafe_allow_html=True)

        # -------------------------------
    # Dynamic heading & subtitle
    # -------------------------------
    if age < 3:
        if country == "India":
            title_text = "Temperament & Early Tendencies 🌱"
            subtitle_text = (
                "These insights are gently guided by early development patterns "
                "and traditional horoscope influences."
            )
        else:
            title_text = "Temperament & Early Tendencies 🌱"
            subtitle_text = (
                "These insights are based on early childhood development and temperament."
            )
    else:
        title_text = "Personality Insights 🌟"
        subtitle_text = (
            "These traits reflect your child’s emerging personality and everyday behavior."
        )


    st.markdown(
         f'''
    <h2 style="text-align: center; color: #3730a3; margin-bottom: 0.8rem;">
        {title_text}
    </h2>
    <p style="text-align:center;color:#6b7280;margin-bottom:1.5rem;">
        {subtitle_text}
    </p>
    ''',
    unsafe_allow_html=True
    )

    # -------------------------------
    # CASE 1: AGE < 3 (AI GENERATED)
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

        traits = st.session_state.ai_traits

        st.markdown(
            '<p style="text-align:center;color:#6b7280;">'
            'These characteristics are development-based on Horoscope.</p>',
            unsafe_allow_html=True
        )

        for t in traits:
            st.markdown(f"- 🌱 {t}")

    # -------------------------------
    # CASE 2: AGE ≥ 3
    # -------------------------------
    else:
        trait_options = [
            "Shy", "Extrovert", "Introvert", "Playful", "Creative",
            "Curious", "Active", "Quiet", "Stubborn", "Sensitive",
            "Social", "Independent", "Focused", "Energetic", "Helpful",
            "Empathetic", "Observant", "Imaginative", "Talkative", "Brave",
            "Disciplined", "Respectful", "Emotional", "Fast Learner", "Competitive"
        ]

        selected = st.multiselect(
            "Select traits that best describe your child",
            trait_options
        )

    
    st.markdown('</div>', unsafe_allow_html=True) # Close the custom div

    st.write("")

    # -------------------------------
    # NAVIGATION
    # -------------------------------
     # ---- BUTTONS OUTSIDE CARD ----
    st.markdown('<div class="bottom-actions">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Back"):
            st.session_state.screen = "india" if country == "India" else "home"
            st.rerun()

    with col2:
        if st.button("Analyze ✨", type="primary"):
            if age >= 3 and not selected:
                st.error("Please select at least one trait.")
            else:
                st.session_state.traits = traits if age < 3 else selected
                st.session_state.screen = "result"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)