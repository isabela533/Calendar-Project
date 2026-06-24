import streamlit as st
import streamlit.components.v1 as components
from logic_buttons import handle_signup

def show_signup():
    warning_msg = st.session_state.pop("signup_warning", "")

    st.html("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    <style>
      .main > div { padding-top: 0 !important; }
      [data-testid="stAppViewContainer"] { padding: 0 !important; }
      [data-testid="block-container"] { padding: 0 !important; max-width: 100% !important; }
      header[data-testid="stHeader"] { display: none; }
      [data-testid="column"]:first-child > div:first-child { height: 100vh; }
      .login-title { font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 400; color: #1a1a2e; margin: 0 0 6px; }
      .login-subtitle { font-size: 13px; color: #888; margin: 0 0 28px; font-weight: 300; }
      .form-warning { background: #fff4e5; border: 0.5px solid #f5a623; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #7a4f00; margin-bottom: 16px; }
      .divider-wrap { display: flex; align-items: center; gap: 12px; margin: 10px 0; }
      .divider-line { flex: 1; height: 0.5px; background: #e0e0e0; }
      .divider-text { font-size: 12px; color: #aaa; white-space: nowrap; }
      .help-text { font-size: 12px; color: #aaa; text-align: center; margin-top: 16px; font-weight: 300; }
      [data-testid="stTextInput"] input, [data-testid="stNumberInput"] input {
        font-family: 'DM Sans', sans-serif !important; font-size: 14px !important;
        border: 0.5px solid #d0d0d0 !important; border-radius: 8px !important;
        padding: 12px 14px !important; color: #1a1a2e !important; box-shadow: none !important;
      }
      [data-testid="stTextInput"] input:focus, [data-testid="stNumberInput"] input:focus {
        border-color: #D85A30 !important; box-shadow: none !important;
      }
      [data-testid="stTextInput"] label, [data-testid="stNumberInput"] label {
        font-size: 11px !important; font-weight: 500 !important;
        letter-spacing: 0.08em !important; text-transform: uppercase !important; color: #888 !important;
      }
      [data-testid="stNumberInput"] [data-testid="stNumberInputStepDown"],
      [data-testid="stNumberInput"] [data-testid="stNumberInputStepUp"] { display: none !important; }
      div[data-testid="stButton"]:nth-of-type(1) button {
        width: 100% !important; padding: 13px !important; background: #1a1a2e !important;
        color: #f0ede8 !important; border: none !important; border-radius: 8px !important;
        font-size: 14px !important; font-weight: 500 !important;
      }
      div[data-testid="stButton"]:nth-of-type(1) button:hover { background: #2a2a4e !important; }
      div[data-testid="stButton"]:nth-of-type(2) button {
        width: 100% !important; padding: 12px !important; background: transparent !important;
        color: #888 !important; border: 0.5px solid #d0d0d0 !important;
        border-radius: 8px !important; font-size: 13px !important;
      }
      div[data-testid="stButton"]:nth-of-type(2) button:hover { border-color: #D85A30 !important; color: #1a1a2e !important; }
    </style>
    """)

    col_left, col_right = st.columns([1.1, 1])

    with col_left:
        components.html("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
          <meta charset="UTF-8"/>
          <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
          <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body {
              font-family: 'DM Sans', sans-serif;
              height: 100vh; background: #1a1a2e;
              padding: 56px 48px; display: flex;
              flex-direction: column; justify-content: space-between;
              position: relative; overflow: hidden;
            }
            body::before {
              content: ''; position: absolute;
              top: -60px; right: -60px; width: 280px; height: 280px;
              border-radius: 50%; background: #D85A30; opacity: 0.13;
            }
            body::after {
              content: ''; position: absolute;
              bottom: -40px; left: -40px; width: 200px; height: 200px;
              border-radius: 50%; background: #7F77DD; opacity: 0.18;
            }
            .brand-name { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 500; color: #f0ede8; letter-spacing: 0.02em; position: relative; z-index: 1; }
            .brand-dot { color: #D85A30; }
            .left-tagline { position: relative; z-index: 1; }
            .left-tagline h2 { font-family: 'Playfair Display', serif; font-size: 30px; font-weight: 400; color: #f0ede8; line-height: 1.45; margin: 0 0 14px; }
            .left-tagline p { font-size: 14px; color: #8b8b9e; line-height: 1.7; font-weight: 300; }
            .features-row { display: flex; gap: 10px; position: relative; z-index: 1; }
            .feature-item { background: rgba(255,255,255,0.06); border: 0.5px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 16px 14px; flex: 1; display: flex; flex-direction: column; gap: 8px; }
            .feature-icon { font-size: 22px; color: #D85A30; }
            .feature-title { font-size: 12px; font-weight: 500; color: #f0ede8; line-height: 1.3; }
            .feature-desc { font-size: 11px; color: #8b8b9e; font-weight: 300; line-height: 1.5; }
          </style>
        </head>
        <body>
          <div class="brand-name">AgencePro<span class="brand-dot">.</span></div>
          <div class="left-tagline">
            <h2>Planifica mejor.<br>Ejecuta sin caos.<br>Crece con control.</h2>
            <p>La plataforma que centraliza tu agencia<br>de marketing de principio a fin.</p>
          </div>
          <div class="features-row">
            <div class="feature-item">
              <i class="ti ti-calendar-event feature-icon"></i>
              <div class="feature-title">Agenda inteligente</div>
              <div class="feature-desc">Detecta días libres y sugiere las mejores fechas para tus eventos.</div>
            </div>
            <div class="feature-item">
              <i class="ti ti-users feature-icon"></i>
              <div class="feature-title">Gestión de recursos</div>
              <div class="feature-desc">Equipo y materiales en un solo lugar, siempre actualizados.</div>
            </div>
            <div class="feature-item">
              <i class="ti ti-chart-dots feature-icon"></i>
              <div class="feature-title">Control total</div>
              <div class="feature-desc">Ve disponibilidad real y evita conflictos antes de que ocurran.</div>
            </div>
          </div>
        </body>
        </html>
        """, height=700, scrolling=False)

    with col_right:
        st.markdown('<p class="login-title">Crear cuenta</p>', unsafe_allow_html=True)
        st.markdown('<p class="login-subtitle">Completa los datos para empezar</p>', unsafe_allow_html=True)

        if warning_msg:
            st.markdown(f'<div class="form-warning">{warning_msg}</div>', unsafe_allow_html=True)

        correo      = st.text_input("Correo electrónico", placeholder="nombre@empresa.com", key="signup_correo")
        presupuesto = st.number_input("Presupuesto inicial ($)", min_value=0, step=100, key="signup_presupuesto")

        if st.button("Crear cuenta →", key="btn_signup"):
            if not correo or presupuesto <= 0:
              st.session_state.signup_warning = "Por favor completa todos los campos."
              st.rerun()
            else:
              session, mensaje = handle_signup(correo, presupuesto)
              if session and "already exists" in mensaje:
                  # Cuenta existente — muestra aviso y no navega
                  st.session_state.signup_warning = mensaje
                  st.rerun()
              elif session:
                  # Cuenta nueva creada OK
                  st.session_state.session = session
                  st.session_state.correo  = correo
                  st.session_state.page    = "dashboard"
                  st.rerun()
              if warning_msg:
                  st.markdown(f'<div class="form-warning">{warning_msg}</div>', unsafe_allow_html=True)
                  if "already exists" in warning_msg:
                      if st.button("← Iniciar sesión con esta cuenta", key="btn_goto_login"):
                          st.session_state.page = "login"
                          st.rerun()

        st.markdown("""
        <div class="divider-wrap">
          <div class="divider-line"></div>
          <span class="divider-text">¿Ya tienes cuenta?</span>
          <div class="divider-line"></div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("<- Iniciar sesión", key="btn_back_login"):
            st.session_state.page = "login"
            st.rerun()

        st.markdown('<p class="help-text">¿Problemas para acceder? Contacta a tu administrador.</p>', unsafe_allow_html=True)