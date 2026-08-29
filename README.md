# Clínica Medisur Chatbot — Automatización de Atención al Paciente

Sistema conversacional desarrollado en Python diseñado para optimizar la comunicación médico-paciente, gestionar consultas informativas y automatizar la confirmación de citas en tiempo real.

---

### Descripción del Proyecto

El chatbot actúa como un asistente virtual capaz de procesar intenciones de lenguaje natural para gestionar flujos de información institucional e interactuar con datos estructurados para el seguimiento de citas programadas.

---

### Habilidades Técnicas y Valor Agregado

* **Gestión de Datos y Automatización:** Manipulación de archivos estructurados (`.csv`) y consultas dinámicas mediante Python y Pandas.
* **Lógica de Procesamiento (NLP):** Diseño de flujos de conversación guiados según el tipo de consulta del paciente.
* **Entrega de Documentación:** Sistema de envío automático de normativas y requisitos (PDF) para estudios médicos.
* **Seguridad:** Manejo de credenciales y variables de entorno (`.env`) para la protección de datos de configuración.

---

### Stack Tecnológico

| Tecnología | Propósito Técnico |
| :--- | :--- |
| **Python 3.x** | Lenguaje principal para la lógica del bot y procesamiento. |
| **Pandas / CSV** | Consulta y gestión de la base de datos de citas y estudios. |
| **NLP Logic** | Procesamiento de intenciones del usuario para respuestas automáticas. |
| **Venv / Pip** | Aislamiento de dependencias y entorno virtual. |

---

### Funcionalidades Principales

1. **Atención Automatizada:** Respuestas instantáneas sobre horarios, ubicación y preparación para estudios clínicos.
2. **Gestión de Citas:** Consulta dinámica en base de datos para confirmar día y hora de turnos existentes.
3. **Reducción de Ausentismo:** Notificación de indicaciones específicas según el procedimiento programado.
4. **Entrega de Requisitos:** Provisión directa de documentos con indicaciones previas a la visita.

---

### Instalación y Ejecución Local

```bash
# Clonar el repositorio
git clone [https://github.com/TatiiRamos/clinica-medisur.git](https://github.com/TatiiRamos/clinica-medisur.git)

# Entrar al directorio
cd clinica-medisur

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el chatbot
python bot.py
