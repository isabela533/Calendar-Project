# AgencePro 🗓️

**Gestión integral para agencias de marketing** — eventos, inventario, equipo y presupuesto, todo en un solo lugar.

AgencePro nace de un problema muy concreto: una agencia que maneja varios eventos a la vez necesita saber, en todo momento, qué recursos tiene libres, qué empleados puede asignar, cuánto presupuesto le queda y si una fecha ya está comprometida. Este proyecto resuelve eso con una interfaz clara y una lógica de validación que nunca deja el inventario en un estado inconsistente.

---

## ✨ Qué puedes hacer con AgencePro

- 📅 **Agendar eventos** con fechas, costo, recursos y equipo asociado
- ⚠️ **Validación automática** de presupuesto, disponibilidad de fecha y restricciones — si una fecha ya está ocupada, el sistema te sugiere huecos libres
- 📦 **Inventario configurable** de recursos materiales y equipo humano, con control de cantidades y disponibilidad
- ⚖️ **Restricciones a tu medida**: define qué recursos dependen de otros (co-requisitos) o qué recursos no pueden combinarse (exclusiones)
- 💡 **Ideas estratégicas**: fechas comerciales clave del año (Black Friday, Día de la Madre, Navidad...) calculadas automáticamente, listas para agendar con un clic
- 📆 **Calendario mensual** con vista de cuadrícula y navegación entre meses
- 📊 **Reportes en tiempo real**: gasto por mes, eventos más costosos, recursos y roles más usados

---

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

---

## 🚀 Cómo ejecutarlo

```bash
# 1. Instala las dependencias
pip install streamlit

# 2. Ubícate en la carpeta visual/ (ahí vive el punto de entrada de la app)
cd visual

# 3. Ejecuta
streamlit run visual.py
```

Streamlit abrirá automáticamente una pestaña en tu navegador (normalmente en `http://localhost:8501`). Desde ahí puedes crear una cuenta nueva o iniciar sesión con una existente.

> 💡 **¿Quieres probarlo rápido sin crear una cuenta?** Inicia sesión con `isabela.alvarez.ramos@gmail.com` — ya tiene presupuesto, inventario, equipo y eventos cargados de ejemplo, lista para explorar todas las funcionalidades sin pasos previos.

---

## 🧠 Cómo está pensado por dentro

El reto principal de este proyecto no era solo la interfaz, sino mantener el manejo de datos **ordenado, exhaustivo y sin ambigüedades** a medida que crecía la cantidad de entidades relacionadas: eventos, recursos, empleados, restricciones y presupuesto.

La solución fue una arquitectura en capas con una clase central, `Session`, que actúa como punto único de acceso a los datos de cada cuenta. A partir de ahí se ramifica en subclases con una responsabilidad clara cada una:

| Clase | Responsabilidad |
|---|---|
| `Session` | Controla al usuario autenticado y coordina el acceso a todos sus datos |
| `Resources_Manager` | Inventario de recursos materiales (alta, baja, ocupar, liberar) |
| `Team_Manager` | Inventario de equipo humano, con la misma lógica |
| `Restrictions` | Co-requisitos y exclusiones entre recursos, ajustables por el usuario |
| `Gestor_json` | Lectura y escritura del archivo de datos de cada cuenta |

Esta separación evita que dos partes del programa modifiquen el mismo dato de formas contradictorias, y hace que cada cambio quede contenido en un único lugar predecible.

Un detalle que terminó siendo clave: al crear un evento, el sistema **primero valida todo** (presupuesto, fechas, restricciones) sin tocar el inventario, y solo si todo pasa, recién ahí ocupa recursos y empleados. Separar "verificar" de "ejecutar" evitó un bug bastante escurridizo donde el inventario quedaba descontado aunque la creación del evento fallara.

---

## 🧩 El reto más grande

Lograr que el manejo de datos fuera **exhaustivo y sin ambigüedades** fue, de lejos, lo más difícil del proyecto. Necesitaba código que me organizara y estuviera optimizado, sin repeticiones ni zonas grises sobre quién modificaba qué.

La solución fue justamente la arquitectura en capas de arriba: una clase madre `Session` que controla al usuario y sus datos guardados, ramificada en subclases ajustables por el propio usuario (`Resources_Manager`, `Team_Manager`, `Restrictions`), más un `Gestor_json` dedicado solo a leer y escribir el archivo de datos. Gracias a eso, funciones como agregar un evento pueden apoyarse constantemente en los datos ya guardados — por ejemplo, verificando en cada intento si la fecha elegida ya está ocupada por otro evento antes de continuar.

## 💡 Aprendizajes

- **Separar responsabilidades de verdad ayuda.** No es solo teoría: dividir el sistema en clases con un único propósito hizo que cada cambio quedara contenido en un solo lugar, en vez de obligarme a tocar medio proyecto por un ajuste pequeño.
- **Validar antes de modificar, siempre.** Cuando una operación afecta varios recursos relacionados a la vez, hay que confirmar que todo va a salir bien *antes* de tocar nada — validar a mitad de camino es la receta perfecta para un inventario inconsistente.
- **Memoria y disco no se sincronizan solos.** Trabajar con JSON me obligó a pensar explícitamente en cuándo y cómo sincronizar los objetos en memoria con su versión guardada en archivo.
- **Streamlit reactiva distinto.** Aprendí a depender de `session_state` como única fuente de verdad entre ejecuciones, a usar `rerun()` con intención, y a entender por qué un widget puede "ignorar" un valor nuevo si su identificador no cambia.

## 🛠️ Construido con

- **Python** — lógica de negocio y manejo de datos
- **Streamlit** — interfaz web reactiva
- **HTML/CSS embebido** — identidad visual propia sobre los componentes de Streamlit
- **JSON** — persistencia de datos por usuario

---

## 📌 Estado del proyecto

Proyecto funcional con flujo completo: registro → inicio de sesión → gestión de eventos, inventario, ideas estratégicas, calendario y reportes. Sigue evolucionando — las ideas de mejora más cercanas son plantillas de eventos reutilizables y notificaciones de presupuesto bajo.