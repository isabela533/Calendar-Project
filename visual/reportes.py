import streamlit as st
from datetime import datetime, date

MESES_NOMBRES = ["", "Ene", "Feb", "Mar", "Abr", "May", "Jun",
                 "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]


def parse_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def show_reportes():
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
      .main-content { padding: 20px 28px; display: flex; flex-direction: column; gap: 18px; }

      /* ── Métricas ── */
      .rep-metrics { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
      .rep-metric { background: #ffffff; border: 0.5px solid #e8e8e8; border-radius: 10px; padding: 16px; font-family: 'DM Sans', sans-serif; }
      .rep-metric-label { font-size: 11px; color: #aaa; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px; }
      .rep-metric-value { font-size: 22px; font-weight: 500; color: #1a1a2e; }

      /* ── Tarjetas ── */
      .rep-card { background: #ffffff; border: 0.5px solid #e8e8e8; border-radius: 10px; padding: 16px 18px; font-family: 'DM Sans', sans-serif; }
      .rep-card-title { font-size: 11px; font-weight: 500; color: #aaa; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 14px; }

      /* ── Gráfico de barras ── */
      .rep-bars { display: flex; align-items: flex-end; gap: 10px; height: 120px; }
      .rep-bar-col { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px; height: 100%; justify-content: flex-end; }
      .rep-bar { width: 100%; border-radius: 4px 4px 0 0; min-height: 2px; }
      .rep-bar-label { font-size: 11px; color: #aaa; }

      /* ── Filas de ranking ── */
      .rep-row { display: flex; align-items: center; gap: 12px; padding: 8px 0; border-bottom: 0.5px solid #f0efec; }
      .rep-row:last-child { border-bottom: none; }
      .rep-row-name { flex: 1; font-size: 13px; font-weight: 500; color: #1a1a2e; }
      .rep-row-bar-bg { flex: 2; height: 8px; border-radius: 4px; background: #f7f6f3; overflow: hidden; }
      .rep-row-bar-fill { height: 100%; border-radius: 4px; }
      .rep-row-value { font-size: 12px; color: #888; min-width: 50px; text-align: right; }

      .rep-grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
    </style>
    """)

    # ── Datos ─────────────────────────────────────────────────────────────
    data       = st.session_state.session.data
    money      = data["money"]
    correo     = st.session_state.get("correo", "usuario@agencia.com")
    initials   = correo[:2].upper()
    events     = data.get("events", [])

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
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Topbar ────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="topbar">
      <div class="topbar-title">Reportes 📊</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    if not events:
        st.info("Aún no hay eventos registrados. Los reportes aparecerán cuando agregues tu primer evento.")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # ── Cálculos generales ───────────────────────────────────────────────
    total_gastado    = sum(float(ev["cost"]) for ev in events)
    presupuesto_actual = money
    presupuesto_inicial = presupuesto_actual + total_gastado
    total_eventos    = len(events)
    promedio_evento  = total_gastado / total_eventos if total_eventos else 0

    st.html(f"""
    <div class="rep-metrics">
      <div class="rep-metric">
        <div class="rep-metric-label">Presupuesto inicial</div>
        <div class="rep-metric-value">${presupuesto_inicial:,.2f}</div>
      </div>
      <div class="rep-metric">
        <div class="rep-metric-label">Gastado</div>
        <div class="rep-metric-value" style="color:#993C1D;">${total_gastado:,.2f}</div>
      </div>
      <div class="rep-metric">
        <div class="rep-metric-label">Disponible</div>
        <div class="rep-metric-value" style="color:#0F6E56;">${presupuesto_actual:,.2f}</div>
      </div>
      <div class="rep-metric">
        <div class="rep-metric-label">Eventos totales</div>
        <div class="rep-metric-value">{total_eventos}</div>
      </div>
    </div>
    """)

    # ── Gasto por mes ─────────────────────────────────────────────────────
    gasto_por_mes = {m: 0.0 for m in range(1, 13)}
    for ev in events:
        try:
            d = parse_date(ev["init"])
            gasto_por_mes[d.month] += float(ev["cost"])
        except Exception:
            continue

    max_gasto = max(gasto_por_mes.values()) or 1
    bars_html = ""
    for m in range(1, 13):
        valor = gasto_por_mes[m]
        altura = int((valor / max_gasto) * 100) if max_gasto else 0
        color = "#D85A30" if valor > 0 else "#F0997B"
        bars_html += f"""
        <div class="rep-bar-col">
          <div class="rep-bar" style="height:{altura}%; background:{color};"></div>
          <div class="rep-bar-label">{MESES_NOMBRES[m]}</div>
        </div>
        """

    st.html(f"""
    <div class="rep-card">
      <div class="rep-card-title">Gasto por mes</div>
      <div class="rep-bars">{bars_html}</div>
    </div>
    """)

    # ── Eventos más costosos ─────────────────────────────────────────────
    eventos_ordenados = sorted(events, key=lambda ev: float(ev["cost"]), reverse=True)[:5]
    max_costo = max((float(ev["cost"]) for ev in eventos_ordenados), default=1) or 1

    rows_eventos = ""
    for ev in eventos_ordenados:
        costo = float(ev["cost"])
        pct = int((costo / max_costo) * 100) if max_costo else 0
        rows_eventos += f"""
        <div class="rep-row">
          <div class="rep-row-name">{ev['name']}</div>
          <div class="rep-row-bar-bg"><div class="rep-row-bar-fill" style="width:{pct}%; background:#D85A30;"></div></div>
          <div class="rep-row-value">${costo:,.2f}</div>
        </div>
        """

    # ── Recursos más usados ───────────────────────────────────────────────
    uso_recursos = {}
    uso_equipo = {}
    for ev in events:
        for r in ev.get("resources", []):
            nombre, _, cant = r[0], r[1], r[2]
            uso_recursos[nombre] = uso_recursos.get(nombre, 0) + cant
        for t in ev.get("team", []):
            rol, cant = t[0], t[1]
            uso_equipo[rol] = uso_equipo.get(rol, 0) + cant

    top_recursos = sorted(uso_recursos.items(), key=lambda x: x[1], reverse=True)[:5]
    max_uso_rc = max((v for _, v in top_recursos), default=1) or 1

    rows_recursos = ""
    if top_recursos:
        for nombre, cant in top_recursos:
            pct = int((cant / max_uso_rc) * 100) if max_uso_rc else 0
            rows_recursos += f"""
            <div class="rep-row">
              <div class="rep-row-name">{nombre}</div>
              <div class="rep-row-bar-bg"><div class="rep-row-bar-fill" style="width:{pct}%; background:#7F77DD;"></div></div>
              <div class="rep-row-value">x{cant}</div>
            </div>
            """
    else:
        rows_recursos = '<div style="font-size:13px; color:#aaa;">Sin datos aún.</div>'

    st.html(f"""
    <div class="rep-grid2">
      <div class="rep-card">
        <div class="rep-card-title">Eventos más costosos</div>
        {rows_eventos}
      </div>
      <div class="rep-card">
        <div class="rep-card-title">Recursos más usados</div>
        {rows_recursos}
      </div>
    </div>
    """)

    # ── Equipo más usado ──────────────────────────────────────────────────
    top_equipo = sorted(uso_equipo.items(), key=lambda x: x[1], reverse=True)[:5]
    max_uso_emp = max((v for _, v in top_equipo), default=1) or 1

    rows_equipo = ""
    if top_equipo:
        for rol, cant in top_equipo:
            pct = int((cant / max_uso_emp) * 100) if max_uso_emp else 0
            rows_equipo += f"""
            <div class="rep-row">
              <div class="rep-row-name">{rol}</div>
              <div class="rep-row-bar-bg"><div class="rep-row-bar-fill" style="width:{pct}%; background:#1D9E75;"></div></div>
              <div class="rep-row-value">x{cant}</div>
            </div>
            """
    else:
        rows_equipo = '<div style="font-size:13px; color:#aaa;">Sin datos aún.</div>'

    st.html(f"""
    <div class="rep-card">
      <div class="rep-card-title">Equipo más solicitado</div>
      {rows_equipo}
    </div>
    """)

    # ── Promedio por evento ───────────────────────────────────────────────
    st.html(f"""
    <div class="rep-card">
      <div class="rep-card-title">Costo promedio por evento</div>
      <div class="rep-metric-value">${promedio_evento:,.2f}</div>
    </div>
    """)

    st.markdown('</div>', unsafe_allow_html=True)