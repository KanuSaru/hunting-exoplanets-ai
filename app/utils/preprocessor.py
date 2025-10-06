import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

def create_preprocessor():
    try:
        # Cargar los datos de entrenamiento
        df = pd.read_csv('../data/Kepler.csv')
        
        # Filtrar solo CANDIDATE y CONFIRMED
        df = df[df['koi_disposition'].isin(['CONFIRMED', 'CANDIDATE'])]
        
        # Eliminar columnas innecesarias
        columns_to_drop = ['kepid', 'kepoi_name', 'kepler_name', 'koi_pdisposition',
                          'koi_score', 'koi_teq_err1', 'koi_teq_err2', 'koi_tce_plnt_num',
                          'koi_disposition']  # También eliminamos la columna objetivo
        df = df.drop(columns=columns_to_drop)
        
        # Manejar variables categóricas
        if 'koi_tce_delivname' in df.columns:
            dummies = pd.get_dummies(df['koi_tce_delivname'], prefix='koi_tce_delivname')
            df = df.drop(columns=['koi_tce_delivname'])
            expected_dummies = ['koi_tce_delivname_q1_q16_tce', 
                              'koi_tce_delivname_q1_q17_dr24_tce']
            dummies = dummies[expected_dummies]
            df = pd.concat([df, dummies], axis=1)
        
        # Rellenar valores faltantes
        df = df.fillna(df.median(numeric_only=True))
        
        # Crear características ingenieradas
        df['depth_duration_ratio'] = df['koi_depth'] / (df['koi_duration'] + 1e-6)
        df['insol_prad_ratio'] = df['koi_insol'] / (df['koi_prad'] + 1e-6)
        df['stellar_luminosity_proxy'] = df['koi_steff'] * (df['koi_srad'] ** 2)
        
        # Ajustar el escalador
        scaler = StandardScaler()
        scaler.fit(df)
        
        # Guardar el preprocesador
        preprocessor = {
            'scaler': scaler,
            'features': df.columns.tolist()
        }
        
        # Asegurar que existe el directorio models
        os.makedirs('../models', exist_ok=True)
        
        # Guardar el preprocesador
        joblib.dump(preprocessor, '../models/preprocessor.pkl')
        print("¡Preprocesador creado y guardado exitosamente!")
        print(f"Características guardadas: {df.columns.tolist()}")
        
    except Exception as e:
        print(f"Error creando el preprocesador: {str(e)}")

if __name__ == "__main__":
    create_preprocessor()