import streamlit as st

# Initialize session state variables
if 'text' not in st.session_state:
    st.session_state.text = ""
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = True
if 'temp_text' not in st.session_state:
    st.session_state.temp_text = ""

# Save the text and switch to display mode
def save_text():
    if st.session_state.temp_text.strip() == "":
        st.error("The message cannot be empty. Please enter some text.")
    else:
        st.session_state.text = st.session_state.temp_text
        st.session_state.edit_mode = False

# Hide Streamlit's default header and footer in display mode
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """

# Check if in edit mode
if st.session_state.edit_mode:
    st.header("Let's Focus")
    st.session_state.edit_mode = st.checkbox("Edit Mode", value=True)
elif st.session_state.text.strip() != "":
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Edit mode
if st.session_state.edit_mode:
    st.session_state.temp_text = st.text_area("Add your Focus Message", st.session_state.text, height=200)
    if st.button("Save"):
        save_text()
        st.rerun()  # Rerun to apply state changes

# Display mode
if not st.session_state.edit_mode:
    st.markdown(
        f"<div style='font-size: 36px; height: 100vh; display: flex; align-items: center; justify-content: center; text-align: center;'>{st.session_state.text}</div>",
        unsafe_allow_html=True
    )
    if st.button("Edit Your Message"):
        st.session_state.edit_mode = True
        st.rerun()  # Rerun to apply state changes
