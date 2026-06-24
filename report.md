# AgencePro 🗓️

**Gestión integral para agencias de marketing** — eventos, inventario, equipo y presupuesto, todo en un solo lugar.

AgencePro nace de un problema muy concreto: una agencia que maneja varios eventos a la vez necesita saber, en todo momento, qué recursos tiene libres, qué empleados puede asignar, cuánto presupuesto le queda y si una fecha ya está comprometida. Este proyecto resuelve eso con una interfaz clara y una lógica de validación que nunca deja el inventario en un estado inconsistente.

---

## ✨ Qué puedes hacer con AgencePro

- 📅 **Agendar eventos**: crea, busca y elimina eventos con nombre, fechas, costo, recursos y equipo asociado.
- ⚠️ **Validación automática**: el sistema comprueba presupuesto, disponibilidad de fechas y restricciones. Si una fecha está ocupada, sugiere huecos libres.
- 📦 **Inventario configurable**: administra recursos materiales (laptops, proyectores, salas) y equipo humano (roles y cantidades).
- ⚖️ **Restricciones a tu medida**: define qué recursos dependen de otros (co-requisitos)(ej. un proyector requiere una sala) o qué recursos no pueden combinarse (exclusiones)
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
## 🖥️ Cómo se usa el programa

### 🔑 Primer acceso: registro de cuenta
- Al abrir la aplicación por primera vez, el usuario llega a la pantalla de inicio de sesión.  
- Si no tiene cuenta, pulsa **"Crear una cuenta nueva"** y completa el registro:  
  1. ✉️ Ingresa un correo electrónico (ej. `isabela.agencia@gmail.com`).  
  2. 💰 Ingresa el presupuesto inicial (ej. `50000`).  
  3. 🖱️ Pulsa "Crear cuenta".  
- El sistema valida que el correo no esté registrado previamente.  
- Si ya existe, invita a iniciar sesión. Si es nuevo, crea la cuenta y redirige al **panel de eventos**.

---

### 🔐 Inicio de sesión
- En accesos posteriores, basta con ingresar el correo y pulsar **"Continuar"**.  
- El sistema carga automáticamente presupuesto, inventario, equipo, restricciones y eventos previos.

---

### 📅 Panel de Eventos
- Pantalla principal del sistema: muestra presupuesto disponible, buscador y lista de eventos.  
- Ejemplo: crear un evento **“Lanzamiento de producto”**:  
  1. Despliega el panel "Agregar nuevo evento".  
  2. Escribe nombre, selecciona fechas e indica costo.  
  3. Selecciona recursos (ej. laptops, proyector).  
  4. Selecciona equipo humano (ej. fotógrafo, asistentes).  
  5. Pulsa "Guardar evento".  
- El sistema valida presupuesto, disponibilidad y restricciones.  
- Si todo es correcto:  
  - El evento se agrega a la lista.  
  - El presupuesto se descuenta automáticamente.  
  - Recursos y empleados quedan ocupados hasta que se elimine el evento.  
- Si la fecha está ocupada, el sistema sugiere automáticamente **alternativas disponibles**.

---

### 📦 Inventario
- Organizado en tres pestañas: **Recursos**, **Equipo**, **Restricciones** (y **Acceso** si el usuario es administrador).  
- Ejemplo: agregar un recurso y definir una restricción:  
  1. En Recursos: agrega "Proyector", tipo "Tecnología", cantidad 3.  
  2. En Restricciones: define que "Proyector" depende de "Sala de Conferencias".  
  3. También puedes definir exclusiones (ej. Sala A no junto con Sala B).  

---

### 💡 Ideas estratégicas
- Presenta automáticamente fechas comerciales clave del año (Black Friday, Navidad, etc.).  
- Agrupadas en:  
  - **Próximas oportunidades** (60 días).  
  - **Listado completo** filtrable por mes.  
- Ejemplo: si en 15 días es Black Friday, pulsa **"Agendar"** y el sistema abre el formulario con nombre y fecha ya prellenados.

---

### 🗓️ Calendario
- Vista mensual en cuadrícula, similar a un calendario convencional.  
- Cada día con evento muestra una etiqueta con su nombre.  
- Navegación entre meses con botones de avance/retroceso o volver al mes actual con **"Hoy"**.

---

### 📊 Reportes
- Calcula métricas en tiempo real:  
  - Presupuesto inicial, total gastado y disponible.  
  - Número total de eventos.  
  - Gasto agrupado por mes.  
  - Eventos más costosos.  
  - Recursos y roles más solicitados.  

---

## 🎯 Resumen de uso
En pocas palabras, el flujo de trabajo es:
1. **Registrar cuenta** con correo y presupuesto.  
2. **Iniciar sesión** para acceder al panel principal.  
3. **Crear y gestionar eventos** con validación automática.  
4. **Administrar inventario y restricciones** para asegurar disponibilidad.  
5. **Aprovechar ideas estratégicas** y fechas clave del calendario comercial.  
6. **Visualizar calendario mensual** para tener una visión clara de la agenda.  
7. **Consultar reportes** para analizar presupuesto y desempeño de la agencia.  

✨ Con este flujo, AgencePro se convierte en una herramienta integral que combina planificación, control de inventario y análisis financiero en una sola interfaz.

---

## 🧩 El reto más grande

La dificultad más importante del proyecto, y la que más influyó en el diseño final, fue encontrar una forma de organizar el manejo de datos que fuera exhaustiva, sin repeticiones ni ambigüedades sobre quién era responsable de cada operación. Con varias entidades relacionadas entre sí (eventos, recursos, empleados, restricciones, presupuesto), el riesgo de terminar con lógica duplicada en distintas partes del programa, o con dos funciones distintas modificando el mismo dato de formas inconsistentes, era alto desde el principio.

Para resolver esto, estructuré el proyecto alrededor de una clase madre, Session, que controla al usuario autenticado y todos sus datos una vez guardados. A partir de esta clase se ramifican subclases especializadas: Resources_Manager para el manejo de recursos materiales, Team_Manager para el manejo del equipo de trabajo, y Restrictions para la gestión de las reglas de co-requisitos y exclusiones entre recursos. Diseñé estas tres subclases para que fueran completamente ajustables por el propio usuario desde la interfaz (puede agregar, modificar o eliminar recursos, roles y restricciones en cualquier momento), lo cual le da mayor versatilidad al proyecto y evita tener que hardcodear valores fijos.

Complementando esta estructura, necesitaba también un gestor del formato de datos que utilizo para persistir la información del usuario: para esto construí la clase Gestor_json, que es la única responsable de leer y escribir el archivo JSON correspondiente a cada cuenta. Gracias a esta separación, todas las funciones de negocio del programa pueden apoyarse en los datos ya registrados del usuario para tomar decisiones. Un ejemplo claro de esto es la lógica para agregar un nuevo evento: cada vez que el usuario intenta programar un evento, el sistema verifica constantemente, contra los datos ya guardados, si la fecha solicitada está ocupada por algún otro evento existente, y solo permite continuar si esa verificación es exitosa.


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

## 🎯 Conclusión
**AgencePro** no es solo una herramienta de gestión, es un sistema que refleja buenas prácticas de diseño de software: separación de responsabilidades, validación atómica, sincronización de estados y personalización visual.
Con él, cualquier agencia puede planificar y ejecutar eventos de forma eficiente, evitando errores y aprovechando al máximo sus recursos.
