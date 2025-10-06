import streamlit as st
import pandas as pd
import io
from PIL import Image
import os

def load_image(image_path):
    try:
        return Image.open(image_path)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

def stats():
    st.set_page_config(page_title="📊 Model Statistics & Analysis", layout="wide")
    
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main-header {
            color: #FF4B4B;
            text-align: center;
            font-size: 3em;
            margin-bottom: 1em;
        }
        .section-header {
            color: #15B3AC;
            margin-top: 2em;
        }
        .highlight-box {
            background-color: #262730;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Main Title with custom styling
    st.markdown("<h1 class='main-header'>🚀 Model Analysis & Performance Dashboard</h1>", unsafe_allow_html=True)

    # Introduction
    st.markdown("""
    <div class='highlight-box'>
        <h3 style='color: #15B3AC;'>🎯 Overview</h3>
        <p>Explore our model's performance through four key visualizations. Each graph provides unique insights 
        into how our AI detects potential exoplanets in the Kepler Space Telescope data.</p>
    </div>
    """, unsafe_allow_html=True)

    # Colab Notebook Section
    st.markdown("""
    <div class='highlight-box'>
        <h3 style='color: #FF4B4B;'>🔬 Deep Dive Analysis</h3>
        <p>For a detailed exploration of our model's development and testing, check out Test #3 in our Colab notebook. 
        This test represents our most successful approach, featuring SMOTE balancing and advanced ensemble techniques.</p>
        <br>
        <h4>📚 Access the Complete Analysis:</h4>
        <a href="https://colab.research.google.com/drive/1JHZbBrR6_p01opTt7snMV8J7gVHdHEFW?usp=sharing" 
           target="_blank" 
           style="background-color: #FF4B4B; 
                  color: white; 
                  padding: 10px 20px; 
                  border-radius: 5px; 
                  text-decoration: none; 
                  display: inline-block;
                  margin-top: 10px;">
            🔗 Open Jupyter Notebook in Google Colab
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("📥 Download Resources"):
        col1, col2 = st.columns(2)
        
        with col1:
            # Load and prepare Kepler data for download
            try:
                df = pd.read_csv('../data/Kepler.csv')
                # Convert dataframe to CSV string
                csv_buffer = io.StringIO()
                df.to_csv(csv_buffer, index=False)
                csv_str = csv_buffer.getvalue()
                
                st.download_button(
                    label="📊 Download Kepler Dataset (CSV)",
                    data=csv_str,
                    file_name="kepler_data.csv",
                    mime="text/csv",
                    help="Download the original Kepler Space Telescope dataset"
                )
            except Exception as e:
                st.error(f"Error loading Kepler data: {str(e)}")
        
        with col2:
            # Add a link to the data documentation
            st.markdown("""
            <div style='background-color: #262730; padding: 15px; border-radius: 5px;'>
                <h4 style='color: #15B3AC;'>📚 Dataset Information</h4>
                <p style='color: white;'>
                    The Kepler dataset contains observations of potential exoplanet candidates, including:
                    <ul style='color: white;'>
                        <li>Transit characteristics</li>
                        <li>Stellar parameters</li>
                        <li>Orbital elements</li>
                    </ul>
                </p>
                <a href="https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative" 
                   target="_blank" 
                   style="background-color: #15B3AC; 
                          color: white; 
                          padding: 8px 15px; 
                          border-radius: 5px; 
                          text-decoration: none; 
                          display: inline-block;
                          margin-top: 10px;">
                    📖 Official Kepler Documentation
                </a>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("""
    <div class='highlight-box'>
        <h3 style='color: #15B3AC;'>🤖 Model Architecture</h3>
        <div style='display: flex; justify-content: space-between; flex-wrap: wrap;'>
            <div style='flex: 1; min-width: 200px; margin: 10px;'>
                <h4 style='color: #FF4B4B;'>Ensemble Components</h4>
                <ul>
                    <li>Random Forest (300 estimators)</li>
                    <li>LightGBM (300 estimators)</li>
                    <li>XGBoost (300 estimators)</li>
                </ul>
            </div>
            <div style='flex: 1; min-width: 200px; margin: 10px;'>
                <h4 style='color: #FF4B4B;'>Data Processing</h4>
                <ul>
                    <li>StandardScaler normalization</li>
                    <li>SMOTE class balancing</li>
                    <li>Feature engineering</li>
                </ul>
            </div>
            <div style='flex: 1; min-width: 200px; margin: 10px;'>
                <h4 style='color: #FF4B4B;'>Training Details</h4>
                <ul>
                    <li>70/30 train-test split</li>
                    <li>Soft voting ensemble</li>
                    <li>Cross-validation: 10-fold</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <style>
        .metric-card {
            background-color: #262730;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            border: 1px solid #15B3AC;
        }
        .metric-value {
            font-size: 24px;
            font-weight: bold;
            color: #FF4B4B;
        }
        .metric-label {
            color: #15B3AC;
            font-size: 16px;
            margin-top: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4,col5 = st.columns(5)

    with col1:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">87.45%</div>
                <div class="metric-label">Accuracy</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">89.56%</div>
                <div class="metric-label">Recall</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">88.92%</div>
                <div class="metric-label">Precision</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">89.24%</div>
                <div class="metric-label">F1 Score</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-value">94.05%</div>
                <div class="metric-label">ROC AUC</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
    <div class='highlight-box' style='margin-top: 20px;'>
        <h4 style='color: #FF4B4B;'>📊 Understanding the Metrics</h4>
        <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;'>
            <div>
                <h5 style='color: #15B3AC;'>Accuracy (87.45%)</h5>
                <p style='color: white;'>
                    Overall correctness of predictions. Represents the proportion of both correct exoplanet 
                    identifications and correct rejections out of all cases.
                </p>
            </div>
            <div>
                <h5 style='color: #15B3AC;'>Recall (89.56%)</h5>
                <p style='color: white;'>
                    Also known as Sensitivity. Shows how well the model identifies actual exoplanets, 
                    representing the percentage of real exoplanets correctly identified.
                </p>
            </div>
            <div>
                <h5 style='color: #15B3AC;'>Precision (88.92%)</h5>
                <p style='color: white;'>
                    Indicates prediction quality. Of all objects our model identified as exoplanets, 
                    this percentage were actually confirmed exoplanets.
                </p>
            </div>
            <div>
                <h5 style='color: #15B3AC;'>F1 Score (89.24%)</h5>
                <p style='color: white;'>
                    Harmonic mean of Precision and Recall. Provides a single score that balances both metrics, 
                    particularly useful when seeking a balanced model performance.
                </p>
            </div>
            <div>
                <h5 style='color: #15B3AC;'>ROC AUC (94.05%)</h5>
                <p style='color: white;'>
                    Area Under the ROC Curve. Measures the model's ability to distinguish between classes. 
                    Our score indicates excellent discrimination capability.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("""
        <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
            margin: 20px 0;
        }
        .grid-item {
            background-color: #262730;
            border-radius: 10px;
            padding: 20px;
            height: 100%;
            border: 1px solid rgba(21, 179, 172, 0.1);
        }
        .grid-item img {
            width: 100%;
            height: 300px;
            object-fit: contain;
            border-radius: 5px;
            margin: 10px 0;
        }
        .insights-box {
            margin-top: 15px;
            padding: 15px;
            background-color: rgba(21, 179, 172, 0.1);
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Start grid layout - Replace all your current visualization sections with this
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)

        # Row 1: Class Distribution and ROC Curve
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="grid-item">
                <h2 style='color: #15B3AC;'>1️⃣ Class Distribution Analysis</h2>
            </div>
        """, unsafe_allow_html=True)
        
        image = load_image("../images/Smote.jpeg")
        if image:
            st.image(image, use_container_width=True)
            
        st.markdown("""
            <div class="insights-box">
                <h4 style='color: #FF4B4B;'>📊 Distribution Insights</h4>
                <ul style='color: white;'>
                    <li>Before and after SMOTE balancing</li>
                    <li>Equal class representation achieved</li>
                    <li>Enhanced training data quality</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="grid-item">
                <h2 style='color: #15B3AC;'>2️⃣ ROC Curve Analysis</h2>
            </div>
        """, unsafe_allow_html=True)
        
        image = load_image("../images/ROC.jpeg")
        if image:
            st.image(image, use_container_width=True)
            
        st.markdown("""
            <div class="insights-box">
                <h4 style='color: #FF4B4B;'>📈 ROC Analysis Insights</h4>
                <ul style='color: white;'>
                    <li>Outstanding AUC score of 0.9405</li>
                    <li>Excellent discrimination capability</li>
                    <li>Robust across different thresholds</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Row 2: Correlation and Feature Interactions
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
            <div class="grid-item">
                <h2 style='color: #15B3AC;'>3️⃣ Feature Correlation Matrix</h2>
            </div>
        """, unsafe_allow_html=True)
        
        image = load_image("../images/Correlation.jpeg")
        if image:
            st.image(image, use_container_width=True)
            
        st.markdown("""
            <div class="insights-box">
                <h4 style='color: #FF4B4B;'>🔍 Correlation Insights</h4>
                <ul style='color: white;'>
                    <li>Key feature relationships identified</li>
                    <li>Strong predictive indicators found</li>
                    <li>Feature importance validation</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="grid-item">
                <h2 style='color: #15B3AC;'>4️⃣ Feature Interactions</h2>
            </div>
        """, unsafe_allow_html=True)
        
        image = load_image("../images/ScatterPlot.jpeg")
        if image:
            st.image(image, use_container_width=True)
            
        st.markdown("""
            <div class="insights-box">
                <h4 style='color: #FF4B4B;'>📈 Pattern Analysis</h4>
                <ul style='color: white;'>
                    <li>Clear feature relationships</li>
                    <li>Distinct class separation</li>
                    <li>Predictive patterns revealed</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Row 3: Confusion Matrix and Precision-Recall
    col5, col6 = st.columns(2)
    with col5:
        st.markdown("""
            <div class="grid-item">
                <h2 style='color: #15B3AC;'>5️⃣ Confusion Matrix</h2>
            </div>
        """, unsafe_allow_html=True)
        
        image = load_image("../images/ConfusionMatrix.jpeg")
        if image:
            st.image(image, use_container_width=True)
            
        st.markdown("""
            <div class="insights-box">
                <h4 style='color: #FF4B4B;'>🎯 Classification Results</h4>
                <ul style='color: white;'>
                    <li>High true positive rate achieved</li>
                    <li>Minimal false classifications</li>
                    <li>Balanced performance across classes</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
            <div class="grid-item">
                <h2 style='color: #15B3AC;'>6️⃣ Precision-Recall Curve</h2>
            </div>
        """, unsafe_allow_html=True)
        
        image = load_image("../images/PR_Curve.jpeg")
        if image:
            st.image(image, use_container_width=True)
            
        st.markdown("""
            <div class="insights-box">
                <h4 style='color: #FF4B4B;'>📊 Performance Trade-off</h4>
                <ul style='color: white;'>
                    <li>High precision: 88.92%</li>
                    <li>Strong recall: 89.56%</li>
                    <li>Optimal balance achieved</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Row 4: Metrics and Probability Distribution
    col7, col8 = st.columns(2)
    with col7:
        st.markdown("""
            <div class="grid-item">
                <h2 style='color: #15B3AC;'>7️⃣ Performance Metrics</h2>
            </div>
        """, unsafe_allow_html=True)
        
        image = load_image("../images/Metrics.jpeg")
        if image:
            st.image(image, use_container_width=True)
            
        st.markdown("""
            <div class="insights-box">
                <h4 style='color: #FF4B4B;'>📈 Key Indicators</h4>
                <ul style='color: white;'>
                    <li>Overall accuracy: 87.45%</li>
                    <li>F1-Score: 89.24%</li>
                    <li>Consistent cross-validation results</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col8:
        st.markdown("""
            <div class="grid-item">
                <h2 style='color: #15B3AC;'>8️⃣ Probability Distribution</h2>
            </div>
        """, unsafe_allow_html=True)
        
        image = load_image("../images/Prob_Dist.jpeg")
        if image:
            st.image(image, use_container_width=True)
            
        st.markdown("""
            <div class="insights-box">
                <h4 style='color: #FF4B4B;'>🎯 Classification Confidence</h4>
                <ul style='color: white;'>
                    <li>Clear separation between classes</li>
                    <li>High confidence predictions</li>
                    <li>Robust decision boundaries</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    # Close grid container
    st.markdown('</div>', unsafe_allow_html=True)


    # Final Summary Section
    st.markdown("""
    <div class='highlight-box' style='background-color: #1E1E1E; margin-top: 2em;'>
        <h3 style='color: #FF4B4B;'>🌟 Model Performance Summary</h3>
        <p style='color: white;'>Our ensemble model demonstrates exceptional performance in exoplanet detection:</p>
        <ul style='color: white;'>
            <li>High accuracy and balanced precision-recall metrics</li>
            <li>Excellent discrimination capability (AUC = 0.9405)</li>
            <li>Robust performance across different classification thresholds</li>
            <li>Successfully addresses class imbalance through SMOTE</li>
        </ul>
        <p style='color: #15B3AC; margin-top: 1em;'>
            These results indicate a highly reliable model for exoplanet candidate classification,
            making it a valuable tool for astronomical research.
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    stats()