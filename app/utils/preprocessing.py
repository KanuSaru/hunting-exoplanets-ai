import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Define model path
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'ensemble_model_exoplanets.pkl')
PREPROCESSOR_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'preprocessor.pkl')

def fit_preprocessor(df):
    """Fit the scaler with training data and save feature order"""
    feature_columns = df.columns.tolist()
    scaler = StandardScaler()
    scaler.fit(df)
    
    # Save both scaler and feature order
    joblib.dump({
        'scaler': scaler,
        'features': feature_columns
    }, PREPROCESSOR_PATH)

def transform_data(df):
    """Transform new data using saved preprocessor"""
    try:
        # Load preprocessor components
        if os.path.exists(PREPROCESSOR_PATH):
            prep = joblib.load(PREPROCESSOR_PATH)
            scaler = prep['scaler']
            feature_columns = prep['features']
        else:
            raise FileNotFoundError("Preprocessor not found. Please train the model first.")

        # Store disposition if exists for later use
        has_disposition = False
        true_labels = None
        if 'koi_disposition' in df.columns:
            has_disposition = True
            true_labels = df['koi_disposition'].map({'CANDIDATE': 0, 'CONFIRMED': 1})
            df = df.drop(columns=['koi_disposition'])

        # Process data
        processed_df = preprocess_features(df)
        
        # Scale features
        scaled_data = scaler.transform(processed_df)
        scaled_df = pd.DataFrame(scaled_data, columns=processed_df.columns)
        
        # Ensure feature order matches training
        for col in feature_columns:
            if col not in scaled_df.columns:
                scaled_df[col] = 0
                
        return scaled_df[feature_columns], true_labels if has_disposition else scaled_df[feature_columns]
        
    except Exception as e:
        raise ValueError(f"Error preprocessing data: {str(e)}")
   

def preprocess_features(df):
    """Apply feature engineering and cleaning"""
    # Drop unnecessary columns
    columns_to_drop = ['kepid', 'kepoi_name', 'kepler_name', 'koi_pdisposition',
                      'koi_score', 'koi_teq_err1', 'koi_teq_err2', 'koi_tce_plnt_num']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
    
    # Handle categorical variables
    if 'koi_tce_delivname' in df.columns:
        dummies = pd.get_dummies(df['koi_tce_delivname'], prefix='koi_tce_delivname')
        df = df.drop(columns=['koi_tce_delivname'])
        expected_dummies = ['koi_tce_delivname_q1_q16_tce', 
                          'koi_tce_delivname_q1_q17_dr24_tce']
        for col in expected_dummies:
            if col not in dummies.columns:
                dummies[col] = 0
        df = pd.concat([df, dummies[expected_dummies]], axis=1)
    
    # Fill missing values
    df = df.fillna(df.median(numeric_only=True))
    
    # Create engineered features
    if set(['koi_depth', 'koi_duration']).issubset(df.columns):
        df['depth_duration_ratio'] = df['koi_depth'] / (df['koi_duration'] + 1e-6)
    if set(['koi_insol', 'koi_prad']).issubset(df.columns):
        df['insol_prad_ratio'] = df['koi_insol'] / (df['koi_prad'] + 1e-6)
    if set(['koi_steff', 'koi_srad']).issubset(df.columns):
        df['stellar_luminosity_proxy'] = df['koi_steff'] * (df['koi_srad'] ** 2)
    
    return df

def predict_with_preprocessing(raw_data):
    """Complete prediction pipeline with preprocessing"""
    try:
        # Preprocess data
        processed_result = transform_data(raw_data)
        
        # Unpack results
        if isinstance(processed_result, tuple):
            processed_data, true_labels = processed_result
        else:
            processed_data = processed_result
            true_labels = None
        
        # Load and apply model
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
        else:
            raise FileNotFoundError("Model file not found at specified path")
            
        predictions = model.predict(processed_data)
        probabilities = model.predict_proba(processed_data)
        
        return predictions, probabilities, true_labels
        
    except Exception as e:
        raise ValueError(f"Prediction error: {str(e)}")