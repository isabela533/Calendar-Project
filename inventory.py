import streamlit as st

def show_inventory():

    st.html("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    <style>
      body, [data-testid="stAppViewContainer"] { background: #f7f6f3 !important; }
      .main > div { padding-top: 0 !important; }
      [data-testid="block-container"] { padding: 0 !important; max-width: 100% !important; }
      header[data-testid="stHeader"] { display: none; }
      [data-testid="stSidebar"] { display: none !important; }
        

    /* ── Topbar — ahora apunta solo al contenedor con key="topbar" ── */
        .st-key-topbar [data-testid="stHorizontalBlock"] {
        background: #1a1a2e !important;
        padding: 10px 28px !important;
        align-items: center !important;
        gap: 8px !important;
        }

        /* Botones de la topbar */
        .st-key-topbar [data-testid="stButton"] button {
        background: transparent !important;
        color: #8b8b9e !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 13px !important;
        font-weight: 400 !important;
        padding: 7px 14px !important;
        width: 100% !important;
        }
        .st-key-topbar [data-testid="stButton"] button:hover {
        background: rgba(255,255,255,0.06) !important;
        color: #f0ede8 !important;
        }

      /* Botón activo — Inventario */
      [data-testid="stButton"][data-key="btn_nav_inv"] button {
        background: rgba(216,90,48,0.18) !important;
        color: #D85A30 !important;
        font-weight: 500 !important;
      }

      /* Botón volver */
      [data-testid="stButton"][data-key="btn_back"] button {
        color: #8b8b9e !important;
        border: 0.5px solid rgba(255,255,255,0.2) !important;
        font-size: 12px !important;
      }

      /* ── Tabs nativos ── */
      [data-testid="stTabs"] { background: #ffffff; border-bottom: 0.5px solid #e8e8e8; padding: 0 10px; }
      [data-testid="stTabs"] button { font-family: 'DM Sans', sans-serif !important; font-size: 13px !important; }
      [data-testid="stTabs"] [aria-selected="true"] { color: #D85A30 !important; border-bottom-color: #D85A30 !important; }

      /* ── Tarjetas ── */
      .res-card { background: #ffffff; border: 0.5px solid #e8e8e8; border-radius: 10px; padding: 14px 18px; display: flex; align-items: center; gap: 14px; margin-bottom: 8px; font-family: 'DM Sans', sans-serif; }
      .res-icon { width: 36px; height: 36px; border-radius: 8px; background: rgba(216,90,48,0.1); display: flex; align-items: center; justify-content: center; color: #D85A30; font-size: 18px; flex-shrink: 0; }
      .res-name { font-size: 14px; font-weight: 500; color: #1a1a2e; }
      .res-meta { font-size: 12px; color: #888; margin-top: 2px; }
      .res-badge-ok { display: inline-block; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 500; background: #e1f5ee; color: #0f6e56; margin-left: 6px; }
      .res-badge-no { display: inline-block; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: 500; background: #fff4e5; color: #7a4f00; margin-left: 6px; }
      .restr-card { background: #ffffff; border: 0.5px solid #e8e8e8; border-radius: 10px; padding: 12px 18px; display: flex; align-items: center; gap: 12px; margin-bottom: 8px; font-family: 'DM Sans', sans-serif; font-size: 13px; color: #1a1a2e; }
      .section-title { font-size: 11px; font-weight: 500; color: #aaa; text-transform: uppercase; letter-spacing: 0.08em; margin: 8px 0 10px; font-family: 'DM Sans', sans-serif; }

      /* ── Inputs ── */
      [data-testid="stTextInput"] input { font-family: 'DM Sans', sans-serif !important; font-size: 13px !important; border: 0.5px solid #e0e0e0 !important; border-radius: 8px !important; box-shadow: none !important; background: #fff !important; }
      [data-testid="stTextInput"] input:focus { border-color: #D85A30 !important; box-shadow: none !important; }
      [data-testid="stTextInput"] label { font-size: 11px !important; font-weight: 500 !important; letter-spacing: 0.06em !important; text-transform: uppercase !important; color: #888 !important; }
      [data-testid="stNumberInput"] input { font-family: 'DM Sans', sans-serif !important; border: 0.5px solid #e0e0e0 !important; border-radius: 8px !important; box-shadow: none !important; }
      [data-testid="stNumberInput"] label { font-size: 11px !important; font-weight: 500 !important; letter-spacing: 0.06em !important; text-transform: uppercase !important; color: #888 !important; }

      /* ── Botones inline ── */
      [data-testid="stButton"][data-key^="inc_"] button { background: #f7f6f3 !important; color: #1a1a2e !important; border: 0.5px solid #e0e0e0 !important; padding: 4px 10px !important; font-size: 14px !important; border-radius: 8px !important; }
      [data-testid="stButton"][data-key^="dec_"] button { background: #f7f6f3 !important; color: #1a1a2e !important; border: 0.5px solid #e0e0e0 !important; padding: 4px 10px !important; font-size: 14px !important; border-radius: 8px !important; }
      [data-testid="stButton"][data-key^="del_"] button { background: rgba(216,90,48,0.08) !important; color: #D85A30 !important; border: 0.5px solid rgba(216,90,48,0.3) !important; padding: 4px 10px !important; border-radius: 8px !important; }
      [data-testid="stButton"][data-key^="save_"] button { background: #1a1a2e !important; color: #f0ede8 !important; border: none !important; width: 100% !important; border-radius: 8px !important; }

      /* ── Expander ── */
      [data-testid="stExpander"] { background: #ffffff !important; border: 0.5px solid #e8e8e8 !important; border-radius: 10px !important; }
      [data-testid="stExpander"] summary { font-family: 'DM Sans', sans-serif !important; font-size: 13px !important; color: #888 !important; }
    </style>
    """)

    # ── Topbar — dentro de un container con key para CSS aislado ──────────
    with st.container(key="topbar"):
        col_brand, col_ev, col_inv, col_ideas, col_space, col_back = st.columns([2, 1, 1, 1, 4, 1.5])

        with col_brand:
            st.markdown('<p style="font-family:Playfair Display,serif;font-size:18px;font-weight:500;color:#f0ede8;margin:0;padding:8px 0;">AgencePro<span style="color:#D85A30">.</span></p>', unsafe_allow_html=True)

        with col_ev:
            st.write("")
            st.write("")
            if st.button("🗓️ Eventos", key="btn_nav_ev"):
                st.session_state.page = "dashboard"
                st.rerun()

        with col_inv:
            st.write("")
            st.write("")
            st.button("📦 Inventario", key="btn_nav_inv")

        with col_ideas:
            st.write("")
            st.write("")
            if st.button("💡 Ideas", key="btn_nav_ideas"):
                st.session_state.page = "ideas"
                st.rerun()

        with col_space:
            st.write("")

        with col_back:
            st.write("")
            st.write("")
            if st.button("← Volver", key="btn_back"):
                st.session_state.page = "dashboard"
                st.rerun()

    # ── Tabs ──────────────────────────────────────────────────────────────
    tabs = st.tabs(["📦 Recursos", "👥 Equipo", "⚖️ Restricciones"])

    # ════════════════════════════════════════════════════════
    # TAB 1 — RECURSOS
    # ════════════════════════════════════════════════════════
    with tabs[0]:
        resources = st.session_state.session.data.get("resources", [])
        if not resources:
            st.info("No hay recursos aún. ¡Agrega el primero!")
        else:
            st.markdown('<div class="section-title">Recursos materiales</div>', unsafe_allow_html=True)
            for r in resources:
                name, type_, quantity, dispo = r
                badge = '<span class="res-badge-ok">disponible</span>' if dispo else '<span class="res-badge-no">no disponible</span>'
                col_card, col_inc, col_dec, col_del = st.columns([8, 0.5, 0.5, 0.5])
                with col_card:
                    st.markdown(f"""
                    <div class="res-card">
                      <div class="res-icon"><i class="ti ti-package"></i></div>
                      <div style="flex:1;">
                        <div class="res-name">{name}{badge}</div>
                        <div class="res-meta">{type_ or "—"} · Cantidad: {quantity}</div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
                with col_inc:
                    st.write("")
                    if st.button("➕", key=f"inc_{name}"):
                        try:
                            st.session_state.session.add_resources([[name, type_, 1, dispo]])
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))
                with col_dec:
                    st.write("")
                    if st.button("➖", key=f"dec_{name}"):
                        try:
                            st.session_state.session.remove_resources([[name, type_, 1, dispo]])
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))
                with col_del:
                    st.write("")
                    if st.button("🗑️", key=f"del_{name}"):
                        try:
                            st.session_state.session.remove_resources([[name, type_, quantity, dispo]])
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))

        with st.expander("＋  Agregar recurso"):
            res_name = st.text_input("Nombre del recurso", key="new_res_name")
            res_type = st.text_input("Tipo", key="new_res_type")
            res_qty  = st.number_input("Cantidad", min_value=1, step=1, key="new_res_qty")
            if st.button("Guardar recurso", key="save_resource"):
                if res_name:
                    try:
                        st.session_state.session.add_resources([[res_name, res_type, res_qty, True]])
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))
                else:
                    st.warning("Por favor ingresa un nombre.")

    # ════════════════════════════════════════════════════════
    # TAB 2 — EQUIPO
    # ════════════════════════════════════════════════════════
    with tabs[1]:
        team = st.session_state.session.data.get("employees", [])
        if not team:
            st.info("No hay miembros de equipo aún. ¡Agrega el primero!")
        else:
            st.markdown('<div class="section-title">Roles y empleados</div>', unsafe_allow_html=True)
            for i, emp in enumerate(team):
                rol, quantity, dispo = emp
                badge = '<span class="res-badge-ok">disponible</span>' if dispo else '<span class="res-badge-no">no disponible</span>'
                col_card, col_inc, col_dec, col_del = st.columns([8, 0.5, 0.5, 0.5])
                with col_card:
                    st.markdown(f"""
                    <div class="res-card">
                      <div class="res-icon"><i class="ti ti-user"></i></div>
                      <div style="flex:1;">
                        <div class="res-name">{rol}{badge}</div>
                        <div class="res-meta">Cantidad: {quantity}</div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
                with col_inc:
                    st.write("")
                    if st.button("➕", key=f"inc_{rol}_{i}"):
                        try:
                            st.session_state.session.add_employee([[rol, 1, dispo]])
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))
                with col_dec:
                    st.write("")
                    if st.button("➖", key=f"dec_{rol}_{i}"):
                        try:
                            st.session_state.session.remove_employee([[rol, 1, dispo]])
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))
                with col_del:
                    st.write("")
                    if st.button("🗑️", key=f"del_{rol}_{i}"):
                        try:
                            st.session_state.session.remove_employee([[rol, quantity, dispo]])
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))

        with st.expander("＋  Agregar rol"):
            emp_rol  = st.text_input("Nombre del rol", key="new_emp_rol")
            emp_cant = st.number_input("Cantidad", min_value=1, step=1, key="new_emp_qty")
            if st.button("Guardar rol", key="save_employee"):
                if emp_rol:
                    try:
                        st.session_state.session.add_employee([[emp_rol, emp_cant, True]])
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))
                else:
                    st.warning("Por favor ingresa un nombre de rol.")

    # ════════════════════════════════════════════════════════
    # TAB 3 — RESTRICCIONES
    # ════════════════════════════════════════════════════════
    with tabs[2]:
        co_requisites = st.session_state.session.data.get("co_requisites", {})
        exclusions    = st.session_state.session.data.get("exclusions", [])

        if not co_requisites and not exclusions:
            st.info("No hay restricciones definidas aún.")

        st.markdown('<div class="section-title">Co-requisitos</div>', unsafe_allow_html=True)
        if co_requisites:
            for resource, deps in co_requisites.items():
                for dep in deps:
                    col_card, col_del = st.columns([10, 0.5])
                    with col_card:
                        st.markdown(f"""
                        <div class="restr-card">
                          <i class="ti ti-link" style="color:#D85A30;font-size:16px;flex-shrink:0;"></i>
                          <span><b>{resource}</b> depende de <b>{dep}</b></span>
                        </div>
                        """, unsafe_allow_html=True)
                    with col_del:
                        st.write("")
                        if st.button("🗑️", key=f"del_coreq_{resource}_{dep}"):
                            try:
                                st.session_state.session.remove_co_rq(resource, [dep])
                                st.rerun()
                            except Exception as e:
                                st.error(str(e))

        with st.expander("＋  Agregar co-requisito"):
            coreq_res  = st.text_input("Recurso con dependencia", key="coreq_res")
            coreq_deps = st.text_input("Dependencias (separadas por coma)", key="coreq_deps")
            if st.button("Guardar co-requisito", key="save_coreq"):
                deps_list = [d.strip() for d in coreq_deps.split(",") if d.strip()]
                try:
                    st.session_state.session.add_co_rq(coreq_res, deps_list)
                    st.success("Co-requisito agregado.")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))

        st.markdown('<div class="section-title" style="margin-top:20px;">Exclusiones</div>', unsafe_allow_html=True)
        if exclusions:
            for r1, r2 in exclusions:
                col_card, col_del = st.columns([10, 0.5])
                with col_card:
                    st.markdown(f"""
                    <div class="restr-card">
                      <i class="ti ti-ban" style="color:#D85A30;font-size:16px;flex-shrink:0;"></i>
                      <span><b>{r1}</b> no puede usarse con <b>{r2}</b></span>
                    </div>
                    """, unsafe_allow_html=True)
                with col_del:
                    st.write("")
                    if st.button("🗑️", key=f"del_excl_{r1}_{r2}"):
                        try:
                            st.session_state.session.remove_exclusion(r1, r2)
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))

        with st.expander("＋  Agregar exclusión"):
            excl_r1 = st.text_input("Primer recurso", key="excl_r1")
            excl_r2 = st.text_input("Segundo recurso", key="excl_r2")
            if st.button("Guardar exclusión", key="save_exclusion"):
                try:
                    st.session_state.session.add_exclusion(excl_r1, excl_r2)
                    st.success(f"Exclusión: {excl_r1} no puede usarse con {excl_r2}.")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))