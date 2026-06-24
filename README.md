# 🚀 AgencePro

**AgencePro** es una aplicación web para agencias de marketing que necesitan organizar **eventos, recursos, equipo humano y presupuesto** desde un solo lugar.

## ✨ Funcionalidades principales
- 🔑 **Autenticación**: registro e inicio de sesión por correo.
- 📅 **Gestión de eventos**: crear, buscar y eliminar eventos con validación automática de fechas y recursos.
- 📦 **Inventario**: administrar recursos materiales y equipo humano.
- ⚖️ **Restricciones**: definir co-requisitos y exclusiones entre recursos.
- 🎯 **Ideas estratégicas**: fechas comerciales clave (Black Friday, Navidad, etc.).
- 🗓️ **Calendario mensual**: vista visual de eventos agendados.
- 📊 **Reportes**: presupuesto disponible, gasto mensual y recursos más usados.

## 👥 Roles y permisos

En **AgencePro** existen dos tipos de usuarios:

### 🔹 Operador
- Puede acceder y gestionar:
  - 📅 **Eventos**
  - 💡 **Ideas nuevas**
  - 🗓️ **Calendario**
- Su rol está enfocado en la **operación diaria** de la agencia.

### 🔹 Administrador
- Tiene acceso a todo lo anterior **y además**:
  - 📦 **Inventario** (recursos materiales, equipo humano)
  - 👥 **Gestión de operadores**
  - 📊 **Reportes de la agencia**
- Su rol está enfocado en la **gestión completa y estratégica** de la organización.

## 🛠️ Tecnologías
- **Python** 🐍
- **Streamlit** 🌐
- **JSON** para persistencia de datos

## ▶️ Cómo ejecutar
1. Instala dependencias:

```bash
# 1. Instala las dependencias
pip install streamlit

# 2. Ubícate en la carpeta visual/ (ahí vive el punto de entrada de la app)
cd visual

# 3. Ejecuta
streamlit run visual.py
```

Streamlit abrirá automáticamente una pestaña en tu navegador (normalmente en `http://localhost:8501`). Desde ahí puedes crear una cuenta nueva o iniciar sesión con una existente.

## 💡 Ejemplo de uso

1. ✉️ Regístrate con tu correo y presupuesto inicial.  
2. 📝 Crea un evento: nombre, fechas, costo, recursos y equipo.  
3. ✅ El sistema valida disponibilidad y restricciones automáticamente.  
4. 📅 Visualiza tus eventos en el calendario y consulta reportes en tiempo real.  

> 💡 **¿Quieres probarlo rápido sin crear una cuenta?** Inicia sesión con `isabela.alvarez.ramos@gmail.com` — ya tiene presupuesto, inventario, equipo y eventos cargados de ejemplo, lista para explorar todas las funcionalidades sin pasos previos.

---

## 🛠️ Construido con

- **Python** — lógica de negocio y manejo de datos
- **Streamlit** — interfaz web reactiva
- **HTML/CSS embebido** — identidad visual propia sobre los componentes de Streamlit
- **JSON** — persistencia de datos por usuario

---

✨ Con **AgencePro** tu agencia tendrá todo lo necesario para planificar y gestionar eventos de forma clara, organizada y eficiente.
