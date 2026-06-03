# 📊 Projet Data-Driven Decision Making
## Wide World Importers — Analyse Décisionnelle & Prévision des Ventes



---

## 🎯 Contexte

Ce projet applique un pipeline décisionnel complet basé sur la donnée, dans le domaine de la **distribution e-commerce** (Wide World Importers). Il couvre l'intégralité du cycle : de la collecte des données jusqu'aux recommandations stratégiques et au plan A/B Test.

**Question décisionnelle centrale :**  
> Quels segments clients et quelles catégories de produits maximisent le chiffre d'affaires et la marge brute ?

---

## 🏗️ Architecture du Projet

```
Projet_DW/
│
├── DDDM_Analyse_WideWorldImporters.ipynb  ← Notebook principal (analyse complète)
├── requirements.txt                        ← Dépendances Python
├── AB_Test_Plan.pdf                        ← Plan A/B Test (2 pages)
│
├── etl_dimensions.py    ← Pipeline ETL : chargement des dimensions
├── etl_faits.py         ← Pipeline ETL : chargement de la table de faits
├── ia_predictions.py    ← Modèles IA : régression linéaire + prévisions
├── main.py              ← Point d'entrée du pipeline ETL
├── config.py            ← Configuration des connexions SQL Server
│
├── dim_client.csv       ← Export Dim_Client (663 clients)
├── dim_produit.csv      ← Export Dim_Produit (227 produits)
├── fact_ventes.csv      ← Export Fact_Ventes (228 000+ transactions)
│
├── olist_order_items_dataset.csv  ← Source 2 : Kaggle Olist E-commerce Dataset
└── prdwh.pbix           ← Dashboard Power BI interactif
```

---

## 📦 Sources de Données

| Source | Description | Volume |
|--------|-------------|--------|
| `fact_ventes.csv` | Transactions de ventes historiques | 228 264 lignes |
| `dim_client.csv` | Données clients et segmentation | 662 lignes |
| `dim_produit.csv` | Catalogue produits et catégories | 226 lignes |
| `olist_order_items_dataset.csv` | Transactions e-commerce brésilien — Kaggle | 112 650 lignes |

---

## ⚙️ Installation & Lancement

### Prérequis
- Python 3.10+
- SQL Server (avec ODBC Driver 17)
- Power BI Desktop (pour le dashboard)

### 1. Cloner le dépôt
```bash
git clone https://github.com/<votre-username>/dddm-wideworldimporters.git
cd dddm-wideworldimporters/Projet_DW
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```


### 3. Lancer le Notebook Jupyter
```bash
jupyter notebook DDDM_Analyse_WideWorldImporters.ipynb
```
Puis : **Kernel → Restart Kernel and Run All Cells**

### 4. Ouvrir le Dashboard Power BI
Ouvrir `prdwh.pbix` avec Power BI Desktop.

---

## 📊 Contenu du Notebook

| Section | Contenu |
|---------|---------|
| 1 | Imports & Chargement des données |
| 2 | Data Audit — Qualité des données |
| 3 | Jointure & Préparation du dataset enrichi |
| 4 | EDA : distributions, évolution CA, boxplots, heatmap |
| 5 | Tests statistiques : ANOVA, T-test, Chi-2 |
| 6 | Clustering K-Means (segmentation clients) |
| 7 | Modélisation prédictive : 3 modèles + validation croisée K-Fold |
| 8 | Interprétabilité SHAP (globale + locale) |
| 9 | Prévisions CA — 3 prochains mois |
| 10 | Recommandations actionnables |
| 11 | Plan A/B Test |
| 12 | Business Case & ROI estimé |

---

## 🤖 Composantes IA

| Modèle | Objectif | Librairie |
|--------|----------|-----------|
| K-Means (k=3) | Segmentation des clients | scikit-learn |
| Régression Linéaire | Prévision CA mensuel (baseline) | scikit-learn |
| Random Forest | Prévision CA mensuel (modèle principal) | scikit-learn |
| Gradient Boosting | Prévision CA mensuel (comparaison) | scikit-learn |
| SHAP TreeExplainer | Interprétabilité du Random Forest | shap |

---

## 📈 Dashboard Power BI

Le fichier `prdwh.pbix` contient un dashboard interactif avec :
- Vue **Direction** : KPIs globaux (CA, Marge, Croissance)
- Vue **Ventes par Segment** : Standard (segmentation issue du clustering K-Means)
- Vue **Performance Produits** : CA et marge par catégorie
- Vue **Tendances Temporelles** : évolution mensuelle
- Vue **Prévisions IA** : CA prévisionnel 3 mois

---

## 👥 Équipe

Projet réalisé dans le cadre du module **Data-Driven Decision Making**  
École : ENSIAS 
Projet réalisé par : Anas el midaoui & Ihssan ben labsir


---

## 🏷️ Version

`v1.0` — Date de rendu : 07 Juin 2026
