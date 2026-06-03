import pandas as pd
import pyodbc
from config import SOURCE_CONN_STR, TARGET_ENGINE

def load_fact_ventes():
    print("Extraction et Transformation de Fact_Ventes (Calcul des KPIs)...")
    
    # 1. Extraction des ventes depuis l'OLTP
    conn = pyodbc.connect(SOURCE_CONN_STR)
    query_sales = """
        SELECT il.InvoiceLineID, i.InvoiceDate, i.CustomerID, c.DeliveryCityID as CityID, 
               il.StockItemID, il.Quantity as QuantiteVendu, il.UnitPrice as PrixUnitaire, 
               il.LineProfit as MargeBrute 
        FROM Sales.InvoiceLines il 
        JOIN Sales.Invoices i ON il.InvoiceID = i.InvoiceID 
        JOIN Sales.Customers c ON i.CustomerID = c.CustomerID
    """
    df_sales = pd.read_sql(query_sales, conn)
    conn.close()

    # 2. Création de la clé de temps (Format AAAAMMJJ)
    df_sales['InvoiceDate'] = pd.to_datetime(df_sales['InvoiceDate'])
    df_sales['TempsKey'] = df_sales['InvoiceDate'].dt.strftime('%Y%m%d').astype(int)

    # 3. Calcul des KPIs demandés
    df_sales['ChiffreAffaires'] = df_sales['QuantiteVendu'] * df_sales['PrixUnitaire']
    df_sales['CoutTotal'] = df_sales['ChiffreAffaires'] - df_sales['MargeBrute']

    # 4. Remplacement par les Surrogate Keys du Data Warehouse
    # On récupère les mappings depuis notre nouvelle base
    dim_client = pd.read_sql("SELECT ClientKey, CustomerID FROM Dim_Client", TARGET_ENGINE)
    dim_produit = pd.read_sql("SELECT ProduitKey, StockItemID FROM Dim_Produit", TARGET_ENGINE)
    dim_geo = pd.read_sql("SELECT GeographieKey, CityID FROM Dim_Geographie", TARGET_ENGINE)

    # Jointures Pandas pour fusionner les clés
    df_fact = df_sales.merge(dim_client, on='CustomerID', how='left')
    df_fact = df_fact.merge(dim_produit, on='StockItemID', how='left')
    df_fact = df_fact.merge(dim_geo, on='CityID', how='left')

    # 5. Nettoyage final avant insertion (On garde uniquement les colonnes de la table cible)
    colonnes_finales = [
        'InvoiceLineID', 'ClientKey', 'ProduitKey', 'GeographieKey', 'TempsKey',
        'QuantiteVendu', 'PrixUnitaire', 'ChiffreAffaires', 'CoutTotal', 'MargeBrute'
    ]
    df_fact_clean = df_fact[colonnes_finales]
    
    # Gestion des lignes orphelines (sécurité)
    df_fact_clean.dropna(subset=['ClientKey', 'ProduitKey', 'GeographieKey'], inplace=True)

    # 6. Chargement
    df_fact_clean.to_sql('Fact_Ventes', con=TARGET_ENGINE, if_exists='append', index=False)
    print("-> Fact_Ventes chargée.")