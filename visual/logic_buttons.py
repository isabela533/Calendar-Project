import os 
from classes.session import Session 
from classes.gestor_json import DATA_DIR
import os
import json
    
def handle_login(correo):
    if not correo:
        return None, "⚠️ Please enter your email before logging in."

    correo = correo.strip().lower()

    # ── 1. Buscar primero como admin (dueño de su propia agencia) ─────────
    admin_path = os.path.join(DATA_DIR, f"{correo}.json")
    if os.path.exists(admin_path):
        session = Session(correo, role="admin", create=False)
        return session, f"✅ Session started. Welcome back, {correo}!"

    # ── 2. Si no es admin, buscar como operador dentro de otras agencias ──
    if os.path.isdir(DATA_DIR):
        for filename in os.listdir(DATA_DIR):
            if not filename.endswith(".json"):
                continue
            filepath = os.path.join(DATA_DIR, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                continue

            team_access = data.get("team_access", [])
            match = next((op for op in team_access if op["correo"].lower() == correo), None)

            if match:
                owner_correo = filename[:-5]  # quita ".json"
                session = Session(
                    correo,
                    role=match["rol"],
                    owner_correo=owner_correo,
                    create=False,
                    filepath = filepath
                )
                return session, f"✅ Session started. Welcome back, {correo}!"

    # ── 3. No se encontró en ningún lado ───────────────────────────────────
    return None, "ℹ️ Cuenta no encontrada. Por favor cree una"

def handle_signup(correo, money): 
    if not correo: return None, "⚠️ Please enter your email." 

    admin_path = os.path.join(DATA_DIR, f"{correo}.json")
    if os.path.exists(admin_path): 
        session = Session(correo, create=False) 
        return session, "ℹ️ Cuenta ya existente. Inicia sesion" 
    else: 
        session = Session( correo, money=money, resources=[], employees=[], co_requisites=[], exclusions=[], team_access = [], create=True ) 
        return session, "✅ Cuenta creada exitosamente"
    

