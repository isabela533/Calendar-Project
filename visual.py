import streamlit as st
import os
from classes.session import Session
import logic_buttons
import streamlit as st
    
st.set_page_config(page_title="AgencePro", page_icon="📅", layout="wide")

# ---------- Estado de navegación ---------- 
if "page" not in st.session_state: 
    st.session_state.page = "login" # página inicial 


# ---------- CSS ----------
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
col1, col2 = st.columns([3,4])

with col1:
    st.write("")
    st.write("")
    st.write("")
   
    st.image("assets/fondo.jpg", use_container_width=True)

with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<div class='centered-col'>", unsafe_allow_html=True)
    st.write("") # espacio vacío 
    
    if st.session_state.page == "login":
        st.markdown("<h1>Hi! Welcome to <b>AgencePro</b></h1>", unsafe_allow_html=True)
        st.markdown("<p>Manage your marketing agency, simply and elegantly.</p>", unsafe_allow_html=True)

        # Campo de correo
        correo = st.text_input("Enter your email", key = "email")
        # Botones
        
        # open new pages _ logic buttons 
        if st.button("Login"): 
            session, msg = logic_buttons.handle_login(correo) 
            st.info(msg) 
            if session: 
                st.session_state.session = session 
                st.session_state.next_page = "dashboard" 
            else: # si no existe cuenta, pasamos a signup 
                st.session_state.next_page = "signup"  
                
        
        # Sign up
        st.markdown("Don’t have an account?", unsafe_allow_html=True)
        
        # fila con Sign Up y Continue juntos 
        col1, col2 = st.columns([2,2]) 
        with col1: 
            if st.button("Sign Up"): 
                st.session_state.page = "signup" 
        with col2: 
            if "next_page" in st.session_state: 
                if st.button("Continue", key = "login_button"): 
                    st.session_state.page = st.session_state.next_page 
                    del st.session_state["next_page"]
            
    elif st.session_state.page == "signup":            
            st.markdown("<h2>Create Account</h2>", unsafe_allow_html=True)
            
            correo = st.text_input("Enter your email", key="signup_email")
            money = st.number_input("💰 Initial budget", min_value=0.0, step=100.0, key="signup_budget")
            
            if st.button("Create account"): 
                session, msg = logic_buttons.handle_signup(correo, money) 
                st.info(msg) 
                if session: 
                    st.session_state.session = session 
                    st.session_state.next_page = "dashboard"

            if "next_page" in st.session_state: 
                if st.button("Continue", key = "signupbutton"): 
                    st.session_state.page = st.session_state.next_page 
                    del st.session_state["next_page"]

    elif st.session_state.page == "dashboard":            
            st.title("DashBoard")
            if "session" in st.session_state: 
                st.write(f"Active session: {st.session_state.session.correo}")
    

    st.markdown("</div>", unsafe_allow_html=True)