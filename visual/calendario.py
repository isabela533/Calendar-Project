import streamlit as st
import calendar
from datetime import date, timedelta, datetime

MESES_NOMBRES = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def shift_month(year, month, delta):
    m = month + delta
    y = year
    if m > 12:
        m = 1
        y += 1
    elif m < 1:
        m = 12
        y -= 1
    return y, m


def parse_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def show_calendario():

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

      /* ── Calendario ── */
      .cal-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; }
      .cal-month-title { font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 500; color: #1a1a2e; }
      .cal-weekdays { display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; margin-bottom: 6px; }
      .cal-weekday { text-align: center; font-size: 11px; font-weight: 500; color: #aaa; text-transform: uppercase; letter-spacing: 0.06em; padding: 4px 0; font-family: 'DM Sans', sans-serif; }
      .cal-days { display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; }
      .cal-day { background: #ffffff; border: 0.5px solid #e8e8e8; border-radius: 8px; min-height: 90px; padding: 6px; display: flex; flex-direction: column; gap: 3px; font-family: 'DM Sans', sans-serif; }
      .cal-day.other-month { background: #f7f6f3; opacity: 0.5; }
      .cal-day.today { border: 1.5px solid #D85A30; }
      .cal-daynum { font-size: 12px; color: #888; }
      .cal-day.today .cal-daynum { color: #D85A30; font-weight: 500; }
      .cal-chip { font-size: 10px; padding: 2px 6px; border-radius: 6px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
      .cal-more { font-size: 10px; color: #aaa; padding: 2px 6px; }

      /* botones de navegación de mes — transparentes */
      .st-key-cal_prev button,
      .st-key-cal_next button {
        background: transparent !important;
        color: #888 !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 20px !important;
        font-weight: 500 !important;
        padding: 6px 10px !important;
        transition: background 0.15s, color 0.15s;
      }
      .st-key-cal_prev button:hover,
      .st-key-cal_next button:hover {
        background: #f7f6f3 !important;
        color: #1a1a2e !important;
      }

      .st-key-cal_today button {
        background: transparent !important;
        color: #D85A30 !important;
        border: 0.5px solid rgba(216,90,48,0.3) !important;
        border-radius: 8px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        padding: 6px 14px !important;
        transition: background 0.15s;
      }
      .st-key-cal_today button:hover {
        background: rgba(216,90,48,0.08) !important;
      }
    </style>
    """)

    # ── Datos ─────────────────────────────────────────────────────────────
    money    = st.session_state.session.data["money"]
    correo   = st.session_state.get("correo", "usuario@agencia.com")
    initials = correo[:2].upper()
    events   = st.session_state.session.data.get("events", [])
    dot_colors = ["#D85A30", "#7F77DD", "#1D9E75", "#D4537E", "#378ADD", "#BA7517"]

    # ── Sidebar ───────────────────────────────────────────────────────────
    role = getattr(st.session_state.session, "role", "admin")
    with st.sidebar:
        st.markdown("&nbsp;", unsafe_allow_html=True)
        st.markdown('<div class="sb-brand">AgencePro<span>.</span></div>', unsafe_allow_html=True)
        st.metric(label="Presupuesto", value=f"${money:,.2f}")
        st.markdown('<div class="sb-nav-label">Menú</div>', unsafe_allow_html=True)

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
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Topbar ────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="topbar">
      <div class="topbar-title">Calendario 📆</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # ── Estado del mes mostrado ──────────────────────────────────────────
    hoy = date.today()
    if "cal_year" not in st.session_state:
        st.session_state.cal_year = hoy.year
    if "cal_month" not in st.session_state:
        st.session_state.cal_month = hoy.month

    year  = st.session_state.cal_year
    month = st.session_state.cal_month

    # ── Mapear eventos a colores y a fechas ──────────────────────────────
    event_color = {}
    event_map = {}
    for i, ev in enumerate(events):
        color = dot_colors[i % len(dot_colors)]
        event_color[ev["name"]] = color
        try:
            d_init = parse_date(ev["init"])
            d_end  = parse_date(ev["end"])
        except Exception:
            continue
        d = d_init
        while d <= d_end:
            event_map.setdefault(d, []).append((ev["name"], color))
            d += timedelta(days=1)

    # ── Navegación de mes ─────────────────────────────────────────────────
    col_prev, col_title, col_next, col_today = st.columns([1, 5, 1, 1.2])
    with col_prev:
        if st.button("←", key="cal_prev"):
            st.session_state.cal_year, st.session_state.cal_month = shift_month(year, month, -1)
            st.rerun()
    with col_title:
        st.markdown(f'<div class="cal-month-title" style="text-align:center;">{MESES_NOMBRES[month]} {year}</div>', unsafe_allow_html=True)
    with col_next:
        if st.button("→", key="cal_next"):
            st.session_state.cal_year, st.session_state.cal_month = shift_month(year, month, 1)
            st.rerun()
    with col_today:
        if st.button("Hoy", key="cal_today"):
            st.session_state.cal_year = hoy.year
            st.session_state.cal_month = hoy.month
            st.rerun()

    # ── Cuadrícula del calendario ────────────────────────────────────────
    cal = calendar.Calendar(firstweekday=0)
    weeks = cal.monthdatescalendar(year, month)

    weekdays_html = "".join(
        f'<div class="cal-weekday">{d}</div>' for d in ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
    )

    days_html = ""
    for week in weeks:
        for d in week:
            classes = "cal-day"
            if d.month != month:
                classes += " other-month"
            if d == hoy:
                classes += " today"

            chips_html = ""
            day_events = event_map.get(d, [])
            for name, color in day_events[:2]:
                chips_html += (
                    f'<div class="cal-chip" style="background:{color}22; color:{color};">{name}</div>'
                )
            if len(day_events) > 2:
                chips_html += f'<div class="cal-more">+{len(day_events) - 2} más</div>'

            days_html += f"""
            <div class="{classes}">
              <div class="cal-daynum">{d.day}</div>
              {chips_html}
            </div>
            """

    st.html(f"""
    <div class="cal-weekdays">{weekdays_html}</div>
    <div class="cal-days">{days_html}</div>
    """)

    # ── Lista de eventos del mes ─────────────────────────────────────────
    eventos_mes = []
    for ev in events:
        try:
            d_init = parse_date(ev["init"])
            d_end  = parse_date(ev["end"])
        except Exception:
            continue
        if d_init.year == year and d_init.month == month or d_end.year == year and d_end.month == month:
            eventos_mes.append(ev)

    if eventos_mes:
        st.markdown(f"#### Eventos en {MESES_NOMBRES[month]}")
        for ev in eventos_mes:
            color = event_color.get(ev["name"], "#888")
            st.markdown(f"""
            <div style="background:#ffffff; border:0.5px solid #e8e8e8; border-radius:10px;
                        padding:12px 16px; margin-bottom:8px; font-family:'DM Sans',sans-serif;
                        display:flex; align-items:center; gap:12px;">
              <div style="width:10px; height:10px; border-radius:50%; background:{color}; flex-shrink:0;"></div>
              <div style="flex:1; font-size:14px; font-weight:500; color:#1a1a2e;">{ev['name']}</div>
              <div style="font-size:12px; color:#888;">{ev['init']} → {ev['end']}</div>
              <div style="font-size:13px; font-weight:500; color:#1a1a2e; min-width:60px; text-align:right;">${float(ev['cost']):,.2f}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No hay eventos este mes.")

    st.markdown('</div>', unsafe_allow_html=True)