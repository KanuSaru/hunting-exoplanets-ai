
import streamlit as st
import numpy as np
import joblib  # o torch si usas PyTorch

st.set_page_config(page_title="🧪 Predicción Individual", layout="centered")
st.title("🧪 Predicción de Exoplaneta por Entrada Manual")

# Cargar modelo entrenado
model = joblib.load("modelo_entrenado.pkl")  # ajusta si usas torch

# Campos requeridos por el modelo
st.subheader("🔧 Ingresa los parámetros del objeto celeste")

period = st.number_input("Período orbital (koi_period)", min_value=0.0)
duration = st.number_input("Duración del tránsito (koi_duration)", min_value=0.0)
depth = st.number_input("Profundidad del tránsito (koi_depth)", min_value=0.0)
prad = st.number_input("Radio del planeta (koi_prad)", min_value=0.0)
srad = st.number_input("Radio de la estrella (koi_srad)", min_value=0.0)
steff = st.number_input("Temperatura de la estrella (koi_steff)", min_value=0.0)
insol = st.number_input("Insolación (koi_insol)", min_value=0.0)
snr = st.number_input("Relación señal/ruido (koi_model_snr)", min_value=0.0)
score = st.number_input("Puntuación del modelo (koi_score)", min_value=0.0)

# Botón de predicción
if st.button("🔍 Predecir"):
    input_data = np.array([[period, duration, depth, prad, srad, steff, insol, snr, score]])
    prediction = model.predict(input_data)[0]
    label = {0: "❌ No es un exoplaneta", 1: "✅ Es un exoplaneta", 2: "🕵️ Candidato"}
    st.success(f"Resultado: {label.get(prediction, 'Desconocido')}")
