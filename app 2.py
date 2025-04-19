import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import gspread

st.set_page_config(page_title="🧪 Test Claves", layout="centered")
st.title("🔐 Verificación de secretos en Streamlit Cloud")

# --- Test ELEVEN_API_KEY ---
st.subheader("🔑 Clave ELEVEN_API_KEY")
if "ELEVEN_API_KEY" in st.secrets:
    st.success("✅ Clave detectada correctamente")
    st.code(st.secrets["ELEVEN_API_KEY"])
else:
    st.error("❌ No se encontró ELEVEN_API_KEY en los secrets")

# --- Test google_service_account ---
st.subheader("📁 Claves de cuenta de servicio de Google")
try:
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = st.secrets["google_service_account"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    st.success("✅ Credenciales de Google cargadas correctamente")
    st.code(creds.service_account_email)
except Exception as e:
    st.error(f"❌ Error al cargar credenciales de Google: {e}")
