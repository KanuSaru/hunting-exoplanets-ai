import streamlit as st
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Path of especial variable __file__
from utils.model import load_model, load_model_f


def plot_confusion_matrix(cm):
    """Create confusion matrix plot using matplotlib"""
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    
    # Add colorbar
    plt.colorbar(im)
    
    # Add labels
    classes = ['False Positive', 'Confirmed']
    tick_marks = range(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    
    # Add numbers inside cells
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    return fig

def batch_prediction():
    st.title("Prediction in Batch")
    uploaded_file = st.file_uploader("Upload CSV File", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        model = load_model_f()
        
        try:
            predictions = model.predict(df)
            probabilities = model.predict_proba(df)
            
            results = df.copy()
            results['Prediction'] = predictions
            results['Probability'] = probabilities[:,1]
            
            st.write("Results: ")
            st.dataframe(results)
            
            if 'label' in df.columns:
                st.write("---")
                st.subheader("Model Performance Analysis")
                
                # Create confusion matrix
                cm = confusion_matrix(df['label'], predictions)
                fig = plot_confusion_matrix(cm)
                st.pyplot(fig)
                
                # Show classification report
                report = classification_report(df['label'], predictions)
                st.text("Classification Report:")
                st.text(report)
                  
            csv = results.to_csv(index=False)
            st.download_button(
                "Download Results",
                csv,
                "results_prediction.csv"
                "text/csv"
            )
        except Exception as e:
            st.error(f"Error making predictions: {str(e)}")
            st.info("Please make sure your CSV file has the correct format and columns")
            
        
if __name__ == "__main__":
    batch_prediction()
        