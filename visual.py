import streamlit as st
import os
from classes.session import Session

import streamlit as st

st.set_page_config(page_title="AgencePro", page_icon="📅", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background-color: #ffece6;
}

/* Contenedor principal */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* Tarjeta de login */
.login-card {
    background-color: #fff;
    padding: 10rem;
    border-radius: 25px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    text-align: center;
    width: 100%;
}

/* Títulos */
.login-card h1 {
    color: #3d1f1f;
    font-size: 32px;
    margin-bottom: 0.5rem;
}
.login-card p {
    color: #5c3c3c;
    font-size: 18px;
    margin-bottom: 2rem;
}

/* Campo de texto */
div.stTextInput > div > input {
    border: 1px solid #f5b5a3;
    border-radius: 10px;
    padding: 0.6rem;
    width: 100%;
    margin-bottom: 1rem;
}

/* Botón Login */
div.stButton > button:first-child {
    background-color: #f76c4e;
    color: white;
    border: none;
    padding: 0.8rem 2rem;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    margin-bottom: 1rem;
}

/* Botón Google */
div.stButton > button:nth-child(2) {
    background-color: white;
    color: #4285F4;
    border: 2px solid #4285F4;
    padding: 0.8rem 2rem;
    border-radius: 10px;
    font-size: 16px;
    cursor: pointer;
    margin-bottom: 1rem;
}

/* Sign up */
.signup {
    color: #f76c4e;
    font-weight: bold;
    text-decoration: none;
}

/* Social icons */
.social-icons {
    margin-top: 2rem;
    color: #3d1f1f;
    font-size: 18px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- Layout con columnas ----------
col1, col2 = st.columns([2,3])

with col1:
    st.image("assets/fondo.jpg", use_container_width=True)

with col2:
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)
    st.markdown("<h1>Hi! Welcome to <b>AgencePro</b></h1>", unsafe_allow_html=True)
    st.markdown("<p>Manage your marketing agency, simply and elegantly.</p>", unsafe_allow_html=True)

    # Campo de correo
    correo = st.text_input("Enter your email")

    # Botones
    st.button("Login")
    st.button("Login with Google")

    # Sign up
    st.markdown("Don’t have an account? <a href='#' class='signup'>Sign up</a>", unsafe_allow_html=True)

    # Social icons
    st.markdown("<div class='social-icons'>🔗 Facebook | 🐦 Twitter | 💻 GitHub | 📸 Instagram</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
