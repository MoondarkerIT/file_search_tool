import streamlit as st
import tokengrabber

st.title("Automatic File Searcher")

st.write("Script is running...")

# --- THE MAGIC ---
# We just call the function directly. 
# No "if st.button():" check is needed.
results = tokengrabber.main() 
# -----------------

if results:
    st.success("Files Found!")
    st.write("successfully grabbed the following files")
else:
    st.warning("No files found yet.")