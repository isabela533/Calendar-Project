import streamlit as st
import os
from classes.session import Session
import logic_buttons
import streamlit as st
    
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
                st.rerun()
        with col2: 
            if "next_page" in st.session_state: 
                st.write("")
                if st.button("Continue", key = "login_button"): 
                    st.session_state.page = st.session_state.next_page 
                    del st.session_state["next_page"]

# ---- Sign up -----            
elif st.session_state.page == "signup": 
    # CSS para centrar el contenido 
    st.markdown(""" 
                <style> 
                .centered-signup 
                { 
                display: flex; 
                flex-direction: column; 
                align-items: center; 
                /* centra horizontal */ 
                justify-content: center; 
                /* centra vertical */
                height: 100vh; 
                /* ocupa toda la altura de la ventana */ 
                width: 100%;
                text-align: center; 
                } 
                </style> 
                """, unsafe_allow_html=True)  
    st.markdown("<div class='.centered-signup'>", unsafe_allow_html=True)
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
        st.write("")
        if st.button("Continue", key = "signupbutton"): 
            st.session_state.page = st.session_state.next_page 
            del st.session_state["next_page"]

#---- Dashboard ----
elif st.session_state.page == "dashboard":            
    st.set_page_config(page_title="Dashboard", layout="wide")

        # ---------- CSS para fondo blanco y centrado ----------
    st.markdown(""" 
                <style> 
                .centered-dashboard
                { 
                display: flex; 
                flex-direction: column; 
                align-items: center; 
                /* centra horizontal */ 
                justify-content: center; 
                /* centra vertical */
                height: 100vh; 
                /* ocupa toda la altura de la ventana */ 
                width: 100%;
                text-align: center; 
                } 
                </style> 
                """, unsafe_allow_html=True)  

    st.markdown("""
    <style>
    body {
        background-color: #fff0e6;
    }
    .title-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
    }
    .title-bar h1 {
        font-size: 36px;
        color: #333;
        margin: 0;
    }
    .subtitle {
        font-size: 18px;
        color: #777;
        margin-top: -5px;
    }
    .inventory-btn {
        font-size: 24px;
        cursor: pointer;
        color: #444;
    }
    .event-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #fafafa;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 0.8rem 1rem;
        margin-bottom: 0.5rem;
    }
    .delete-btn {
        background: none;
        border: none;
        color: #cc0000;
        font-size: 20px;
        cursor: pointer;
    }
    .fab {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #f76c4e;
        color: white;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        font-size: 30px;
        text-align: center;
        line-height: 60px;
        cursor: pointer;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- Título ----------
    # Barra superior con título y botón real
    col1, col2 = st.columns([8,1])  # col1 más grande para el título, col2 pequeña para el botón

    with col1:
        st.markdown("""
        <h1 style="margin-bottom:0;">Agence Pro 📸💡🪙</h1>
        <p class="subtitle">Smart time & resource management for marketing agencies 📅</p>
        """, unsafe_allow_html=True)

    with col2:
        # CSS para que el botón sea solo el emoji, sin fondo
        st.write("")
        st.write("")
        st.write("")
        st.markdown("""
        <style>
        button[data-testid="stButton"] {
            background-color: transparent !important;
            color: black !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
            font-size: 24px !important; /* tamaño del emoji */
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("📦 Inventory", key="inventory_btn"):
            st.session_state.page = "inventory"   # aquí defines la página a la que quieres ir
            st.rerun()

    # ----- Money de la agencia -----
    money = st.session_state.session.data["money"] 
    st.markdown(f"<div class='money-box'>💰 Agency Budget: ${money:,.2f}</div>", unsafe_allow_html=True)
    # ---------- Buscador ----------
    search = st.text_input("🔍 Search events", "")

    events = st.session_state.session.data.get("events", [])
    if search:
        filtered = [ev for ev in events if search.lower() in ev["name"].lower()] 
        if not filtered: 
            st.info("No matching events.") 
        else: 
            for ev in filtered: 
                st.write(f"{ev['name']} | {ev['init']} → {ev['end']} | Cost: {ev['cost']}")
        
    # ---------- Lista de eventos y Eliminar Eventos ----------
    if not events:
        st.info("No events yet. Add your first one!")
    else:
        for ev in events:
            if search.lower() in ev["name"].lower():
                col1, col2 = st.columns([8,1]) 
                # dos columnas: texto y botón 
                with col1:
                    # convertir recursos y team en texto legible
                    resources_str = ", ".join([f"{r[0]} x{r[2]}" for r in ev.get("resources", [])])
                    team_str = ", ".join([f"{t[0]} x{t[1]}" for t in ev.get("team", [])])

                    st.markdown(f"""
                        <div class="event-card" style="border:1px solid #ccc; padding:10px; border-radius:8px; margin-bottom:10px;">
                            <b>{ev['name']}</b><br>
                            💰 Cost: {ev['cost']}<br>
                            📅 {ev['init']} → {ev['end']}<br>
                            📦 Resources: {resources_str if resources_str else "None"}<br>
                            👥 Team: {team_str if team_str else "None"}
                        </div>
                        """, unsafe_allow_html=True)
 
                with col2: 
                    if st.button("🗑️", key=f"delete_{ev['name']}"): 
                        try: 
                            st.session_state.session.delete_event(ev) 
                            st.rerun() 
                        except Exception as e: 
                            st.error(str(e))


    # Formulario para nuevo evento (expander)
    with st.expander("➕ Add new event"):
        name = st.text_input("Event name", key="event_name")
        init = st.date_input("Start date", key="event_init")
        end = st.date_input("End date", key="event_end")
        cost = st.number_input("Cost", min_value=0.0, key="event_cost")

        # --- Recursos --- 
        st.markdown("### 📦 Resources needed") 
        with st.form("add_resources_form", clear_on_submit=True): 
            res_name = st.text_input("Resource name") 
            res_type = None 
            res_cant = st.number_input("Quantity", min_value=1, step=1) 
            res_submit = st.form_submit_button("Add resource") 
            
            if res_submit: 
                st.session_state["resources"].append([res_name, res_type, res_cant, True]) 
                st.success(f"Resource '{res_name}' added ✅") 
                
        # --- Team --- 
        st.markdown("### 👥 Team needed") 
        with st.form("add_team_form", clear_on_submit=True): 
            rol = st.text_input("Role") 
            emp_cant = st.number_input("Number of employees", min_value=1, step=1) 
            team_submit = st.form_submit_button("Add team member") 

            if team_submit: 
                st.session_state["team"].append([rol, emp_cant, True]) 
                st.success(f"Role '{rol}' added ✅")

        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("Save event"):
                new_event = {"name": name, "init": str(init), "end": str(end), "cost": cost, "resources": st.session_state["resources"], "team": st.session_state["team"]}
                try:
                    result = st.session_state.session.add_event(new_event)
                    #Caso 1 -> agregado correctamente 
                    if result is True:
                        st.session_state["event_added"] = True
                        st.rerun()
                    elif isinstance(result,tuple) and result[0] is False:
                        st.session_state["event_suggestions"] = result[1]
                        st.session_state["pending_event"] = new_event
                except Exception as e:
                    st.session_state["event_error"] = str(e) + " Please try again"
                    st.session_state["resources"] = []
                    st.session_state["team"] = [] 
                    st.rerun()
        with col2:
            st.write("")
            if st.button("Cancel"):
                st.session_state["resources"] = []
                st.session_state["team"] = []
                st.session_state.page = "dashboard"
                st.rerun()

                

        # ----- Mostrar mensjaes persistentes ----- 
        if st.session_state.get("event_added", False): 
            st.success("Event added successfully.") 
            st.session_state["event_added"] = False

        if "event_suggestions" in st.session_state:
            suggestions = st.session_state["event_suggestions"]
            st.warning("⚠️ This date is already taken. Choose one of these available slots:")
            for i, (sug_init, sug_end) in enumerate(suggestions, start=1): 
                if st.button(f"Option {i}: {sug_init} → {sug_end}", key=f"suggestion_{i}"): 
                    new_event = st.session_state.get("pending_event", {})
                    if not new_event: 
                        new_event = { 
                            "name": st.session_state.get("event_name", ""), 
                            "init": sug_init, 
                            "end": sug_end, 
                            "cost": st.session_state.get("event_cost", 0.0), 
                            "resources": st.session_state.get("resources", []), 
                            "team": st.session_state.get("team", []) 
                            } 
                    else: 
                        new_event["init"], new_event["end"] = sug_init, sug_end

                    st.session_state.session.add_event(new_event) 
                    st.session_state["event_added"] = True 
                    st.session_state.pop("event_suggestions") 
                    st.session_state.pop("pending_event")
                    st.rerun() 
            if st.button("Cancel", key = "cancel"): 
                st.info("Event creation cancelled.") 
                st.session_state.pop("event_suggestions") 
            
        if "event_error" in st.session_state: 
            st.error(st.session_state["event_error"]) 
            st.session_state.pop("event_error")

#----- Inventario ------
elif st.session_state.page == "inventory":
    st.set_page_config(page_title="Inventory", layout="wide")
    st.markdown(""" 
                <style> 
                .block-container { 
                    padding-top: 80px; /* aumenta el espacio superior */ } 
                </style> """, unsafe_allow_html=True)
    # ---------- Encabezado ---------- 
    st.markdown(""" 
                <h1 style="margin-bottom:0;
                ">Inventory 📋</h1> 
                <p style="color:#777; font-size:16px; margin-top:0;"> 
                Organize your resources and your working team.<br> 
                You can also add restrictions on your resources for better care and management. 
                </p> 
                """, unsafe_allow_html=True)
    # ---------- Pestañas estilo navegador ---------- 
    tabs = st.tabs(["📦 Resources", "👥 Work Team", "⚖️ Restrictions"])
    # Recursos
    with tabs[0]: 
        st.subheader("Resources list") 
        resources = st.session_state.session.data.get("resources", []) 
        if not resources: 
            st.info("No resources yet. Add your first one!") 
        else: 
            for r in resources:
                name, type_, quantity, dispo = r
                col1, col2, col3, col4 = st.columns([8,0.4,0.4,0.4])
                with col1: 
                    st.markdown(f""" 
                                <div style="padding:0.5rem; border:1px solid #ddd; border-radius:8px; background:#fafafa;"> 
                                <b>{name}</b><br> 
                                Type: {type_}<br> 
                                Quantity: {quantity}<br>
                                Dispo: {dispo}
                                </div> 
                                """, unsafe_allow_html=True)
                with col2: 
                    if st.button("➕", key=f"inc_{name}"): 
                        try:
                            st.session_state.session.add_resources([[name, type_, 1, dispo]]) 
                            st.rerun() 
                        except Exception as e: 
                            st.error(str(e))         
                with col3: 
                    if st.button("➖", key=f"dec_{name}"): 
                        try: 
                            st.session_state.session.remove_resources([[name, type_, 1, dispo]]) 
                            st.rerun() 
                        except Exception as e: 
                            st.error(str(e))
                with col4: 
                    if st.button("🗑️", key=f"del_{name}"): 
                        try:
                            st.session_state.session.remove_resources([[name, type_, quantity, dispo]]) 
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))
                            
        with st.expander("➕ Add new resource"): 
            name = st.text_input("Resource name") 
            type_ = st.text_input("Type") 
            quantity = st.number_input("Quantity", min_value=1, step=1, key="team_quantity") 
            availability = True
            if st.button("Save resource"): 
                new_resource = [[name, type_, quantity, availability]]
                try: 
                    st.session_state.session.add_resources(new_resource)  
                    st.rerun() 
                except Exception as e: 
                    st.error(str(e))  
    # WorkTeam 
    with tabs[1]:
        st.subheader("Work Team List")
        team = st.session_state.session.data.get("employees", []) 
        if not team: 
            st.info("No team members yet. Add your first one!") 
        else: 
            for i, emp in enumerate(team):
                rol, quantity, dispo = emp
                col1, col2, col3, col4 = st.columns([8,0.4,0.4,0.4])
                with col1:
                    st.markdown(f""" 
                                <div style="padding:0.5rem; border:1px solid #ddd; border-radius:8px; background:#fafafa;"> 
                                <b>{rol}</b><br>  
                                Quantity: {quantity}<br>
                                Dispo: {dispo} 
                                </div> 
                                """, unsafe_allow_html=True)
                with col2: 
                    if st.button("➕", key=f"inc_{rol}_{i}"): 
                        try:
                            st.session_state.session.add_employee([[rol, 1, dispo]]) 
                            st.rerun() 
                        except Exception as e: 
                            st.error(str(e))         
                with col3: 
                    if st.button("➖", key=f"dec_{rol}_{i}"): 
                        try: 
                            st.session_state.session.remove_employee([[rol, 1, dispo]]) 
                            st.rerun() 
                        except Exception as e: 
                            st.error(str(e))
    
                with col4: 
                    if st.button("🗑️", key=f"del_{rol}_{i}"): 
                        try:
                            st.session_state.session.remove_employee([[rol, quantity, dispo]]) 
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))
        #Botones de agregar empleados 
        
        with st.expander("➕ Add a new role"): 
            rol = st.text_input("Role name")  
            cant = st.number_input("Quantity", min_value=1, step=1, key="employee_quantity") 
            dispo = True
            if st.button("Save new role"): 
                new_resource = [[rol, cant, dispo]]
                try: 
                    st.session_state.session.add_employee(new_resource)  
                    st.rerun() 
                except Exception as e: 
                    st.error(str(e))  
    # Restrictions
    with tabs[2]:
        st.subheader("Restrictions list")

        co_requisites = st.session_state.session.data.get("co_requisites", {})
        exclusions = st.session_state.session.data.get("exclusions", [])

        if not co_requisites and not exclusions:
            st.info("No restrictions defined.")
        
        st.markdown("### 🔗 Co‑requisites")
        if co_requisites:
            for resource, deps in co_requisites.items():
                for dep in deps:
                    col1, col2 = st.columns([8,0.5])
                    with col1:
                        st.write(f"- {resource} depends on {dep}")
                    with col2:
                        if st.button("🗑️", key=f"del_coreq_{resource}_{dep}"):
                            try:
                                st.session_state.session.remove_co_rq(resource, [dep])
                                st.rerun()
                            except Exception as e:
                                st.error(str(e))

        with st.expander("➕ Add new co-requisite"):
            resource = st.text_input("Name the resource or role that has dependency")
            deps_text = st.text_input("Dependencies (comma separated)")
            if st.button("Save co-requisite"):
                dependencia = [d.strip() for d in deps_text.split(",") if d.strip()]
                try:
                    st.session_state.session.add_co_rq(resource, dependencia)
                    st.success("Co-requisite added successfully.")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))
                                        
        # Mostrar exclusiones
        if exclusions:
            st.markdown("### 🚫 Exclusions")
            for r1, r2 in exclusions:   # aquí cada elemento es una lista [r1, r2]
                    col1,col2 = st.columns([8,0.5])
                    with col1:
                        st.write(f"- {r1} cannot be used with {r2}")
                    with col2:
                        if st.button("🗑️", key=f"del_excl_{r1}_{r2}"): 
                            try: 
                                st.session_state.session.remove_exclusion(r1, r2) 
                                st.rerun() 
                            except Exception as e: 
                                st.error(str(e))

        # Formulario para agregar nueva exclusión 
        with st.expander("➕ Add new exclusion"): 
            r1 = st.text_input("First resource") 
            r2 = st.text_input("Second resource") 
            if st.button("Save exclusion"): 
                try: # cada exclusión es una lista [r1, r2] 
                    st.session_state.session.add_exclusion(r1, r2) 
                    st.success(f"Exclusion added: {r1} cannot be used with {r2}") 
                    st.rerun() 
                except Exception as e: st.error(str(e))


    # ---------- Botón inferior izquierdo para volver al dashboard ----------
    st.markdown("""
    <style>
    .back-btn {
        position: fixed;
        bottom: 30px;
        left: 30px;
        background-color: #4e79f7;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 20px;
        font-size: 16px;
        cursor: pointer;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .back-btn:hover {
        background-color: #365ac9;
    }
    </style>
    """, unsafe_allow_html=True)

    if st.button("⬅️ Back to Dashboard", key="back_dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()



