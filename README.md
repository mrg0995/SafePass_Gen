# 🔐 SafePass Gen: Generador de Contraseñas Seguras

Una herramienta de ciberseguridad desarrollada con **Python** y **Streamlit** que permite crear contraseñas robustas utilizando estándares criptográficos avanzados.

## ✨ Características
- 🛡️ **Fuerza Criptográfica**: Utiliza el módulo `secrets` de Python para garantizar una aleatoriedad real y segura.
- ⚙️ **Personalización Total**: Ajusta la longitud (8-32 caracteres) y elige entre mayúsculas, números y símbolos.
- 📊 **Medidor de Seguridad**: Evaluación en tiempo real de la robustez de la contraseña generada (Nivel Débil, Medio o NASA).
- 🕒 **Historial de Sesión**: Guarda tus últimas 5 contraseñas generadas durante la sesión actual para que no las pierdas.
- 📋 **Copiado Rápido**: Formato de visualización que permite copiar la contraseña con un solo clic.

## 🛠️ Tecnologías utilizadas
- **Python 3.x**
- **Streamlit** (Interfaz de usuario)
- **Secrets Module** (Seguridad y generación aleatoria)
- **String Module** (Manejo de caracteres)

## 🚀 Instalación y Uso

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/mrg0995/safepass-gen.git](https://github.com/mrg0995/safepass-gen.git)

2. Instalar las dependencias:
   ```bash
   pip install streamlit
  
3. Ejecutar la aplicación:
   ```bash
   streamlit run password_gen.py
