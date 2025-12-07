import streamlit as st
import time
import logic  # <--- This imports your file from above

# --- 1. VISUAL SETUP (Green & Black Vibe) ---
st.set_page_config(page_title="System Loader", layout="centered")

st.markdown("""
<style>
    /* Force Background Black */
    .stApp { background-color: #000000; }
    
    /* Force Text Green */
    h1, h2, p, div, span {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Hide Streamlit Header/Footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Start Button Style */
    .stButton > button {
        background-color: #000000;
        color: #00FF41;
        border: 2px solid #00FF41;
        font-size: 24px;
        height: 70px;
        width: 100%;
        text-transform: uppercase;
    }
    .stButton > button:hover {
        background-color: #00FF41;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'final_output' not in st.session_state:
    st.session_state.final_output = ""

# --- 3. PAGE LOGIC ---

# === PAGE 1: START BUTTON ===
if st.session_state.page == 'start':
    st.write("##")
    st.markdown("<h1 style='text-align: center;'>SYSTEM READY</h1>", unsafe_allow_html=True)
    st.write("##")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("START SEQUENCE"):
            st.session_state.page = 'running'
            st.rerun()

# === PAGE 2: LOADING BAR (The 1 Minute Timer) ===
elif st.session_state.page == 'running':
    st.write("##")
    st.write("Processing data...")
    
    # Create the Progress Bar
    bar = st.progress(0)
    status_text = st.empty()
    
    # === THE LOOP: Runs for approx 60 seconds ===
    # We loop 60 times, waiting 1 second each time
    for i in range(60):
        # Update bar (math: i / 60 gives percentage)
        bar.progress((i + 1) / 60)
        
        # Optional: Changing text to look busy
        status_text.write(f"Analyzing sector {i+1}/60...")
        
        # Wait 1 second
        time.sleep(1)
        
        # --- TRICK: Run your script near the end ---
        # We run your script at second 58 so it finishes exactly when the bar hits 100%
        if i == 58:
            status_text.write("Finalizing results...")
            st.session_state.final_output = logic.run_my_script()

    # === FINISH ===
    st.session_state.page = 'done'
    st.rerun()

# === PAGE 3: DONE ===
elif st.session_state.page == 'done':
    st.markdown("<h1 style='text-align: center;'>COMPLETE</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Show what your script found
    st.write(st.session_state.final_output)
    
    st.write("##")
    # A text box just because you asked for it
    st.text_input("Enter command:", placeholder="Type here...")
    
    if st.button("RESET"):
        st.session_state.page = 'start'
        st.rerun()
