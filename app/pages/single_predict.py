import streamlit as st
import numpy as np
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Path of especial variable __file__

from utils.model import load_model, load_model_f

def get_default_values():
    try:
        df = pd.read_csv('../data/Kepler.csv')
        return df.median(numeric_only=True)
    except Exception as e:
        st.error(f"Error loading default values: {str(e)}")
        return None    

def predict_single():
    st.title("Individual Prediction")
    col1, col2 = st.columns([2,1])
    with col1:
        st.info("""
        ### Instructions
        1. Fill in the required basic parameters
        2. Optionally, expand sections for more detailed parameters
        3. Click predict to see results
        """)
    with col2:
        st.warning("⚠️ Default values are used for unfilled fields")
    
    try:
        # User inputs in a form
        with st.form("prediction_form"):
            
            default_values = get_default_values()
            if default_values is None:
                st.error("Could not load default values")
                return
            
            st.subheader("Required Parameters")
            koi_duration = st.number_input(
                "Transit Duration (hours)", 
                min_value=0.0, 
                max_value=24.0,
                help="Time it takes for the planet to cross in front of its star"
            )
            
            koi_depth = st.number_input(
                "Transit Depth (ppm)",
                min_value=0.0,
                help="Decrease in the brightness of the star during transit"
            )
            
            koi_steff = st.number_input(
                "Effective Temperature of the Star (K)",
                min_value=2000.0,
                max_value=12000.0,
                help="Surface temperature of the star"
            )
            
            koi_slogg = st.number_input(
                "Stellar Surface Gravity (log10[cm/s^2])",
                min_value=0.0,
                max_value=5.0,
                help="Measurement of gravity on the surface of the star"
            )
            
            # Optional Parameters in Expanders
            with st.expander("Orbital Parameters"):
                koi_period = st.number_input("Orbital Period (days)", value=0.0)
                koi_impact = st.number_input("Impact Parameter", value=0.0)
                koi_teq = st.number_input("Equilibrium Temperature (K)", value=0.0)
                
            with st.expander("Planet Parameters"):
                koi_prad = st.number_input("Planet Radius (Earth radii)", value=0.0)
                koi_insol = st.number_input("Insolation Flux (Earth flux)", value=0.0)
                
            with st.expander("Star Parameters"):
                koi_srad = st.number_input("Stellar Radius (Solar radii)", value=0.0)
                ra = st.number_input("Right Ascension", value=0.0)
                dec = st.number_input("Declination", value=0.0)
                koi_kepmag = st.number_input("Kepler Magnitude", value=0.0)

            with st.expander("Flag Parameters"):
                koi_fpflag_nt = st.checkbox("NT Flag")
                koi_fpflag_ss = st.checkbox("SS Flag")
                koi_fpflag_co = st.checkbox("CO Flag")
                koi_fpflag_ec = st.checkbox("EC Flag")
                
            
            submitted = st.form_submit_button("Predict")
          
        if submitted:
            with st.spinner('Processing prediction...'):
                try:
                    default_values = get_default_values()
                    
                    if default_values is None:
                        st.error("Could not load default values")
                        return
               
                    # Default Values
                    input_data = {
                        'koi_duration': koi_duration,
                        'koi_depth': koi_depth,
                        'koi_steff': koi_steff,
                        'koi_slogg': koi_slogg,
                    }
                    
                    optional_params = {
                        'koi_period': koi_period if koi_period != 0.0 else default_values['koi_period'],
                        'koi_impact': koi_impact if koi_impact != 0.0 else default_values['koi_impact'],
                        'koi_teq': koi_teq if koi_teq != 0.0 else default_values['koi_teq'],
                        'koi_prad': koi_prad if koi_prad != 0.0 else default_values['koi_prad'],
                        'koi_insol': koi_insol if koi_insol != 0.0 else default_values['koi_insol'],
                        'koi_srad': koi_srad if koi_srad != 0.0 else default_values['koi_srad'],
                        'ra': ra if ra != 0.0 else default_values['ra'],
                        'dec': dec if dec != 0.0 else default_values['dec'],
                        'koi_kepmag': koi_kepmag if koi_kepmag != 0.0 else default_values['koi_kepmag'],
                        'koi_fpflag_nt': int(koi_fpflag_nt),
                        'koi_fpflag_ss': int(koi_fpflag_ss),
                        'koi_fpflag_co': int(koi_fpflag_co),
                        'koi_fpflag_ec': int(koi_fpflag_ec)
                    }
                    
                    default_fields = {
                        'koi_period_err1': default_values['koi_period_err1'],
                        'koi_period_err2': default_values['koi_period_err2'],
                        'koi_time0bk': default_values['koi_time0bk'],
                        'koi_time0bk_err1': default_values['koi_time0bk_err1'],
                        'koi_time0bk_err2': default_values['koi_time0bk_err2'],
                        'koi_impact_err1': default_values['koi_impact_err1'],
                        'koi_impact_err2': default_values['koi_impact_err2'],
                        'koi_duration_err1': default_values['koi_duration_err1'],
                        'koi_duration_err2': default_values['koi_duration_err2'],
                        'koi_depth_err1': default_values['koi_depth_err1'],
                        'koi_depth_err2': default_values['koi_depth_err2'],
                        'koi_prad_err1': default_values['koi_prad_err1'],
                        'koi_prad_err2': default_values['koi_prad_err2'],
                        'koi_insol_err1': default_values['koi_insol_err1'],
                        'koi_insol_err2': default_values['koi_insol_err2'],
                        'koi_steff_err1': default_values['koi_steff_err1'],
                        'koi_steff_err2': default_values['koi_steff_err2'],
                        'koi_slogg_err1': default_values['koi_slogg_err1'],
                        'koi_slogg_err2': default_values['koi_slogg_err2'],
                        'koi_srad_err1': default_values['koi_srad_err1'],
                        'koi_srad_err2': default_values['koi_srad_err2'],
                        'koi_model_snr': default_values['koi_model_snr'],
                        'koi_tce_delivname_q1_q17_dr24_tce': 1,
                        'koi_tce_delivname_q1_q17_dr25_tce': 0
                    }
                    
                    input_data.update(optional_params)
                    input_data.update(default_fields)
                    
                    input_data['depth_duration_ratio'] = input_data['koi_depth'] / (input_data['koi_duration'] + 1e-6)
                    input_data['insol_prad_ratio'] = input_data['koi_insol'] / (input_data['koi_prad'] + 1e-6)
                    input_data['stellar_luminosity_proxy'] = input_data['koi_steff'] * (input_data['koi_srad'] ** 2)
                    
                    features = pd.DataFrame([input_data])
                    model = load_model_f()
                    prediction = model.predict(features)[0]
                    probability = model.predict_proba(features)[0]
                    
                    # Show results in an expander
                    with st.expander("Prediction Results", expanded=True):
                        if prediction == 1:
                            st.success(f"Possible Exoplanet! (Confidence: {probability[1]:.2%})")
                            st.balloons()
                        else:
                            st.error(f"Probably not an exoplanet (Confidence: {probability[0]:.2%})")
                        
                        # Show additional details
                        st.write("---")
                        st.caption("Detailed Probabilities:")
                        st.json({
                            "False Positive": f"{probability[0]:.3f}",
                            "Confirmed Exoplanet": f"{probability[1]:.3f}"
                        })
                        
                except Exception as e:
                    st.error(f"Error during prediction: {str(e)}")
                    st.info("Please check your input values and try again")

    except Exception as e:
        st.error(f"Application Error: {str(e)}")
        st.info("Please refresh the page and try again")
    
if __name__ == "__main__":
    predict_single()