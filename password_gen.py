import streamlit as st
import secrets
import string

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="SafePass Gen", page_icon="🔐", layout="centered")

# Initialize history and state if they don't exist
if 'history' not in st.session_state:
    st.session_state.history = []
if 'last_password' not in st.session_state:
    st.session_state.last_password = ""

def generate_password(length, use_upper, use_nums, use_syms):
    characters = string.ascii_lowercase
    if use_upper: characters += string.ascii_uppercase
    if use_nums:  characters += string.digits
    if use_syms:  characters += string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# --- 2. SIDEBAR ---
st.sidebar.header("⚙️ Settings")
password_length = st.sidebar.slider("Length", 8, 32, 12)

use_uppercase = st.sidebar.checkbox("Uppercase", value=True)
use_digits = st.sidebar.checkbox("Numbers", value=True)
use_symbols = st.sidebar.checkbox("Symbols", value=True)

# History Section in Sidebar
st.sidebar.divider()
st.sidebar.subheader("🕒 Recent")
if st.session_state.history:
    for p in st.session_state.history:
        st.sidebar.text(p)
    
    if st.sidebar.button("🗑️ Clear History", use_container_width=True):
        st.session_state.history = []
        st.session_state.last_password = ""
        st.rerun()
else:
    st.sidebar.info("No history yet.")

# --- 3. MAIN BODY ---
st.title("🔐 SafePass: Password Generator")
st.write("Generate secure keys with cryptographic standards.")

if st.button("Generate New Password ⚡", type="primary", use_container_width=True):
    new_pass = generate_password(password_length, use_uppercase, use_digits, use_symbols)
    st.session_state.last_password = new_pass
    # Keep only the last 5 entries in history
    st.session_state.history.insert(0, new_pass)
    st.session_state.history = st.session_state.history[:5]

# Show current password if it exists
if st.session_state.last_password:
    st.subheader("Your secure password:")
    st.code(st.session_state.last_password)
    
    # Strength Meter Logic
    score = sum([password_length >= 12, use_uppercase, use_digits, use_symbols])
    
    if score <= 2:
        st.error("Strength: **Weak** ⚠️ (Improve your settings)")
    elif score == 3:
        st.warning("Strength: **Medium** 🆗")
    else:
        st.success("Strength: **Strong** 💪 (NASA Level)")
else:
    st.info("Click the button above to generate your first password.")
