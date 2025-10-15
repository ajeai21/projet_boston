# Projet Boston ETL
## Équipe

**Groupe n°9**

| Nom | Rôle / Contribution |
|-----|-------------------|
| Ajeai SRIYOGANATHAN | Développement ETL |
| Dounia KADDOURI | Extraction des données |
| Aya KODAD | Analyse statistique et documentation |
| Mohammed HAKKOU | CI/CD, organisation projet et README |
| Israe LAZIZI | Tests unitaires |
| Janet Ashley TIADAM TCHINDA | Transformation des des données |

# Vision produit
Ce projet met en œuvre un pipeline ETL pour récupérer les salaires des employés municipaux de Boston, nettoyer les données, les enregistrer dans un CSV et calculer des statistiques par département.
# Tests unitaires
- Chaque fonction du pipeline (extract, transform, load, analyse) a un test simple.
- Les tests sont exécutables avec `pytest`.
- Objectif : s'assurer que le code fonctionne même après modifications.

---

## 2. Installation

1. Cloner le dépôt :

git clone <URL_DU_DEPOT>
cd project_data

## 3. Créer un environnement virtuel et l’activer :

python -m venv env_dataops
.\env_dataops\Scripts\activate   # Windows
# ou
source env_dataops/bin/activate  # macOS/Linux

## 4. Installer les dépendances :

pip install -r requirements.txt
# ou
pip install pandas numpy pytest

5. Exécution du pipeline ETL

Depuis Python ou Jupyter Notebook :

from mon_projet.etl import extract_boston_salary, transform, load, analyse

URL = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"

# Extraction
df = extract_boston_salary(URL)

# Transformation
df_clean = transform(df)

# Chargement
load(df_clean, "boston_salaries_clean.csv")

# Analyse
stats = analyse(df_clean)
print(stats.get("POLICE"))  # exemple

4. Tests unitaires

Tous les modules du pipeline sont testés avec pytest.

Commande pour lancer les tests :

$env:PYTHONPATH = "$PWD"  # Windows PowerShell
python -m pytest -v tests


Les tests vérifient :

extract_boston_salary retourne bien un DataFrame

transform nettoie et convertit correctement les salaires

load crée un fichier CSV valide

analyse retourne des statistiques correctes par département


5. Organisation Agile
Backlog Produit

Le backlog liste les fonctionnalités et tâches à réaliser pour ce projet ETL :

Extraction des données

Récupérer les données publiques de Boston (City Payroll 2018) via l’API.

Transformation des données

Nettoyer les noms de colonnes, convertir les salaires en float, supprimer les valeurs manquantes.

Chargement (Load)

Sauvegarder les données nettoyées dans un fichier CSV exploitable.

Analyse statistique

Calculer min, max, moyenne, médiane, écart et nombre d’employés par département.

Tests unitaires

Vérifier que chaque fonction ETL fonctionne correctement avec pytest.

CI/CD avec GitHub Actions

Automatiser l’exécution des tests à chaque push ou pull request.

Documentation et README

Décrire le projet, l’équipe, le pipeline ETL et les instructions pour les tests.

Sprints

| Sprint   | Objectifs                                 |
| -------- | ----------------------------------------- |
| Sprint 1 | Implémenter `extract` et `transform`      |
| Sprint 2 | Implémenter `load` et `analyse`           |
| Sprint 3 | Écrire les tests unitaires                |
| Sprint 4 | Mettre en place CI/CD avec GitHub Actions |
| Sprint 5 | Finaliser README et documentation         |

Rôles et Rituels (méthode Agile)

Rôles de l’équipe :

Product Owner (PO) : Définit les objectifs du projet et priorise le backlog.

Scrum Master / Coordinateur : S’assure que l’équipe avance efficacement et que les tâches sont bien organisées.

Développeurs / Data Engineers : Implémentent l’ETL, les tests, la CI/CD et la documentation.

Rituels / pratiques Agile :

Daily Stand-up (10 min) : Chaque membre partage ce qu’il a fait, ce qu’il fera, et les obstacles rencontrés.

Sprint Planning : Planification des tâches à réaliser pour le sprint (ex : extraction, transformation, tests).

Sprint Review : Présentation des fonctionnalités réalisées et retour de l’équipe / professeur.

Retrospective : Discussion sur ce qui a bien fonctionné et ce qui peut être amélioré pour le prochain sprint.



Rituels Agile possibles :

Daily Stand-up : 10 min chaque jour pour partager l’avancement

Sprint Review : vérifier les fonctionnalités terminées à la fin de chaque sprint

Retrospective : évaluer ce qui a bien ou mal fonctionné et améliorer le processus

6. Exemple de sortie

CSV généré : boston_salaries_clean.csv

NAME,TITLE,DEPARTMENT_NAME,TOTAL EARNINGS
Alice,Engineer,IT,1000.0
Bob,Manager,HR,2000.0
...


Statistiques pour le département Police :

stats["POLICE"]
# Résultat exemple : {'min': 35000, 'max': 120000, 'moyenne': 75000, 'mediane': 70000, 'écart': 85000, 'nb_employés': 120}

7. Bonnes pratiques

Tests unitaires systématiques avec pytest

Automatisation CI/CD via GitHub Actions

Pipeline ETL modulaire et réutilisable pour d’autres jeux de données