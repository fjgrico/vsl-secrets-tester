import streamlit as st

st.title("🧪 TEST DE SECRETS")

st.markdown("### 🔍 Verificando claves de configuración")

# Mostrar todas las claves disponibles
st.write("📋 Claves detectadas:", list(st.secrets.keys()))

# Comprobar si existe la clave de ElevenLabs
if "ELEVEN_API_KEY" in st.secrets:
    st.success("✅ Clave ELEVEN_API_KEY detectada correctamente")
    st.code(st.secrets["ELEVEN_API_KEY"])
else:
    st.error("❌ No se encontró la clave ELEVEN_API_KEY. Revisa tu secrets.toml")

