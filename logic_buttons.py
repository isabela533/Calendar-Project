import os 
from classes.session import Session 
import streamlit as st

def handle_login(correo): 
    if not correo: 
        return None, "⚠️ Please enter your email before logging in." 
    if os.path.exists(f"data/{correo}.json"): 
        session = Session(correo, create=False) 
        return session, f"✅ Session started. Welcome back, {correo}!" 
    else: 
        return None, "ℹ️ No account found. Please create one:" 
    
def handle_signup(correo, money): 
    if not correo: return None, "⚠️ Please enter your email." 
    if os.path.exists(f"data/{correo}.json"): 
        session = Session(correo, create=False) 
        return session, "ℹ️ Account already exists. Opening dashboard..." 
    else: 
        session = Session( correo, money=money, resources=[], employees=[], co_requisites=[], exclusions=[], create=True ) 
        return session, "✅ Account created successfully."
