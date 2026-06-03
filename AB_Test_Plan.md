# Plan A/B Test — Programme de Fidélisation Clients VIP
## Wide World Importers | Data-Driven Decision Making

---

## 1. Contexte & Objectif

L'analyse exploratoire des données de ventes Wide World Importers révèle que la catégorie Packaging Materials génère un CA moyen de 1 452 USD par transaction, soit presque 4 fois plus que la catégorie Novelty Items (396 USD), une différence confirmée statistiquement par T-test (t = 116.69, p < 0.0001).
Objectif du test : Valider si une campagne promotionnelle ciblée sur la catégorie Packaging Materials augmente significativement le CA moyen par transaction de cette catégorie.

---

## 2. Hypothèses

| | Énoncé |
|---|---|
| **H₀ (nulle)** | La campagne ne modifie pas le CA moyen par transaction Packaging Materials : μ_B = μ_A |
| **H₁ (alternative)** | La campagne augmente le CA moyen par transaction d'au moins 10% : μ_B ≥ 1.10 × μ_A |

**Type de test :** T-test bilatéral de Student (Welch) — α = 0.05  
**Puissance statistique cible :** β = 0.80 (80%)

---

## 3. Conception du Test

### Groupes expérimentaux

| Groupe | Description | Traitement |
|--------|-------------|------------|
| **Groupe A — Contrôle** | Transactions Packaging Materials sans promotion | Aucun campagne |
| **Groupe B — Traitement** | Transactions Packaging Materials ciblées | Campagne promotionnelle activée |

**Méthode d'assignation :** Randomisation aléatoire simple parmi les clients VIP actifs (ayant effectué ≥1 achat dans les 3 derniers mois).

### Taille d'échantillon

Calcul basé sur :
- Effet minimum détectable : +10% de CA moyen
- Écart-type estimé : basé sur les données historiques de ventes
- Puissance : 80% | Niveau de signification : 5%

**→ Taille minimale requise : 50 clients par groupe (100 clients au total)**

*Note : *
La catégorie Packaging Materials représente le volume suffisant pour l'assignation*

---

## 4. Durée & Calendrier

| Phase | Durée | Description |
|-------|-------|-------------|
| Préparation | 1 semaine | Sélection et randomisation des clients, configuration du programme |
| Exécution | 3 mois | Collecte des données — période suffisante pour observer l'effet |
| Analyse | 1 semaine | Calcul des métriques, test statistique, décision |
| **Total** | **~14 semaines** | |

**Début proposé :** Juillet 2026  
**Fin proposée :** Octobre 2026

---

## 5. Métriques de Suivi

### Métrique principale
- **CA moyen mensuel par client** (en USD) — mesure directe de l'impact business

### Métriques secondaires
- Marge brute moyenne par client
- Fréquence d'achat (nombre de transactions / mois)
- Panier moyen par transaction
- Taux de rétention (% clients actifs en fin de période)

### Métriques de guardrail (à surveiller)
- Taux de satisfaction client (ne doit pas baisser)
- Coût opérationnel du programme (ROI doit rester positif)

---

## 6. Critères de Décision

| Résultat | Décision |
|----------|----------|
| p-value < 0.05 **ET** augmentation CA ≥ 10% | ✅ **DÉPLOYER**  la campagne sur toute la catégorie |
| p-value < 0.05 **MAIS** augmentation CA < 10% | ⚠️ **AJUSTER** AJUSTER la campagne — effet insuffisant |
| p-value ≥ 0.05 | ❌ **NE PAS DÉPLOYER** — effet non prouvé  |

---

## 7. Risques & Mitigations

| Risque | Probabilité | Mitigation |
|--------|-------------|------------|
| Contamination entre groupes | Faible | Assignation stricte, pas de communication croisée |
| Biais de saisonnalité | Moyen | Durée de 3 mois couvrant plusieurs périodes |
| Taille d'échantillon insuffisante | Faible | Taille d'échantillon insuffisante — volume de transactions Packaging Materials suffisant |
| Abandon du programme par les clients | Faible | Suivi mensuel, ajustements possibles sans rompre le protocole |

---

## 8. Impact Financier Attendu

D'après l'analyse exploratoire des données de ventes :

- CA moyen Packaging Materials : 1 452 USD par transaction
- Gain estimé si +10% : +145 USD par transaction
- Sur le volume historique de la catégorie, l'impact annuel estimé est significatif
- ROI positif dès le 2ème mois si l'augmentation de 10% est confirmée

---

*Document rédigé dans le cadre du projet Data-Driven Decision Making*  
*Module DDDM —anas el midaoui & ihssan ben labsir| Date : Juin 2026*
