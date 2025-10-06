# hunting-exoplanets-ai

# hunting-exoplanets-ai


---

markdown
# 🌌 A World Away — Hunting for Exoplanets with AI

This project leverages **machine learning** to identify potential **exoplanets** using NASA’s **Kepler Object of Interest (KOI)** dataset.  
Developed for the **NASA Space Apps Challenge**, it unites **astronomy**, **data science**, and **artificial intelligence** in an interactive web application built with **Streamlit**.

---

## 🚀 Overview

The system enables users to:
1. 🏠 **Explore model performance and overview** (Main page)  
2. 📁 **Upload CSV files** for batch exoplanet predictions  
3. 🔭 **Input parameters manually** for single candidate analysis  
4. 📈 **Visualize model results** and understand the science behind each graph  

The trained ensemble model achieves an **accuracy of 87–88%**, which is **slightly higher than that reported** in  
[*Exoplanet detection using machine learning* — MNRAS, 2022](https://academic.oup.com/mnras/article/513/4/5505/6472249).  

We mention this humbly — as a sign of the progress that can be made when academic research meets student innovation.

---

## 🧠 Model Details

- **Dataset:** NASA Kepler KOI Catalog (`app/data/Kepler.csv`)  
- **Processed dataset:** `app/data/processed_kepler.csv`  
- **Model file:** `app/models/ensemble_model_exoplanets.pkl`  
- **Training notebook:** `app/notebooks/hunting_exoplanets_notebook.ipynb`  
- **Algorithm:** Ensemble learning (Random Forest + Gradient Boosting)  
- **Performance Metrics:**  
  - Accuracy: **0.8745**  
  - Recall: **0.8956**  
  - Precision: **0.8892**  
  - F1-score: **0.8924**  
  - ROC-AUC: **0.9405**

---

## 🛠 Technologies Used

- **Python 3.10+**
- **Streamlit** – interactive web app framework  
- **scikit-learn**, **Pandas**, **NumPy**, **Matplotlib**, **Joblib**  
- **Jupyter Notebook** – model training and experimentation  
- **uv** – lightweight dependency and environment manager  

---

## 🧩 Project Structure
app/
├── data/
│   ├── Kepler.csv
│   └── processed_kepler.csv
│
├── images/
│   ├── ConfusionMatrix.jpeg
│   ├── Correlation.jpeg
│   ├── Metrics.jpeg
│   ├── PR_Curve.jpeg
│   ├── Prob_Dist.jpeg
│   ├── ROC.jpeg
│   ├── ScatterPlot.jpeg
│   └── Smote.jpeg
│
├── models/
│   ├── ensemble_model_exoplanets.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   └── hunting_exoplanets_notebook.ipynb
│
├── pages/
│   ├── __init__.py
│   ├── app.py
│   ├── batch_prediction.py
│   ├── single_predict.py
│   └── stats.py
│
├── utils/
│   ├── __init__.py
│   ├── model.py
│   ├── preprocessing.py
│   └── preprocessor.py
│
├── __init__.py
└── main.py
`

The **sidebar** in the Streamlit app loads all four functional pages automatically.

---

## ⚙ Installation

Clone this repository:
bash
git clone https://github.com/KanuSaru/hunting-exoplanets-ai.git
cd hunting-exoplanets-ai

### Option 1 — Standard installation

bash
pip install -r requirements.txt


### Option 2 — Using **uv** (recommended)

> [uv](https://github.com/astral-sh/uv) is a modern, ultra-fast dependency and environment manager for Python.
> It automatically installs the required packages and handles isolated environments.

Run:

bash
cd app/
uv run main.py

This will download dependencies automatically.

---

## ▶ Running the App

Once dependencies are installed, launch the Streamlit interface:

bash
cd app/pages
streamlit run app.py
```

Then open the local URL (usually [http://localhost:8501](http://localhost:8501)) in your browser.

---

## 🌍 Features

* *Batch Prediction:* Upload a .csv file with stellar and planetary parameters to classify multiple entries.
* *Single Prediction:* Input parameters manually to evaluate one potential exoplanet.
* *Visual Analysis:* Includes balance charts, correlation heatmaps, scatter plots, ROC/PR curves, and confusion matrices.
* *Educational Design:* Each graph and metric is explained in plain language to promote understanding.

---

## 🪐 Images & Graphs

All visual assets are stored in app/images/ and include:

* Metrics.jpeg – overall model performance
* ROC.jpeg and PR_Curve.jpeg – classifier evaluation curves
* ConfusionMatrix.jpeg – comparison of predictions vs. true labels
* Correlation.jpeg and ScatterPlot.jpeg – data relationship analysis
* Smote.jpeg – visualization of class balance after resampling
* Prob_Dist.jpeg – probability distribution of predictions

---

## 💡 Inspiration

This project was inspired by the scientific study
[Exoplanet detection using machine learning (MNRAS, 2022)](https://academic.oup.com/mnras/article/513/4/5505/6472249).
