import streamlit as st
import time

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="NetSearch Protocol", layout="centered")

# --- 2. CSS STYLING (The Matrix/Hacker Vibe) ---
st.markdown("""
<style>
    /* Force Background to Black */
    .stApp {
        background-color: #000000;
    }
    
    /* Force Text to Green */
    h1, h2, h3, p, div, span {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Style the Buttons */
    .stButton > button {
        background-color: #000000;
        color: #00FF41;
        border: 2px solid #00FF41;
        border-radius: 0px;
        font-size: 20px;
        font-weight: bold;
        width: 100%;
        height: 60px;
    }
    .stButton > button:hover {
        background-color: #00FF41;
        color: #000000;
    }
    
    /* Style the Text Input Box */
    .stTextInput > div > div > input {
        color: #00FF41;
        background-color: #111111;
        border: 1px solid #00FF41;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = 'start'

# --- 4. APP LOGIC ---

# === SCREEN 1: START MENU ===
if st.session_state.page == 'start':
    st.write("##")
    st.write("##")
    
    # We use HTML directly to ensure the color works
    st.markdown("<h1 style='text-align: center; color: #00FF41;'>SYSTEM ACCESS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00FF41;'>SECURE TERMINAL V1.0</p>", unsafe_allow_html=True)
    
    st.write("##")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("INITIALIZE"):
            st.session_state.page = 'loading'
            st.rerun()

# === SCREEN 2: FAKE LOADING ===
elif st.session_state.page == 'loading':
    st.write("##")
    
    msg_placeholder = st.empty()
    bar = st.progress(0)
    
    # The Loading Steps
    steps = [
        "ESTABLISHING UPLINK...",
        "BYPASSING FIREWALL...",
        "DECRYPTING PACKETS...",
        "SEARCHING DATABASE...",
        "ACCESS GRANTED."
    ]
    
    for i, step in enumerate(steps):
        # Update text
        msg_placeholder.markdown(f"**> {step}**")
        
        # Update bar
        bar.progress((i + 1) * 20)
        
        # Speed of animation
        time.sleep(1.0)
        
    st.session_state.page = 'finished'
    st.rerun()

# === SCREEN 3: DONE + INPUT ===
elif st.session_state.page == 'finished':
    st.markdown("<h1 style='text-align: center; color: #00FF41;'>PROCESS COMPLETE</h1>", unsafe_allow_html=True)
    st.write("---")
    
    user_input = st.text_input("ENTER COMMAND:", placeholder="Type filename here...")
    
    st.write("##")
    if st.button("RESET SYSTEM"):
        st.session_state.page = 'start'
        st.rerun()
