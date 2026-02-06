import streamlit as st

def load_css():
    st.markdown("""
    <style>
    /* =========================
       1. PAGE & ROOT BACKGROUND
       ========================= */

    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap');

    body {
        background-color: #f8f7ff;
        font-family: 'Fredoka', sans-serif;
    }
    
    header[data-testid="stHeader"], 
    div[data-testid="stAppToolbar"] {
        background: transparent !important;
        background-color: transparent !important;
    }

    div[data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #7c3aed 0%, #9333ea 50%, #a855f7 100%) !important;
        background-attachment: fixed !important;
        /* Ensure there is no gap at the very top */
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    # /* Make the header transparent so it doesn't look like a solid block */
    # div[data-testid="stHeader"] {
    #     background: rgba(0,0,0,0) !important;
    #     color: white !important;
    # }

    .stAppToolbar {
        background: transparent !important;
    }
                
   /* =========================
   2. MAIN CONTAINER 
   ========================= */

    .block-container {
        max-width: 1000px !important;
        width: 100% !important;
        /* Increase padding here to push the white card AWAY from the top bar */
        padding-top: 80px;
        padding-bottom: 5rem !important;
        margin: 0 auto !important;
    }
                
    /* =========================
       3. APP HEADER
       ========================= */

    .app-header {
        text-align: center;
        color: white;
        margin-bottom: 0;
        padding: 1.5rem 1rem;
        animation: fadeInDown 0.8s ease-out;
    }

    .app-header h1 {
        font-size: clamp(2.5rem, 6vw, 4rem);
        color: #ffffff !important;
        font-weight: 700;
        margin: 0;
        margin-bottom: 3rem !important;
        letter-spacing: -0.01em;
        text-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    .app-header p {
        font-size: 1.25rem;
        color: rgba(255, 255, 255, 0.85) !important;
        opacity: 0.95;
        margin-top: 0.5rem;
        font-weight: 400;
    }

    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        25% { transform: scale(1.15); }
        50% { transform: scale(1); }
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }

    .splash-emoji {
        font-size: 80px;
        animation: heartbeat 2s ease-in-out infinite;
        margin-bottom: 1rem;
        display: block;
        text-align: center;
    }

    .thinking-emoji {
        font-size: 70px;
        animation: bounce 1.5s ease-in-out infinite;
        margin-bottom: 1rem;
        display: block;
        text-align: center;
    }

    .result-emoji {
        font-size: 60px;
        animation: float 3s ease-in-out infinite;
        margin-bottom: 1rem;
        display: block;
        text-align: center;
    }

    /* =========================
   4. THE CONTENT CARD
   ========================= */
                
    div[data-testid="stVerticalBlock"] {
        background: #fefcf8 !important;
        border-radius: 32px !important; /* This now applies to all 4 corners */
        padding: clamp(2.5rem, 5vw, 4rem) !important;
        box-shadow: 0 20px 60px -10px rgba(0, 0, 0, 0.25) !important;
        max-width: 720px !important;
        width: 95% !important;
        /* Reset margin to let the parent container's padding do the work */
        margin: 0 auto !important; 
    }
                
        /* 🔥 Force readable text INSIDE white card */
    div[data-testid="stVerticalBlock"] h1,
    div[data-testid="stVerticalBlock"] h2,
    div[data-testid="stVerticalBlock"] h3,
    div[data-testid="stVerticalBlock"] p,
    div[data-testid="stVerticalBlock"] label,
    div[data-testid="stVerticalBlock"] span {
        color: #1f2937 !important;
    }


    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* =========================
       5. MODERN WIDGETS
       ========================= */

    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #3730a3;
        margin-bottom: 2rem;
        text-align: center;
    }

    .progress-text {
        font-size: 0.9rem;
        font-weight: 700;
        color: #7c3aed;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        margin-bottom: 0.8rem;
    }

    /* Streamlit Progress Bar */
    div[data-testid="stProgress"] > div > div > div > div {
        background-color: #7c3aed !important;
        height: 12px !important;
        border-radius: 6px !important;
    }

    .question {
        font-size: clamp(1.1rem, 4vw, 1.15rem);
        font-weight: 600;
        color: #374151;
        line-height: 1.5;
        margin-bottom: 1.2rem;
    }

    /* =========================
    MOBILE BUTTON FIX (CRITICAL)
    ========================= */
    @media (max-width: 768px) {

        /* All buttons */
        div.stButton > button {
            width: auto !important;
            min-width: 160px !important;
            padding: 0.8rem 1.2rem !important;
            font-size: 0.95rem !important;
            border-radius: 16px !important;
            margin: 0 auto !important;
            display: block !important;
        }

        /* Back button (secondary) */
        div.stButton > button:not([kind="primary"]) {
            background: #ede9fe !important;
            color: #4c1d95 !important;
            box-shadow: none !important;
            margin-bottom: 1.2rem !important;
        }

        /* Analyze / Primary CTA */
        div.stButton > button[kind="primary"] {
            min-width: 180px !important;
            font-size: 1rem !important;
        }
    }


    /* Radio chips (Modern pill style) */
    .stRadio label {
        background: #f9fafb !important;
        padding: 1rem 1.5rem !important;
        border-radius: 16px !important;
        font-weight: 600 !important;
        border: 2px solid #e5e7eb !important;
        transition: all 0.3s ease !important;
        color: #374151 !important;
        font-size: 1rem !important;
    }

    .stRadio label:hover {
        background: #ede9fe !important;
        color: #7c3aed !important;
    }

    .stRadio div[data-testid="stMarkdownContainer"] p {
        font-weight: 600 !important;
        color: inherit !important; /* Ensure text color is inherited from forced label color */
    }

    /* Active state for radio (Targeting Streamlit's internal selection) */
    div[data-testid="stRadio"] label[data-selected="true"] {
        background: #7c3aed !important;
        color: #ffffff !important; /* Force white text for selected state */
        border-color: #6d28d9 !important;
        box-shadow: 0 10px 20px -5px rgba(124, 58, 237, 0.3) !important;
    }

    /* Selectbox & Sliders */
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 16px !important;
        border: 2px solid #e5e7eb !important;
        background: white !important;
    }

    .stSlider > div > div > div > div {
        background-color: #7c3aed !important;
    }

    /* Date Input */
    .stDateInput input {
        border-radius: 16px !important;
        border: 2px solid #e5e7eb !important;
        background: white !important;
        padding: 0.8rem !important;
    }

    /* Multiselect styling */
    .stMultiSelect div[data-baseweb="select"] {
        border-radius: 16px !important;
        border: 2px solid #e5e7eb !important;
        background: white !important;
    }

    .stMultiSelect span[data-baseweb="tag"] {
        background: #8b5cf6 !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
    }

    /* =========================
       6. RESPONSIVE
       ========================= */

    @media (max-width: 640px) {
        .block-container {
            padding-top: 1rem !important;
            width: 100% !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
                
        }
        
        div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stVerticalBlock"]) {
            padding: 2rem 1.5rem !important;
            border-radius: 24px !important;
        }

        /* Fix column width on mobile */
        div[data-testid="column"] {
            width: 100% !important;
            flex: 1 1 auto !important;
            min-width: 100% !important;
        }
    }
                
 /* =========================================
   FINAL FIX: 2 SQUARES TOP, 1 BAR BOTTOM
   ========================================= */
@media (max-width: 768px) {
    
    /* 1. Remove the empty ghost label box */
    div[data-testid="stRadio"] > label {
        display: none !important;
    }

    /* 2. Container: Allow wrapping so 'Other' can go to the next line */
    div[data-testid="stRadio"] > div {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 10px !important;
        padding-top: 0 !important;
    }

    /* 3. Base style for all boxes */
    .stRadio label {
        background: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 12px !important;
        padding: 15px 5px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        min-height: 80px !important; /* Forces Male/Female to stay same height */
    }

    /* 4. MALE & FEMALE (First two buttons) - 50% width */
    div[data-testid="stRadio"] > div > div:nth-of-type(1),
    div[data-testid="stRadio"] > div > div:nth-of-type(2) {
        flex: 1 1 calc(50% - 10px) !important;
    }

    /* 5. OTHER (Third button) - 100% width */
    div[data-testid="stRadio"] > div > div:nth-of-type(3) {
        flex: 1 1 100% !important;
        min-height: 50px !important; /* Slightly shorter bar for 'Other' */
    }

    /* Hide default radio circles */
    .stRadio input[type="radio"] {
        display: none !important;
    }

    /* Selected State color */
    div[data-testid="stRadio"] label[data-selected="true"] {
        background: #7c3aed !important;
        color: white !important;
        border-color: #6d28d9 !important;
    }
}
        
    </style>
    """, unsafe_allow_html=True)
