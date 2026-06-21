import os 
from classes.session import Session 
from classes.gestor_json import DATA_DIR
import os

def handle_login(correo): 
    if not correo: 
        return None, "⚠️ Please enter your email before logging in." 
    path = os.path.join(DATA_DIR, f"{correo}.json")
    if os.path.exists(path): 
        session = Session(correo, create=False) 
        return session, f"✅ Session started. Welcome back, {correo}!" 
    else: 
        return None, "ℹ️ Cuenta no encontrada. Por favor cree una" 
    
def handle_signup(correo, money): 
    if not correo: return None, "⚠️ Please enter your email." 
    path = os.path.join(DATA_DIR, f"{correo}.json")
    if os.path.exists(path): 
        session = Session(correo, create=False) 
        return session, "ℹ️ Cuenta ya existente. Inicia sesion" 
    else: 
        session = Session( correo, money=money, resources=[], employees=[], co_requisites=[], exclusions=[], create=True ) 
        return session, "✅ Cuenta creada exitosamente"
