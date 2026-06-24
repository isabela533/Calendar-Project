import streamlit as st
from datetime import date
from fechas_clave import get_fechas_clave, get_proximas, TIPO_COLORES
from datetime import date as date_type

def show_ideas():

    st.html("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    <style>
      body, [data-testid="stAppViewContainer"] { background: #f7f6f3 !important; }
      .main > div { padding-top: 0 !important; }
      [data-testid="block-container"] { padding: 0 !important; max-width: 100% !important; }
      header[data-testid="stHeader"] { display: none; }

      [data-testid="stSidebar"] { background: #1a1a2e !important; min-width: 220px !important; max-width: 400px !important; display: block !important; visibility: visible !important; transform: none !important; }
      [data-testid="stSidebar"] > div { padding: 28px 20px !important; }
      [data-testid="stSidebarNav"] { display: none; }
      [data-testid="stSidebarCollapseButton"] { display: none !important; }
      [data-testid="collapsedControl"] { display: none !important; }

      .sb-brand { font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 500; color: #f0ede8; margin-bottom: 28px; }
      .sb-brand span { color: #D85A30; }
      .sb-nav-label { font-size: 10px; color: #8b8b9e; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; font-family: 'DM Sans', sans-serif; }
      .sb-user { display: flex; align-items: center; gap: 10px; padding-top: 16px; border-top: 0.5px solid rgba(255,255,255,0.08); margin-top: 16px; }
      .sb-avatar { width: 32px; height: 32px; border-radius: 50%; background: #D85A30; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 500; color: #fff; flex-shrink: 0; }
      .sb-user-name { font-size: 12px; color: #f0ede8; font-family: 'DM Sans', sans-serif; }
      .sb-user-sub { font-size: 11px; color: #8b8b9e; font-family: 'DM Sans', sans-serif; }

      [data-testid="stSidebar"] [data-testid="stButton"] button {
        width: 100% !important; background: transparent !important; color: #8b8b9e !important;
        border: none !important; border-radius: 8px !important; font-family: 'DM Sans', sans-serif !important;
        font-size: 13px !important; font-weight: 400 !important; text-align: left !important;
        padding: 9px 10px !important; margin-bottom: 2px !important;
      }
      [data-testid="stSidebar"] [data-testid="stButton"] button:hover { background: rgba(255,255,255,0.06) !important; color: #f0ede8 !important; }
      [data-testid="stSidebar"] [data-testid="stMetric"] { background: rgba(255,255,255,0.07) !important; border: 0.5px solid rgba(255,255,255,0.1) !important; border-radius: 10px !important; padding: 14px !important; margin-bottom: 24px !important; }
      [data-testid="stSidebar"] [data-testid="stMetricLabel"] p { color: #8b8b9e !important; font-size: 10px !important; text-transform: uppercase !important; letter-spacing: 0.08em !important; }
      [data-testid="stSidebar"] [data-testid="stMetricValue"] { color: #f0ede8 !important; font-size: 22px !important; }

      .topbar { background: #ffffff; border-bottom: 0.5px solid #e8e8e8; padding: 14px 28px; display: flex; align-items: center; justify-content: space-between; }
      .topbar-title { font-size: 16px; font-weight: 500; color: #1a1a2e; font-family: 'DM Sans', sans-serif; }
      .main-content { padding: 20px 28px; }

      /* Tarjeta de fecha próxima */
      .prox-card {
        background: #ffffff; border: 0.5px solid #e8e8e8; border-radius: 10px;
        padding: 16px 18px; margin-bottom: 10px; font-family: 'DM Sans', sans-serif;
        display: flex; align-items: center; gap: 14px;
      }
      .prox-emoji { font-size: 24px; flex-shrink: 0; }
      .prox-info { flex: 1; }
      .prox-nombre { font-size: 14px; font-weight: 500; color: #1a1a2e; }
      .prox-desc { font-size: 12px; color: #888; margin-top: 2px; }
      .prox-fecha { font-size: 12px; color: #888; text-align: right; }
      .prox-dias { font-size: 18px; font-weight: 500; text-align: right; }
      .tipo-badge {
        display: inline-block; padding: 3px 10px; border-radius: 20px;
        font-size: 11px; font-weight: 500; margin-top: 4px; font-family: 'DM Sans', sans-serif;
      }

      /* Tarjeta de mes completo */
      .mes-card {
        background: #ffffff; border: 0.5px solid #e8e8e8; border-radius: 10px;
        padding: 16px 18px; margin-bottom: 8px; font-family: 'DM Sans', sans-serif;
        display: flex; align-items: center; gap: 14px;
      }
      .mes-emoji { font-size: 20px; flex-shrink: 0; width: 30px; text-align: center; }
      .mes-nombre { font-size: 13px; font-weight: 500; color: #1a1a2e; flex: 1; }
      .mes-fecha-str { font-size: 12px; color: #aaa; min-width: 90px; text-align: right; }

      [data-testid="stButton"][data-key^="agendar_"] button {
        background: #D85A30 !important; color: #fff !important;
        border: none !important; border-radius: 8px !important;
        font-size: 12px !important; font-weight: 500 !important;
        padding: 6px 14px !important; white-space: nowrap !important;
      }

      [data-testid="stTextInput"] input { font-family: 'DM Sans', sans-serif !important; font-size: 13px !important; border: 0.5px solid #e0e0e0 !important; border-radius: 8px !important; box-shadow: none !important; }
      [data-testid="stTextInput"] input:focus { border-color: #D85A30 !important; box-shadow: none !important; }
      [data-testid="stSelectbox"] { font-family: 'DM Sans', sans-serif !important; }
    </style>
    """)

    # ── Datos ─────────────────────────────────────────────────────────────
    money    = st.session_state.session.data["money"]
    correo   = st.session_state.get("correo", "usuario@agencia.com")
    initials = correo[:2].upper()
    year     = date.today().year
    todas    = get_fechas_clave(year)
    proximas = get_proximas(todas, dias=60)

    MESES = ["Todos", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    # ── Sidebar ───────────────────────────────────────────────────────────
    role = getattr(st.session_state.session, "role", "admin")
    with st.sidebar:
        st.markdown("&nbsp;", unsafe_allow_html=True)
        st.markdown('<div class="sb-brand">AgencePro<span>.</span></div>', unsafe_allow_html=True)
        st.metric(label="Presupuesto", value=f"${money:,.2f}")
        st.markdown('<div class="sb-nav-label">Menú</div>', unsafe_allow_html=True)

        if st.button("🗓️  Eventos", key="btn_nav_eventos"):
            st.session_state.page = "dashboard"
            st.rerun()


        if st.button("💡  Ideas", key="btn_nav_ideas"):
            st.session_state.page = "ideas"
            st.rerun()

        if role == "admin":
            if st.button("📦  Inventario", key="btn_nav_inventory"):
                st.session_state.page = "inventory"
                st.rerun()

        st.markdown(f"""
        <div class="sb-user">
          <div class="sb-avatar">{initials}</div>
          <div>
            <div class="sb-user-name">{correo.split("@")[0]}</div>
            <div class="sb-user-sub">{correo}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Topbar ────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="topbar">
      <div class="topbar-title">💡 Ideas estratégicas</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # ── Próximas oportunidades ────────────────────────────────────────────
    if proximas:
        st.markdown("### Oportunidades en los próximos 60 días")
        for f in proximas:
            dias_restantes = (f["fecha"] - date.today()).days
            color = TIPO_COLORES.get(f["tipo"], "#888")
            col_info, col_btn = st.columns([5, 1])
            with col_info:
                st.markdown(f"""
                <div class="prox-card">
                  <div class="prox-emoji">{f['emoji']}</div>
                  <div class="prox-info">
                    <div class="prox-nombre">{f['nombre']}</div>
                    <div class="prox-desc">{f['desc']}</div>
                    <span class="tipo-badge" style="background:{color}22; color:{color};">{f['tipo']}</span>
                  </div>
                  <div>
                    <div class="prox-dias" style="color:{color};">{dias_restantes}d</div>
                    <div class="prox-fecha">{f['fecha'].strftime('%d %b')}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            with col_btn:
                st.write("")
                st.write("")
                if st.button("＋ Agendar", key=f"agendar_{f['nombre']}"):
                    st.session_state["prefill_event_name"] = f['nombre']
                    st.session_state["prefill_event_date"] = f['fecha']
                    st.session_state["abrir_expander"] = True

    # ── Todas las fechas por mes ───────────────────────────────────────────
    st.markdown("### Calendario completo del año")

    mes_sel = st.selectbox("Filtrar por mes", MESES, key="filtro_mes")
    buscar  = st.text_input("", placeholder="🔍  Buscar fecha clave...", key="buscar_idea", label_visibility="collapsed")

    filtradas = todas
    if mes_sel != "Todos":
        num_mes = MESES.index(mes_sel)
        filtradas = [f for f in filtradas if f["fecha"].month == num_mes]
    if buscar:
        filtradas = [f for f in filtradas if buscar.lower() in f["nombre"].lower()]

    for f in filtradas:
        color = TIPO_COLORES.get(f["tipo"], "#888")
        col_card, col_btn = st.columns([5, 1])
        with col_card:
            st.markdown(f"""
            <div class="mes-card">
              <div class="mes-emoji">{f['emoji']}</div>
              <div class="mes-nombre">
                {f['nombre']}
                <span class="tipo-badge" style="background:{color}22; color:{color}; margin-left:8px;">{f['tipo']}</span>
                <div style="font-size:12px; color:#aaa; margin-top:2px;">{f['desc']}</div>
              </div>
              <div class="mes-fecha-str">{f['fecha'].strftime('%d %b %Y')}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_btn:
            st.write("")
            if st.button("＋ Agendar", key=f"agendar_all_{f['nombre']}_{f['fecha']}"):
                st.session_state["prefill_event_name"] = f['nombre']
                st.session_state["prefill_event_date"] = f['fecha']
                st.session_state["abrir_expander"] = True

  # ── Formulario nuevo evento ───────────────────────────────────────────
    prefill_name = st.session_state.get("prefill_event_name", "")
    prefill_date = st.session_state.get("prefill_event_date", date.today())
    abrir        = st.session_state.get("abrir_expander", False)

    # Keys dinámicos — cambian cuando cambia la fecha/nombre elegido
    # Esto fuerza a Streamlit a recrear el widget con el nuevo value
    date_key = f"idea_init_{prefill_date}"
    end_key  = f"idea_end_{prefill_date}"
    name_key = f"idea_name_{prefill_name.replace(' ', '_')}"

    with st.expander("＋  Agendar evento", expanded=abrir):

        name = st.text_input("Nombre del evento", value=prefill_name, key=name_key)

        col_d1, col_d2 = st.columns(2)
        with col_d1:
            init = st.date_input("Fecha inicio", value=prefill_date, key=date_key)
        with col_d2:
            end = st.date_input("Fecha fin", value=prefill_date, key=end_key)

        # ... resto igual sin cambiar nada
        cost = st.number_input("Costo ($)", min_value=0.0, step=10.0, key="idea_event_cost")

        # ── Recursos ──────────────────────────────────────────────────────
        inventario = st.session_state.session.data.get("resources", [])
        empleados  = st.session_state.session.data.get("employees", [])

        st.markdown("**📦 Recursos necesarios**")
        opciones_recursos = [f"{r[0]} (disponibles: {r[2]})" for r in inventario if r[3]]

        if opciones_recursos:
            seleccionados_res = st.multiselect(
                "Selecciona recursos del inventario",
                opciones_recursos,
                key="idea_sel_resources"
            )
            cant_res = st.number_input("Cantidad por recurso", min_value=1, step=1, key="idea_cant_res")
            if st.button("Agregar recursos seleccionados", key="idea_btn_add_res"):
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
                    f'{icono} <b>{r[0]}</b> x{r[2]} '
                    f'<span style="color:{color}; font-size:11px;">— {estado}</span></div>',
                    unsafe_allow_html=True
                )

        st.markdown("**👥 Equipo necesario**")
        opciones_equipo = [f"{e[0]} (disponibles: {e[1]})" for e in empleados if e[2]]

        if opciones_equipo:
            seleccionados_eq = st.multiselect(
                "Selecciona roles del equipo",
                opciones_equipo,
                key="idea_sel_team"
            )
            cant_eq = st.number_input("Cantidad por rol", min_value=1, step=1, key="idea_cant_eq")
            if st.button("Agregar equipo seleccionado", key="idea_btn_add_team"):
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
                    f'{icono} <b>{t[0]}</b> x{t[1]} '
                    f'<span style="color:{color}; font-size:11px;">— {estado}</span></div>',
                    unsafe_allow_html=True
                )

        # ── Guardar / Cancelar ────────────────────────────────────────────
        col_save, col_cancel = st.columns(2)
        with col_save:
            if st.button("Guardar evento", key="idea_btn_save"):
                if not name:
                    st.warning("Por favor ingresa un nombre para el evento.")
                else:
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
                            st.session_state["idea_event_added"] = True
                            st.session_state.pop("prefill_event_name", None)
                            st.session_state.pop("prefill_event_date", None)
                            st.session_state.pop("abrir_expander", None)
                            st.rerun()
                        elif isinstance(result, tuple) and result[0] is False:
                            st.session_state["event_suggestions"] = result[1]
                            st.session_state["pending_event"] = new_event
                    except Exception as e:
                        st.error(str(e))
                        st.session_state["resources"] = []
                        st.session_state["team"] = []
                        st.rerun()

        with col_cancel:
            if st.button("Cancelar", key="idea_btn_cancel"):
                st.session_state["resources"] = []
                st.session_state["team"] = []
                st.rerun()

        # ── Mensajes ──────────────────────────────────────────────────────
        if st.session_state.pop("idea_event_added", False):
            st.success("¡Evento agendado correctamente! Ya aparece en tu dashboard.")

        if "event_suggestions" in st.session_state:
            st.warning("⚠️ Esta fecha ya está ocupada. Elige una opción:")
            for i, (sug_init, sug_end) in enumerate(st.session_state["event_suggestions"], 1):
                st.markdown(
                    f'<div style="background:#fff8f5; border:0.5px solid #D85A30; border-radius:8px; '
                    f'padding:10px 14px; font-size:13px; margin-bottom:8px;">'
                    f'📅 Opción {i}: {sug_init} → {sug_end}</div>',
                    unsafe_allow_html=True
                )
                if st.button(f"Usar opción {i}", key=f"idea_sug_{i}"):
                    pending = st.session_state.get("pending_event", {})
                    pending["init"], pending["end"] = sug_init, sug_end
                    st.session_state.session.add_event(pending)
                    st.session_state["resources"] = []
                    st.session_state["team"] = []
                    st.session_state.pop("event_suggestions", None)
                    st.session_state.pop("pending_event", None)
                    st.session_state["idea_event_added"] = True
                    st.rerun()
            if st.button("Cancelar", key="idea_cancel_sug"):
                st.session_state.pop("event_suggestions", None)
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)