🤖 Clínica Medisur Chatbot
Este proyecto es un Chatbot conversacional desarrollado en Python diseñado para optimizar la atención al paciente y automatizar las consultas informativas de la Clínica Medisur.

El chatbot utiliza un motor de procesamiento de lenguaje natural (NLP) para gestionar preguntas frecuentes sobre la clínica y, fundamentalmente, para realizar el seguimiento y confirmación de citas programadas.

✨ Características Clave y Funcionalidades
El chatbot ofrece dos pilares de servicio fundamentales para mejorar la experiencia del paciente:

1. Atención al Paciente Automatizada
Responde consultas comunes sobre la operación de la clínica:

Información Institucional: Proporciona datos de contacto, horarios y ubicaciones.

Indicaciones Generales: Entrega directamente el documento de "Indicaciones Generales para Pacientes" (ej. vestimenta, requisitos de documentación) antes de la visita, tal como se muestra en el archivo ins_pacientes.pdf.

Requisitos de Estudios: Responde sobre la documentación o preparación necesaria para estudios clínicos específicos.

2. Gestión y Seguimiento de Turnos (Proceso de Cita)
Confirmación de Turno: Al iniciar la conversación, el chatbot puede buscar en la base de datos (usando consulta_base.py y estudios_clinica.csv) si el paciente tiene una cita programada.

Recordatorios: Envía recordatorios de la cita con anticipación, disminuyendo la tasa de ausentismo (no-shows).

Información Relevante: Proporciona el día, la hora y las indicaciones específicas relevantes para su estudio o consulta.

🛠️ Tecnologías y Arquitectura
https://docs.google.com/spreadsheets/d/1JxI_mkegfw7qBXBrF24quO-OkgyhtikHUbuAQ9yVhFc/edit?gid=572199886#gid=572199886

💻 Instalación y Ejecución
Sigue estos pasos para configurar y ejecutar el chatbot localmente:

Clonar el Repositorio:

Bash

git clone https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories
cd clinica-medisur-chatbot
Crear y Activar Entorno Virtual (Recomendado):

Bash

python -m venv venv
source venv/bin/activate  # En Linux/macOS
# .\venv\Scripts\activate  # En Windows
Instalar Dependencias:

Bash

pip install -r requirements.txt
Configurar Variables de Entorno: Asegúrate de editar el archivo config.py con las credenciales necesarias (si aplica).

Ejecutar el Bot:

Bash

python bot.py
🤝 Contribución y Contacto
¡Tu interés en este proyecto es bienvenido! Si deseas contribuir a mejorar la lógica de conversación, integrar una nueva base de datos o expandir las funcionalidades de citas, siéntete libre de abrir un issue o enviar un pull request.

Este proyecto es una muestra de mis habilidades en automatización de servicios, manejo de datos e integración de Python en soluciones empresariales.

Desarrollado por: Tatiana Ramos 
Contacto: tatiiramos9@gmail.com  | https://www.linkedin.com/in/tatiana-ramos-gpti/
