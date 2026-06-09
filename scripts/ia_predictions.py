import pandas as pd
from config import TARGET_ENGINE
from sklearn.linear_model import LinearRegression
import numpy as np

def generate_sales_forecast():
    print("Génération des prévisions de ventes avec IA (Régression Linéaire)...")
    
    # Lire les ventes historiques groupées par mois
    query = """
        SELECT t.Annee, t.Mois, SUM(f.ChiffreAffaires) as CA_Mensuel
        FROM Fact_Ventes f
        JOIN Dim_Temps t ON f.TempsKey = t.TempsKey
        GROUP BY t.Annee, t.Mois
        ORDER BY t.Annee, t.Mois
    """
    df = pd.read_sql(query, TARGET_ENGINE)
    
    df['TimeIndex'] = range(1, len(df) + 1)
    
    X = df[['TimeIndex']]
    y = df['CA_Mensuel']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Prédire les 3 prochains mois
    last_index = df['TimeIndex'].max()
    future_X = pd.DataFrame({'TimeIndex': [last_index + 1, last_index + 2, last_index + 3]})
    predictions = model.predict(future_X)
    
    # Créer le DataFrame final 
    df_predictions = pd.DataFrame({
        'MoisPrevision': ['Mois + 1', 'Mois + 2', 'Mois + 3'],
        'ChiffreAffairesPrevu': np.round(predictions, 2)
    })
    
    df_predictions.to_sql('Previsions_Ventes', con=TARGET_ENGINE, if_exists='replace', index=False)
    print("-> Table de prévisions générée avec succès.")