# Plan A/B Test — Programme de Fidélisation Clients VIP
## Wide World Importers | Data-Driven Decision Making

---

## 1. Contexte & Objectif

L'analyse du Data Warehouse WideWorldImporters révèle que les clients du segment **VIP** génèrent un chiffre d'affaires moyen par transaction significativement supérieur aux autres segments (confirmé par T-test, p < 0.05). Cependant, ce segment reste sous-exploité en termes de rétention et de fréquence d'achat.

**Objectif du test :** Valider si la mise en place d'un **programme de fidélité dédié aux clients VIP** (remises personnalisées, account manager dédié, offres exclusives) augmente significativement leur chiffre d'affaires moyen mensuel.

---

## 2. Hypothèses

| | Énoncé |
|---|---|
| **H₀ (nulle)** | Le programme de fidélité ne modifie pas le CA moyen mensuel des clients VIP : μ_B = μ_A |
| **H₁ (alternative)** | Le programme de fidélité augmente le CA moyen mensuel des clients VIP d'au moins 10% : μ_B ≥ 1.10 × μ_A |

**Type de test :** T-test bilatéral de Student (Welch) — α = 0.05  
**Puissance statistique cible :** β = 0.80 (80%)

---

## 3. Conception du Test

### Groupes expérimentaux

| Groupe | Description | Traitement |
|--------|-------------|------------|
| **Groupe A — Contrôle** | Clients VIP sans changement | Aucun programme fidélité |
| **Groupe B — Traitement** | Clients VIP sélectionnés | Programme fidélité activé : remises personnalisées + account manager |

**Méthode d'assignation :** Randomisation aléatoire simple parmi les clients VIP actifs (ayant effectué ≥1 achat dans les 3 derniers mois).

### Taille d'échantillon

Calcul basé sur :
- Effet minimum détectable : +10% de CA moyen
- Écart-type estimé : basé sur les données historiques du DW
- Puissance : 80% | Niveau de signification : 5%

**→ Taille minimale requise : 50 clients par groupe (100 clients au total)**

*Note : Le segment VIP compte ~150 clients actifs dans le DW, ce qui permet l'assignation de 50 par groupe.*

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
| p-value < 0.05 **ET** augmentation CA ≥ 10% | ✅ **DÉPLOYER** le programme à tous les clients VIP |
| p-value < 0.05 **MAIS** augmentation CA < 10% | ⚠️ **AJUSTER** le programme — effet insuffisant pour le ROI |
| p-value ≥ 0.05 | ❌ **NE PAS DÉPLOYER** — effet non prouvé statistiquement |

---

## 7. Risques & Mitigations

| Risque | Probabilité | Mitigation |
|--------|-------------|------------|
| Contamination entre groupes | Faible | Assignation stricte, pas de communication croisée |
| Biais de saisonnalité | Moyen | Durée de 3 mois couvrant plusieurs périodes |
| Taille d'échantillon insuffisante | Faible | 150 clients VIP disponibles > 100 requis |
| Abandon du programme par les clients | Faible | Suivi mensuel, ajustements possibles sans rompre le protocole |

---

## 8. Impact Financier Attendu

D'après le Business Case calculé dans le notebook :

- **CA Total historique** : voir notebook section 12
- **Gain estimé (Rec. 1 — Fidélisation VIP)** : +2% du CA total
- **Coût estimé du programme** : remises ≤5% + 1 account manager
- **ROI estimé** : positif dès le 2ème mois si augmentation ≥ 10% confirmée

---

*Document rédigé dans le cadre du projet Data-Driven Decision Making*  
*Module DDDM — Filière GL & GD 2A | Date : Juin 2026*
