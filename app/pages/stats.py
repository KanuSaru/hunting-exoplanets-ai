import streamlit as st

def stats():

    st.set_page_config(page_title="📊 Statistics — Graph Explanation", layout="wide")
    st.title("📊 Explanation of the Model’s Graphs for Exoplanet Detection")

    st.markdown("""
    This page presents the **four main visualizations** used to evaluate
    the model’s performance and behavior.  
    Each image represents a different aspect of the analysis and is explained below:
    """)

    # 1️⃣ Class Balance
    st.header("1️⃣ Class Balance")
    st.image("../images/Smote.jpeg", caption="Distribution of classes in the dataset")
    st.markdown("""
    **What does it show?**  
    It represents how many samples exist for each type of astronomical object:  
    - **CONFIRMED**  
    - **CANDIDATE**  

    **Why is it important?**  
    An **imbalanced dataset** (where one class has many more samples than the others)
    can cause the model to learn in a biased way.  
    This graph helps determine whether **resampling or class weighting techniques** are needed
    to improve training balance.
    """)

    # 2️⃣ Correlation with KOI Disposition
    st.header("2️⃣ Correlation with the Independent Variable (KOI Disposition)")
    st.image("../images/Correlation.jpeg", caption="Correlation matrix between features and KOI disposition")
    st.markdown("""
    **What does it show?**  
    The **strength of the relationship** between numerical features and the final disposition (`koi_disposition`).  
    Each cell indicates how strongly two variables are correlated (values range from -1 to 1).  

    **Why is it important?**  
    It helps identify **which features contribute the most** to the model’s decisions
    and whether there are **redundant or less useful variables**.  
    Values close to **1 or -1** indicate strong relationships, while values near **0** indicate weak correlations.
    Negative values indicate that the variables are **inversely proportional**.
    """)

    # 3️⃣ Feature Scatter
    st.header("3️⃣ Feature Scatter Plots")
    st.image("../images/ScatterPlot.jpeg", caption="Relationships between pairs of numerical features")
    st.markdown("""
    **What does it show?**  
    A collection of scatter plots comparing pairs of variables.  
    Each point represents a dataset observation with its corresponding values for two features.  

    **Why is it important?**  
    It helps visualize **trends, patterns, and outliers**:  
    - If points form lines or curves → a relationship exists.  
    - If points are widely scattered → the variables are likely independent.  

    This visualization helps understand the **structure of the data before model training**.
    """)

    # 4️⃣ Confusion Matrix
    st.header("4️⃣ Confusion Matrix")
    st.image("../images/ConfusionMatrix.jpeg", caption="Comparison between predicted and actual values")
    st.markdown("""
    **What does it show?**  
    It compares the **true classes** with the **predicted ones** produced by the model.  
    Each cell indicates how many cases were correctly or incorrectly classified.

    **Why is it important?**  
    It provides a detailed look at the model’s performance:
    - The **main diagonal** represents correct predictions.  
    - Values outside the diagonal correspond to misclassifications.  

    From this matrix, we can derive metrics such as:
    - **Precision**, **Recall**, **F1-score**, **Accuracy**, and **ROC-AUC**,  
    which provide a comprehensive evaluation of model performance.
    """)

if __name__ == "__main__":
    stats()