import streamlit as st
from datetime import date

def show_dashboard():
    # ── Estilos ────────────────────────────────────────────────────────────
    st.html("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    <style>
      body, [data-testid="stAppViewContainer"] { background: #f7f6f3 !important; }
      .main > div { padding-top: 0 !important; }
      [data-testid="block-container"] { padding: 0 !important; max-width: 100% !important; }
      header[data-testid="stHeader"] { display: none; }

      /* ── Sidebar ── */
    [data-testid="stSidebar"] { 
        background: #1a1a2e !important; 
        min-width: 220px !important; 
        max-width: 400px !important;
        display: block !important;
        visibility: visible !important;
        transform: none !important;
        }
        [data-testid="stSidebar"] > div { padding: 28px 20px !important; }
        [data-testid="stSidebarNav"] { display: none; }

        /* Oculta el botón de colapsar para que no pase de nuevo */
        [data-testid="stSidebarCollapseButton"] { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }

      /* ── Sidebar textos ── */
      .sb-brand { font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 500; color: #f0ede8; margin-bottom: 28px; }
      .sb-brand span { color: #D85A30; }
      .sb-budget { background: rgba(255,255,255,0.07); border: 0.5px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px; margin-bottom: 24px; }
      .sb-budget-label { font-size: 10px; color: #8b8b9e; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 4px; font-family: 'DM Sans', sans-serif; }
      .sb-budget-value { font-size: 22px; font-weight: 500; color: #f0ede8; font-family: 'DM Sans', sans-serif; }
      .sb-nav-label { font-size: 10px; color: #8b8b9e; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; font-family: 'DM Sans', sans-serif; }
      .sb-user { display: flex; align-items: center; gap: 10px; padding-top: 16px; border-top: 0.5px solid rgba(255,255,255,0.08); margin-top: 16px; }
      .sb-avatar { width: 32px; height: 32px; border-radius: 50%; background: #D85A30; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 500; color: #fff; flex-shrink: 0; font-family: 'DM Sans', sans-serif; }
      .sb-user-name { font-size: 12px; color: #f0ede8; font-family: 'DM Sans', sans-serif; }
      .sb-user-sub { font-size: 11px; color: #8b8b9e; font-family: 'DM Sans', sans-serif; }

      /* ── Botones del sidebar ── */
      [data-testid="stSidebar"] [data-testid="stButton"] button {
        width: 100% !important;
        background: transparent !important;
        color: #8b8b9e !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 13px !important;
        font-weight: 400 !important;
        text-align: left !important;
        padding: 9px 10px !important;
        margin-bottom: 2px !important;
      }
      [data-testid="stSidebar"] [data-testid="stButton"] button:hover {
        background: rgba(255,255,255,0.06) !important;
        color: #f0ede8 !important;
      }

      /* ── Topbar ── */
      .topbar {
        background: #ffffff;
        border-bottom: 0.5px solid #e8e8e8;
        padding: 14px 28px;
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
      .topbar-title { font-size: 16px; font-weight: 500; color: #1a1a2e; font-family: 'DM Sans', sans-serif; }

      /* ── Tarjetas de eventos ── */
      .event-card {
        background: #ffffff;
        border: 0.5px solid #e8e8e8;
        border-radius: 10px;
        padding: 16px 18px;
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 10px;
        font-family: 'DM Sans', sans-serif;
      }
      .event-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
      .event-name { font-size: 14px; font-weight: 500; color: #1a1a2e; flex: 1; }
      .event-meta { display: flex; gap: 18px; flex-wrap: wrap; }
      .event-meta-item { font-size: 12px; color: #888; display: flex; align-items: center; gap: 5px; }
      .event-cost { font-size: 13px; font-weight: 500; color: #1a1a2e; min-width: 56px; text-align: right; }

      /* ── Área principal ── */
      .main-content { padding: 20px 28px; }

      /* ── Inputs ── */
      [data-testid="stTextInput"] input {
        font-family: 'DM Sans', sans-serif !important; font-size: 13px !important;
        border: 0.5px solid #e0e0e0 !important; border-radius: 8px !important;
        background: #ffffff !important; color: #1a1a2e !important; box-shadow: none !important;
      }
      [data-testid="stTextInput"] input:focus { border-color: #D85A30 !important; box-shadow: none !important; }
      [data-testid="stTextInput"] label { font-size: 11px !important; font-weight: 500 !important; letter-spacing: 0.06em !important; text-transform: uppercase !important; color: #888 !important; }
      [data-testid="stNumberInput"] input { font-family: 'DM Sans', sans-serif !important; border: 0.5px solid #e0e0e0 !important; border-radius: 8px !important; box-shadow: none !important; }
      [data-testid="stNumberInput"] label { font-size: 11px !important; font-weight: 500 !important; letter-spacing: 0.06em !important; text-transform: uppercase !important; color: #888 !important; }

      /* ── Botones área principal ── */
      /* Botón primario — Guardar / Agregar */
      [data-testid="stMainBlockContainer"] [data-testid="stButton"] button {
        font-family: 'DM Sans', sans-serif !important;
        border-radius: 8px !important;
        font-size: 13px !important;
      }
      button[kind="primaryFormSubmit"],
      [data-testid="stFormSubmitButton"] button {
        background: #1a1a2e !important;
        color: #f0ede8 !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 13px !important;
        font-weight: 500 !important;
      }

      /* Botón eliminar */
      [data-testid="stButton"][data-key^="delete_"] button {
        background: #fff0ec !important;
        color: #D85A30 !important;
        border: none !important;
        border-radius: 8px !important;
        font-size: 15px !important;
        padding: 6px 10px !important;
      }

      /* Botón guardar evento */
      [data-testid="stButton"][data-key="btn_save_event"] button {
        background: #1a1a2e !important;
        color: #f0ede8 !important;
        border: none !important;
        width: 100% !important;
      }

      /* Botón cancelar */
      [data-testid="stButton"][data-key="btn_cancel_event"] button,
      [data-testid="stButton"][data-key="cancel_suggestions"] button {
        background: transparent !important;
        color: #888 !important;
        border: 0.5px solid #d0d0d0 !important;
        width: 100% !important;
      }

      /* ── Expander ── */
      [data-testid="stExpander"] { background: #ffffff !important; border: 0.5px solid #e8e8e8 !important; border-radius: 10px !important; }
      [data-testid="stExpander"] summary { font-family: 'DM Sans', sans-serif !important; font-size: 13px !important; color: #888 !important; }

      /* ── Sugerencias ── */
      .suggestion-card { background: #fff8f5; border: 0.5px solid #D85A30; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #1a1a2e; margin-bottom: 8px; font-family: 'DM Sans', sans-serif; }
    </style>
    """)

    # ── Datos ─────────────────────────────────────────────────────────────
    money   = st.session_state.session.data["money"]
    correo  = st.session_state.get("correo", "usuario@agencia.com")
    initials = correo[:2].upper()
    events  = st.session_state.session.data.get("events", [])
    dot_colors = ["#D85A30", "#7F77DD", "#1D9E75", "#D4537E", "#378ADD", "#BA7517"]

    # ── Sidebar ───────────────────────────────────────────────────────────
    role = getattr(st.session_state.session, "role", "admin")
    with st.sidebar:
        st.markdown("&nbsp;", unsafe_allow_html=True)  # ← fuerza activación
        st.markdown(f"""
        <div class="sb-brand">AgencePro<span>.</span></div>
        ...
        <div class="sb-budget">
            <div class="sb-budget-label">Presupuesto</div>
            <div class="sb-budget-value">${money:,.2f}</div>
        </div>
        <div class="sb-nav-label">Menú</div>
        """, unsafe_allow_html=True)

        if st.button("💻  Eventos", key="btn_nav_eventos"):
            st.session_state.page = "dashboard"
            st.rerun()

        if st.button("📆  Calendario", key="btn_nav_calendario"):
            st.session_state.page = "calendario"
            st.rerun()


        if st.button("💡  Ideas", key="btn_nav_ideas"):
            st.session_state.page = "ideas"
            st.rerun()

        if role == "admin":
            if st.button("📦  Inventario", key="btn_nav_inventory"):
                st.session_state.page = "inventory"
                st.rerun()

            if st.button("📊  Reportes", key="btn_nav_reportes"):
                st.session_state.page = "reportes"
                st.rerun()

        st.markdown(f"""
        <div class="sb-user">
          <div class="sb-avatar">{initials}</div>
          <div>
            <div class="sb-user-name">{correo.split("@")[0]}</div>
            <div class="sb-user-sub">{correo}</div>
            <div class="sb-user-sub">{role}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        
    # ── Topbar ────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="topbar">
      <div class="topbar-title">Eventos Agendados 🗓️</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Contenido ─────────────────────────────────────────────────────────
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    search = st.text_input("", placeholder="🔍  Buscar eventos...", key="search_events", label_visibility="collapsed")

    filtered = [ev for ev in events if search.lower() in ev["name"].lower()] if search else events

    if not filtered:
        st.info("No hay eventos aún. ¡Agrega el primero!")
    else:
        for i, ev in enumerate(filtered):
            resources_str = ", ".join([f"{r[0]} x{r[2]}" for r in ev.get("resources", [])]) or "Sin recursos"
            team_str      = ", ".join([f"{t[0]} x{t[1]}" for t in ev.get("team", [])])      or "Sin equipo"
            dot_color     = dot_colors[i % len(dot_colors)]

            col_card, col_del = st.columns([12, 1])
            with col_card:
                st.markdown(f"""
                <div class="event-card">
                  <div class="event-dot" style="background:{dot_color};"></div>
                  <div class="event-name">{ev['name']}</div>
                  <div class="event-meta">
                    <div class="event-meta-item"><i class="ti ti-calendar"></i> {ev['init']} → {ev['end']}</div>
                    <div class="event-meta-item"><i class="ti ti-package"></i> {resources_str}</div>
                    <div class="event-meta-item"><i class="ti ti-users"></i> {team_str}</div>
                  </div>
                  <div class="event-cost">${float(ev['cost']):,.2f}</div>
                </div>
                """, unsafe_allow_html=True)
            with col_del:
                st.write("")
                if st.button("🗑️", key=f"delete_{ev['name']}_{i}"):
                    try:
                        st.session_state.session.delete_event(ev)
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))

    # ── Nuevo evento ──────────────────────────────────────────────────────
    with st.expander("＋  Agregar nuevo evento"):
        name = st.text_input("Nombre del evento", key="event_name")
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            init = st.date_input("Fecha inicio", key="event_init")
        with col_d2:
            end = st.date_input("Fecha fin", key="event_end")
        cost = st.number_input("Costo ($)", min_value=0.0, step=10.0, key="event_cost")

        st.markdown("**📦 Recursos necesarios**")
        inventario = st.session_state.session.data.get("resources", [])
        opciones_recursos = [f"{r[0]} (disponibles: {r[2]})" for r in inventario if r[3]]

        if opciones_recursos:
            seleccionados_res = st.multiselect(
                "Selecciona recursos del inventario",
                opciones_recursos,
                key="sel_resources"
            )
            cant_res = st.number_input("Cantidad por recurso", min_value=1, step=1, key="cant_res")
            if st.button("Agregar recursos seleccionados", key="btn_add_res"):
                for opcion in seleccionados_res:
                    nombre = opcion.split(" (disponibles:")[0]
                    tipo = next((r[1] for r in inventario if r[0] == nombre), None)
                    entrada = [nombre, tipo, cant_res, True]
                    if entrada not in st.session_state["resources"]:
                        st.session_state["resources"].append(entrada)
                st.rerun()
        else:
            st.info("No hay recursos en inventario. Agrégalos desde Inventario.")

        if st.session_state.get("resources"):
            for r in st.session_state["resources"]:
                disponible = any(inv[0].lower() == r[0].lower() and inv[2] >= r[2] for inv in inventario)
                color = "#1D9E75" if disponible else "#D85A30"
                icono = "✅" if disponible else "⚠️"
                estado = "disponible" if disponible else "insuficiente en inventario"
                st.markdown(
                    f'<div style="background:#f7f6f3; border:0.5px solid #e0e0e0; border-radius:8px; '
                    f'padding:8px 12px; margin-bottom:6px; font-size:13px;">'
                    f'{icono} <b>{r[0]}</b> x{r[2]} <span style="color:{color}; font-size:11px;">— {estado}</span></div>',
                    unsafe_allow_html=True
                )

        st.markdown("**👥 Equipo necesario**")
        empleados = st.session_state.session.data.get("employees", [])
        opciones_equipo = [f"{e[0]} (disponibles: {e[1]})" for e in empleados if e[2]]

        if opciones_equipo:
            seleccionados_eq = st.multiselect(
                "Selecciona roles del equipo",
                opciones_equipo,
                key="sel_team"
            )
            cant_eq = st.number_input("Cantidad por rol", min_value=1, step=1, key="cant_eq")
            if st.button("Agregar equipo seleccionado", key="btn_add_team"):
                for opcion in seleccionados_eq:
                    rol = opcion.split(" (disponibles:")[0]
                    entrada = [rol, cant_eq, True]
                    if entrada not in st.session_state["team"]:
                        st.session_state["team"].append(entrada)
                st.rerun()
        else:
            st.info("No hay empleados en inventario. Agrégalos desde Inventario.")

        if st.session_state.get("team"):
            for t in st.session_state["team"]:
                disponibles_rol = sum(1 for e in empleados if e[0].lower() == t[0].lower())
                tiene = disponibles_rol >= t[1]
                color = "#1D9E75" if tiene else "#D85A30"
                icono = "✅" if tiene else "⚠️"
                estado = f"{disponibles_rol} disponibles" if tiene else f"solo {disponibles_rol} disponibles"
                st.markdown(
                    f'<div style="background:#f7f6f3; border:0.5px solid #e0e0e0; border-radius:8px; '
                    f'padding:8px 12px; margin-bottom:6px; font-size:13px;">'
                    f'{icono} <b>{t[0]}</b> x{t[1]} <span style="color:{color}; font-size:11px;">— {estado}</span></div>',
                    unsafe_allow_html=True
                )

        col_save, col_cancel = st.columns(2)
        with col_save:
            if st.button("Guardar evento", key="btn_save_event"):
                new_event = {
                    "name": name, "init": str(init), "end": str(end),
                    "cost": cost,
                    "resources": st.session_state["resources"],
                    "team": st.session_state["team"]
                }
                try:
                    result = st.session_state.session.add_event(new_event)
                    if result is True:
                        st.session_state["resources"] = []
                        st.session_state["team"] = []
                        st.session_state["event_added"] = True
                        st.rerun()
                    elif isinstance(result, tuple) and result[0] is False:
                        st.session_state["event_suggestions"] = result[1]
                        st.session_state["pending_event"] = new_event
                except Exception as e:
                    st.session_state["event_error"] = str(e)
                    st.session_state["resources"] = []
                    st.session_state["team"] = []
                    st.rerun()

        with col_cancel:
            if st.button("Cancelar", key="btn_cancel_event"):
                st.session_state["resources"] = []
                st.session_state["team"] = []
                st.rerun()

        if st.session_state.get("event_added", False):
            st.success("Evento agregado correctamente.")
            st.session_state["event_added"] = False

        if "event_suggestions" in st.session_state:
            st.warning("⚠️ Esta fecha ya está ocupada. Elige una de estas opciones:")
            for i, (sug_init, sug_end) in enumerate(st.session_state["event_suggestions"], 1):
                st.markdown(f'<div class="suggestion-card"><i class="ti ti-calendar"></i> Opción {i}: {sug_init} → {sug_end}</div>', unsafe_allow_html=True)
                if st.button(f"Usar opción {i}", key=f"suggestion_{i}"):
                    pending = st.session_state.get("pending_event", {})
                    pending["init"], pending["end"] = sug_init, sug_end
                    st.session_state.session.add_event(pending)
                    st.session_state["resources"] = []
                    st.session_state["team"] = []
                    st.session_state["event_added"] = True
                    st.session_state.pop("event_suggestions")
                    st.session_state.pop("pending_event")
                    st.rerun()
            if st.button("Cancelar", key="cancel_suggestions"):
                st.session_state.pop("event_suggestions")
                st.rerun()

        if "event_error" in st.session_state:
            st.error(st.session_state.pop("event_error"))

    st.markdown('</div>', unsafe_allow_html=True)