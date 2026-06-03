from etl_dimensions import load_dim_temps, load_dim_geographie, load_dim_produit, load_dim_client
from etl_faits import load_fact_ventes
from ia_predictions import generate_sales_forecast

if __name__ == "__main__":
    print("  DÉMARRAGE DU PIPELINE ETL WIDE WORLD IMPORTERS  ")
    
    # 1. Chargement des Dimensions 
    load_dim_temps()
    load_dim_geographie()
    load_dim_produit()
    load_dim_client()
    
    # 2. Chargement de la table de Faits 
    load_fact_ventes()
    
    # 3. Application des modèles d'IA sur les données consolidées
    generate_sales_forecast()
    
    print(" PIPELINE TERMINÉ AVEC SUCCÈS. LE DATA WAREHOUSE EST PRÊT. ")