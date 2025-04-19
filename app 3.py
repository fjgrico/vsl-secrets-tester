import streamlit as st
import os
from TTS.api import TTS
from elevenlabs import ElevenLabs, Voice, VoiceSettings

st.set_page_config(page_title="🎙️ Generador de VSL con voz", layout="centered")
st.title("🎙️ Narrador VSL con IA")

guion = st.text_area("✍️ Pega aquí tu guion VSL", height=250)

modo = st.radio("Selecciona el tipo de narración:", ["🎧 Voz gratuita (open source)", "🎙️ Voz profesional (ElevenLabs)"])

audio_path = ""

if st.button("🎬 Generar narración"):
    with st.spinner("Generando narración..."):

        try:
            if modo == "🎙️ Voz profesional (ElevenLabs)":
                if "ELEVEN_API_KEY" not in st.secrets:
                    st.error("❌ No se encontró la clave ELEVEN_API_KEY en los secrets.")
                else:
                    client = ElevenLabs(api_key=st.secrets["ELEVEN_API_KEY"])
                    audio = client.generate(
                        text=guion,
                        model="eleven_multilingual_v2",
                        voice=Voice(
                            voice_id="EXAVITQu4vr4xnSDxMaL",
                            settings=VoiceSettings(stability=0.4, similarity_boost=0.8)
                        )
                    )
                    audio_path = "narracion_profesional.mp3"
                    with open(audio_path, "wb") as f:
                        for chunk in audio:
                            f.write(chunk)
                    st.audio(audio_path)
                    st.success("✅ Voz profesional generada")

            else:
                tts = TTS(model_name="tts_models/es/css10/vits", progress_bar=False, gpu=False)
                audio_path = "narracion_gratis.wav"
                tts.tts_to_file(text=guion, file_path=audio_path)
                st.audio(audio_path)
                st.success("✅ Voz gratuita generada")

            with open(audio_path, "rb") as file:
                st.download_button(
                    label="⬇️ Descargar narración",
                    data=file,
                    file_name=audio_path,
                    mime="audio/wav" if audio_path.endswith(".wav") else "audio/mpeg"
                )

        except Exception as e:
            st.error(f"❌ Error al generar audio: {e}")