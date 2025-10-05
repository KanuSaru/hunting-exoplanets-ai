import streamlit as st 
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Path of especial variable __file__
from single_predict import predict_single
from batch_prediction import batch_prediction

def main_page():
    
    st.markdown("""
        <h1 style='text-align: center; color: #15B3AC; margin-bottom: 40px;'>
            🌍 Exoplanet Detector
        </h1>
    """, unsafe_allow_html=True)
    
  
    st.markdown("""
        <div style='padding: 20px; border-radius: 10px; margin-bottom: 30px; 
                    background: linear-gradient(135deg, #1E2A78, #FF2E63);
                    color: white; text-align: center;'>
            <h2 style='margin-bottom: 20px;'>Discover New Worlds</h2>
            <p style='font-size: 1.2em;'>
                Using advanced AI to identify potential exoplanets from Kepler telescope data
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #262730; padding: 20px; border-radius: 10px;'>
                <h3 style='color: #15B3AC; margin-bottom: 20px;'>🎯 What can you do?</h3>
                <ul style='color: white; font-size: 1.1em;'>
                    <li style='margin-bottom: 10px;'>✨ <b>Individual Prediction:</b> Analyze single observations</li>
                    <li style='margin-bottom: 10px;'>📊 <b>Batch Analysis:</b> Process multiple data points</li>
                    <li style='margin-bottom: 10px;'>📈 <b>Visualization:</b> Explore detailed statistics</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #262730; padding: 20px; border-radius: 10px;'>
                <h3 style='color: #15B3AC; margin-bottom: 20px;'>🚀 Getting Started</h3>
                <ol style='color: white; font-size: 1.1em;'>
                    <li style='margin-bottom: 10px;'>Select an option from the navigation menu</li>
                    <li style='margin-bottom: 10px;'>Input your stellar data</li>
                    <li style='margin-bottom: 10px;'>Get AI-powered predictions</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)
    
    # Información adicional
    st.markdown("""
        <div style='margin-top: 40px; text-align: center; color: #666;'>
            <p>Based on NASA's Kepler Space Telescope data and machine learning models</p>
        </div>
    """, unsafe_allow_html=True)
    
def sidebar():
    with st.sidebar:
        st.title("Navigation")
        col1, col2, col3 = st.columns(3)
        
        button_style = """
            <style>
            div.stButton > button {
                width: 100%;
                background-color: #262730;
                color: #FFFFFF;
                height: 50px;
                margin: 10px 0px;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            div.stButton > button:hover {
                background-color: #363940;
                color: #FFFFFF;
                border: none;
            }
            </style>
        """
        
        st.markdown(button_style, unsafe_allow_html=True)
        
        if st.button("🏠 Home"):
            st.session_state.page = "Home"
        if st.button("🔭 Individual Prediction"):
            st.session_state.page = "Individual Prediction"
        if st.button("📊 Batch Prediction"):
            st.session_state.page = "Batch Prediction and Plots"
        if st.button("📈 Model Statistics"):
            st.session_state.page = "Model Statistics (General)"
            
        if 'page' not in st.session_state:
            st.session_state.page = "Home"
        
        return st.session_state.page
        
def main():
    
    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    
    page = sidebar()
    
    if page == "Home":
        main_page()
    elif page == "Individual Prediction":
        predict_single()
    elif page == "Batch Prediction and Plots":
        batch_prediction()
    elif 'Model Statistics (General)':
        return
        
if __name__ == "__main__":
    main()