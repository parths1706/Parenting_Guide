import streamlit as st

def render_traits():
    age = st.session_state.basic_info.get("age", 0)

    st.markdown(
        '<div class="app-header"><h1>Know About Your Child</h1>'
        '<p>Personalized insights for your child\'s growth 💕</p></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<h2 style="text-align: center; color: #3730a3; margin-bottom: 1.5rem;">Characteristics 🌟</h2>',
        unsafe_allow_html=True
    )

    if age < 3:
        st.markdown(
            '<p style="text-align: center; color: #6b7280; margin-bottom: 2rem;">'
            'Your child is very young. At this age, personality is still developing. '
            'We will base the analysis on age, development stage, and cultural insights.'
            '</p>',
            unsafe_allow_html=True
        )
        selected = []
    else:
        st.markdown(
            '<p style="text-align: center; color: #6b7280; margin-bottom: 2rem;">'
            'What makes your child unique? Select traits that best match your child.'
            '</p>',
            unsafe_allow_html=True
        )

        trait_options = [
            "Shy", "Extrovert", "Introvert", "Playful", "Creative",
            "Curious", "Active", "Quiet", "Stubborn", "Sensitive",
            "Social", "Independent", "Focused", "Energetic", "Helpful",
            "Empathetic", "Observant", "Imaginative", "Talkative", "Brave",
            "Disciplined", "Respectful", "Emotional", "Fast Learner", "Competitive"
        ]

        selected = st.multiselect(
            "Select Traits",
            trait_options,
            label_visibility="collapsed"
        )

    st.write("")

    if st.button("← BACK"):
        if st.session_state.basic_info.get("country") == "India":
            st.session_state.screen = "india"
        else:
            st.session_state.screen = "home"
        st.rerun()

    st.write("")

    if st.button("ANALYZE ✨", type="primary"):
        if age >= 3 and not selected:
            st.error("Please select at least one characteristic!")
        else:
            st.session_state.traits = selected
            st.session_state.screen = "result"
            st.rerun()


   
