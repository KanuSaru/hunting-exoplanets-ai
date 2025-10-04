import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="🔭 Detección de Exoplanetas", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b1f3a; color: #f0f0f0; }
    h1, h2, h3 { color: #00ffd5; }
    .stButton>button { background-color: #00ffd5; color: black; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("📄 Navegación")
page = st.sidebar.radio("Ir a:", ["Subir CSV", "Predicción Individual"])

if page == "Subir CSV":
    st.title("🔭 Detección de Exoplanetas con IA")
    uploaded_file = st.file_uploader("📁 Sube tu archivo CSV con datos de exoplanetas", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("👀 Vista previa del archivo")
        st.dataframe(df.head())
        if st.button("🔍 Analizar con IA"):
            st.info("🔧 El modelo aún no está conectado. Tu equipo puede integrar aquí la función de predicción.")
        st.download_button(
            label="📥 Descargar CSV procesado",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="resultado.csv",
            mime="text/csv"
        )

elif page == "Predicción Individual":
    st.title("🧪 Predicción de Exoplaneta por Entrada Manual")

    period = st.number_input("Período orbital (koi_period)", min_value=0.0)
    duration = st.number_input("Duración del tránsito (koi_duration)", min_value=0.0)
    depth = st.number_input("Profundidad del tránsito (koi_depth)", min_value=0.0)
    prad = st.number_input("Radio del planeta (koi_prad)", min_value=0.0)
    srad = st.number_input("Radio de la estrella (koi_srad)", min_value=0.0)
    steff = st.number_input("Temperatura de la estrella (koi_steff)", min_value=0.0)
    insol = st.number_input("Insolación (koi_insol)", min_value=0.0)
    snr = st.number_input("Relación señal/ruido (koi_model_snr)", min_value=0.0)
    score = st.number_input("Puntuación del modelo (koi_score)", min_value=0.0)

    if st.button("🔍 Predecir"):
        st.info("🔧 El modelo aún no está conectado. Cuando esté disponible, se mostrará aquí el resultado.")

st.markdown("---")
st.markdown("Creado por el equipo *Hunting Exoplanets AI* 🚀 | NASA Space Apps Challenge 2025")
