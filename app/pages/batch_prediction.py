import streamlit as st
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Path of especial variable __file__
from utils.model import load_model, load_model_f


def batch_prediction():
    return

if __name__ == "__main__":
    batch_prediction()
    