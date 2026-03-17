import streamlit as st
import secrets
import string

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="SafePass Gen", page_icon="🔐", layout="centered")

# Inicializamos el historial si no existe
if 'historial' not in st.session_state:
    st.session_state.historial = []
if 'last_password' not in st.session_state:
    st.session_state.last_password = ""

def generar_contrasena(largo, mayus, nums, sims):
    caracteres = string.ascii_lowercase
    if mayus: caracteres += string.ascii_uppercase
    if nums:  caracteres += string.digits
    if sims:  caracteres += string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(largo))

# --- 2. BARRA LATERAL ---
st.sidebar.header("⚙️ Configuración")
longitud = st.sidebar.slider("Longitud", 8, 32, 12)

use_upper = st.sidebar.checkbox("Mayúsculas", value=True)
use_digits = st.sidebar.checkbox("Números", value=True)
use_symbols = st.sidebar.checkbox("Símbolos", value=True)

# Sección de Historial en Sidebar
st.sidebar.divider()
st.sidebar.subheader("🕒 Recientes")
if st.session_state.historial:
    for p in st.session_state.historial:
        st.sidebar.text(p)
    
    if st.sidebar.button("🗑️ Limpiar Historial", use_container_width=True):
        st.session_state.historial = []
        st.rerun()
else:
    st.sidebar.info("No hay historial.")

# --- 3. CUERPO PRINCIPAL ---
st.title("🔐 SafePass: Generador de Contraseñas")
st.write("Genera claves seguras con estándar criptográfico.")

if st.button("Generar Nueva Contraseña ⚡", type="primary", use_container_width=True):
    nueva_pass = generar_contrasena(longitud, use_upper, use_digits, use_symbols)
    st.session_state.last_password = nueva_pass
    st.session_state.historial.insert(0, nueva_pass)
    st.session_state.historial = st.session_state.historial[:5]

# Mostrar la contraseña actual si existe
if st.session_state.last_password:
    st.subheader("Tu contraseña segura:")
    st.code(st.session_state.last_password)
    
    # Medidor de seguridad
    puntos = sum([longitud >= 12, use_upper, use_digits, use_symbols])
    
    if puntos <= 2:
        st.error("Nivel: **Débil** ⚠️ (Mejora la configuración)")
    elif puntos == 3:
        st.warning("Nivel: **Media** 🆗")
    else:
        st.success("Nivel: **Robusta** 💪 (Nivel NASA)")
else:
    st.info("Haz clic en el botón para generar tu primera contraseña.")