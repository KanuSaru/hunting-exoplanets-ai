import os
import joblib


def get_model_path(filename):
    """Get absolute path to model file"""
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Gets utils directory
    app_dir = os.path.dirname(current_dir)  # Gets app directory
    model_dir = os.path.join(app_dir, 'models')  # Points to models directory at app level
    return os.path.join(model_dir, filename)

def load_model():
    try:
        model_path = get_model_path('ensemble_model.pkl')
        model = joblib.load(model_path)
        return model
    
    except FileNotFoundError:
        raise FileNotFoundError("Model file not found.")

def load_model_f():
    try:
        model_path = get_model_path('ensemble_model_final.pkl')
        model = joblib.load(model_path)
        return model
    
    except FileNotFoundError:
        raise FileNotFoundError("Model file not found.")
