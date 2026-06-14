import streamlit as st
import os
from classes.session import Session
import dashboard as dashboard
import login as login
import ideas as ideas
import signup as signup
import inventory as inventory
import calendario as calendario
import reportes as reportes 
    
st.set_page_config(page_title="AgencePro", page_icon="📅", layout="wide")

# ---------- Estado de navegación ---------- 
if "page" not in st.session_state: 
    st.session_state.page = "login" # página inicial 

if "session" not in st.session_state: 
    st.session_state.session = None 

if "resources" not in st.session_state: 
    st.session_state["resources"] = [] 

if "team" not in st.session_state: 
    st.session_state["team"] = []


# ---------- CSS ----------
# ------ Login ------
st.set_page_config(layout="wide")
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
if st.session_state.page == "login":
    login.show_login()

# ---- Sign up -----            
elif st.session_state.page == "signup": 
    signup.show_signup()

#---- Dashboard ----
elif st.session_state.page == "dashboard":            
    dashboard.show_dashboard()

#----- Inventario ------
elif st.session_state.page == "inventory":
    inventory.show_inventory()

#----- Ideas ------
elif st.session_state.page == "ideas":
    ideas.show_ideas()

elif st.session_state.page == "calendario":
    calendario.show_calendario()

elif st.session_state.page == "reportes":
    reportes.show_reportes()
