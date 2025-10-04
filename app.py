import streamlit as st
import pandas as pd

st.set_page_config(page_title="🔭 Detección de Exoplanetas", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b1f3a; color: #f0f0f0; }
    h1, h2, h3 { color: #00ffd5; }
    .stButton>button { background-color: #00ffd5; color: black; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🔭 Detección de Exoplanetas con IA")

st.sidebar.header("⚙️ Opciones")
st.sidebar.write("Algun parametro por aqui.")

uploaded_file = st.file_uploader("📁 Subir archivo CSV con datos de exoplanetas", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("👀 Vista previa del archivo")
    st.dataframe(df.head())

    if st.button("🔍 Analizar con IA"):
        st.info("🔧 El modelo aún no está subido si o no.")

    st.download_button(
        label="📥 Descargar CSV procesado",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="resultado.csv",
        mime="text/csv"
    )

st.markdown("---")
st.markdown("Creado por el equipo *Hunting Exoplanets AI* 🚀 | NASA Space Apps Challenge 2025")
