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
Backlog produit
| ID | Fonctionnalité  | Description                                         | Priorité |
| -- | --------------- | --------------------------------------------------- | -------- |
| 1  | Extraction      | Récupérer les données depuis l’API Boston Open Data | Haute    |
| 2  | Transformation  | Nettoyer et convertir les salaires en float         | Haute    |
| 3  | Load            | Sauvegarder les données nettoyées dans un CSV       | Moyenne  |
| 4  | Analyse         | Calculer statistiques par département               | Haute    |
| 5  | Tests unitaires | Vérifier toutes les fonctions                       | Haute    |
| 6  | CI/CD           | Automatiser les tests avec GitHub Actions           | Moyenne  |
| 7  | Documentation   | Rédiger le README et les instructions               | Moyenne  |

Sprints

| Sprint   | Objectifs                                 |
| -------- | ----------------------------------------- |
| Sprint 1 | Implémenter `extract` et `transform`      |
| Sprint 2 | Implémenter `load` et `analyse`           |
| Sprint 3 | Écrire les tests unitaires                |
| Sprint 4 | Mettre en place CI/CD avec GitHub Actions |
| Sprint 5 | Finaliser README et documentation         |

Rôles et rituels
Rôle	Description
Product Owner	Définit la vision et le backlog produit
Développeur ETL	Implémente les fonctions extract, transform, load, analyse
Testeur	Écrit et exécute les tests unitaires
Scrum Master	S’assure que les sprints avancent correctement, organise les réunions

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