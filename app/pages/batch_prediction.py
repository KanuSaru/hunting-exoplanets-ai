import streamlit as st
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import numpy as np


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.preprocessing import predict_with_preprocessing 

def batch_prediction():
    st.title("Batch Prediction")
    
    # Information box
    st.info("""
    ### Required Data Format
    Please ensure your CSV file contains the necessary Kepler Object of Interest (KOI) features:
    - Transit characteristics (period, duration, depth)
    - Stellar parameters (temperature, radius, surface gravity)
    - Orbital elements (insolation, planetary radius)
    
    The file should follow the Kepler dataset format with columns similar to the NASA Exoplanet Archive.
    """)
    
    # File upload
    uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])
    
    if uploaded_file:
        try:
            # Load and display raw data
            df = pd.read_csv(uploaded_file)
            st.write("### 📊 Raw Data Preview")
            st.dataframe(df.head())

            # Store true labels if they exist
            true_labels = None
            if 'koi_disposition' in df.columns:
                st.write("### Original Class Distribution")
                st.write(df['koi_disposition'].value_counts())
                
                # Filter valid dispositions
                df = df[df['koi_disposition'].isin(['CANDIDATE', 'CONFIRMED'])]
                true_labels = df['koi_disposition'].map({'CANDIDATE': 0, 'CONFIRMED': 1})
                
                st.write("### Filtered Class Distribution")
                st.write(df['koi_disposition'].value_counts())

            try:
                # Use the preprocessing utility to get predictions
                predictions, probabilities, preprocessed_true_labels = predict_with_preprocessing(df)
                
                # Create results dataframe
                results_df = pd.DataFrame({
                    'Prediction': ['CONFIRMED' if p == 1 and prob[1] >= 0.55 else 'CANDIDATE' 
                                 for p, prob in zip(predictions, probabilities)],
                    'Confidence': np.max(probabilities, axis=1),
                    'CANDIDATE_Probability': probabilities[:, 0],
                    'CONFIRMED_Probability': probabilities[:, 1]
                })
                
                # Display results
                st.write("### 🎯 Prediction Results")
                st.dataframe(results_df)
                
                # Show prediction distribution
                st.write("### 📊 Prediction Distribution")
                pred_counts = results_df['Prediction'].value_counts()
                fig, ax = plt.subplots()
                pred_counts.plot(kind='bar')
                plt.title("Distribution of Predictions")
                plt.xlabel("Class")
                plt.ylabel("Count")
                st.pyplot(fig)
                
                # Show confidence distribution
                st.write("### 📈 Confidence Distribution")
                fig, ax = plt.subplots()
                plt.hist(results_df['Confidence'], bins=20)
                plt.title("Distribution of Prediction Confidence")
                plt.xlabel("Confidence Score")
                plt.ylabel("Count")
                st.pyplot(fig)
                
                # Create confusion matrix if true labels exist
                if preprocessed_true_labels is not None:
                    st.write("### 🎯 Model Performance")
                    cm = confusion_matrix(preprocessed_true_labels, predictions)
                    
                    fig, ax = plt.subplots(figsize=(8, 6))
                    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                              xticklabels=['CANDIDATE', 'CONFIRMED'],
                              yticklabels=['CANDIDATE', 'CONFIRMED'])
                    plt.title('Confusion Matrix')
                    plt.xlabel('Predicted')
                    plt.ylabel('Actual')
                    st.pyplot(fig)
                    
                    st.write("### 📊 Classification Metrics")
                    report = classification_report(true_labels, predictions,
                                                target_names=['CANDIDATE', 'CONFIRMED'])
                    st.text(report)
                    
                    accuracy = (cm[0,0] + cm[1,1]) / cm.sum()
                    st.write(f"Overall Accuracy: {accuracy:.2%}")
                
                # Download results
                csv = results_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Predictions",
                    data=csv,
                    file_name="exoplanet_predictions.csv",
                    mime="text/csv"
                )
                
            except Exception as e:
                st.error(f"Prediction error: {str(e)}")
                st.write("Please check the input data format and try again.")
                
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
            st.write("Please ensure your file follows the required format.")

if __name__ == "__main__":
    batch_prediction()