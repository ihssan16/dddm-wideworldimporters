import pandas as pd
import pyodbc
from config import SOURCE_CONN_STR, TARGET_ENGINE
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore') 

def get_conn():
    return pyodbc.connect(SOURCE_CONN_STR)

def load_dim_temps():
    print("Génération de Dim_Temps...")
    date_range = pd.date_range(start='2013-01-01', end='2026-12-31', freq='D')
    df = pd.DataFrame({'DateComplete': date_range})
    
    df['TempsKey'] = df['DateComplete'].dt.strftime('%Y%m%d').astype(int)
    df['Annee'] = df['DateComplete'].dt.year
    df['Trimestre'] = df['DateComplete'].dt.quarter
    df['Mois'] = df['DateComplete'].dt.month
    df['NomMois'] = df['DateComplete'].dt.month_name(locale='fr_FR.utf8')
    df['Jour'] = df['DateComplete'].dt.day
    df['NomJourSemaine'] = df['DateComplete'].dt.day_name(locale='fr_FR.utf8')
    df['EstWeekend'] = df['DateComplete'].dt.dayofweek.isin([5, 6]).astype(int)
    
    df.to_sql('Dim_Temps', con=TARGET_ENGINE, if_exists='append', index=False)
    print("-> Dim_Temps chargée.")

def load_dim_geographie():
    print("Extraction et Transformation de Dim_Geographie...")
    query = """
        SELECT c.CityID, c.CityName as Ville, sp.StateProvinceName as ProvinceEtat, 
               sp.SalesTerritory as TerritoireDeVente, co.CountryName as Pays, co.Continent 
        FROM Application.Cities c 
        JOIN Application.StateProvinces sp ON c.StateProvinceID = sp.StateProvinceID 
        JOIN Application.Countries co ON sp.CountryID = co.CountryID
    """
    df = pd.read_sql(query, get_conn())
    df.to_sql('Dim_Geographie', con=TARGET_ENGINE, if_exists='append', index=False)
    print("-> Dim_Geographie chargée.")

def load_dim_produit():
    print("Extraction et Transformation de Dim_Produit...")
    query = """
        SELECT si.StockItemID, si.StockItemName as NomProduit, sg.StockGroupName as Categorie, 
               c.ColorName as Couleur, si.Size as Taille, si.TypicalWeightPerUnit as PoidsParUnite 
        FROM Warehouse.StockItems si 
        -- On utilise une jointure pour simplifier le modèle
        LEFT JOIN Warehouse.StockItemStockGroups sisg ON si.StockItemID = sisg.StockItemID 
        LEFT JOIN Warehouse.StockGroups sg ON sisg.StockGroupID = sg.StockGroupID 
        LEFT JOIN Warehouse.Colors c ON si.ColorID = c.ColorID
    """
    df = pd.read_sql(query, get_conn())
    
    # Nettoyage 
    df = df.drop_duplicates(subset=['StockItemID'])
    df.fillna({'Couleur': 'Non défini', 'Taille': 'Standard', 'Categorie': 'Général'}, inplace=True)
    
    df.to_sql('Dim_Produit', con=TARGET_ENGINE, if_exists='append', index=False)
    print("-> Dim_Produit chargée.")

def load_dim_client():
    print("Extraction, IA (Clustering) et Transformation de Dim_Client...")
    query = """
        SELECT c.CustomerID, c.CustomerName, cc.CustomerCategoryName, 
               bg.BuyingGroupName, c.StandardDiscountPercentage, c.PaymentDays
        FROM Sales.Customers c 
        LEFT JOIN Sales.CustomerCategories cc ON c.CustomerCategoryID = cc.CustomerCategoryID 
        LEFT JOIN Sales.BuyingGroups bg ON c.BuyingGroupID = bg.BuyingGroupID
    """
    df = pd.read_sql(query, get_conn())
    df.fillna({'BuyingGroupName': 'Indépendant'}, inplace=True)
    
    # === COMPOSANTE IA : CLUSTERING K-MEANS ===
    # On segmente les clients basés sur leurs habitudes de paiement et remises
    features_ia = df[['StandardDiscountPercentage', 'PaymentDays']].fillna(0)
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(features_ia)
    
    # Mapping des résultats de l'IA en texte lisible pour le tableau de bord
    segment_map = {0: 'Standard', 1: 'Premium', 2: 'VIP'}
    df['Segment_Client'] = [segment_map[c] for c in clusters]
    
    # On retire les colonnes techniques utilisées pour l'IA avant l'insertion
    df = df.drop(columns=['StandardDiscountPercentage', 'PaymentDays'])
    
    df.to_sql('Dim_Client', con=TARGET_ENGINE, if_exists='append', index=False)
    print("-> Dim_Client chargée.")