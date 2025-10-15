import json
import urllib.request
import pandas as pd


def extract_boston_salary(url: str) -> pd.DataFrame:
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            records = data['result']['records']
            df = pd.DataFrame(records)
            print(f"✅ Extraction réussie : {df.shape[0]} lignes récupérées.")
            return df
    except Exception as e:
        print(f" Erreur lors de l'extraction : {e}")
        return pd.DataFrame()


def transform(df: pd.DataFrame) -> pd.DataFrame:
    
    if df.empty:
        print("⚠️ DataFrame vide, rien à transformer.")
        return df

    # Standardisation des noms de colonnes
    df.columns = [col.strip().upper() for col in df.columns]

    # Conversion de TOTAL EARNINGS en float
    if "TOTAL EARNINGS" in df.columns:
        df["TOTAL EARNINGS"] = (
            df["TOTAL EARNINGS"]
            .astype(str)
            .str.replace(",", "", regex=True)
            .str.replace("$", "", regex=True)
            .astype(float)
        )
    else:
        print("Colonne TOTAL EARNINGS introuvable.")
        return df

    # Suppression des lignes avec TOTAL EARNINGS manquant
    df = df.dropna(subset=["TOTAL EARNINGS"])

    # Sélection des colonnes utiles
    colonnes_utiles = ["NAME", "TITLE", "DEPARTMENT_NAME", "TOTAL EARNINGS"]
    df = df[colonnes_utiles]

    print(f" Transformation terminée : {df.shape[0]} lignes conservées.")
    return df


def load(df: pd.DataFrame, filename: str = "boston_salaries_clean.csv") -> None:
    
    if df.empty:
        print("DataFrame vide, rien à enregistrer.")
        return

    # Sauvegarde dans le dossier courant
    df.to_csv(filename, index=False)
    print(f"Données sauvegardées dans le fichier : {filename}")



def analyse(df: pd.DataFrame) -> dict:
   
    if df.empty:
        print("DataFrame vide, impossible d'analyser.")
        return {}

    stats = {}

    
    grouped = df.groupby("DEPARTMENT_NAME")["TOTAL EARNINGS"]

    for dept, series in grouped:
        stats[dept] = {
            "min": series.min(),
            "max": series.max(),
            "moyenne": series.mean(),
            "mediane": series.median(),
            "écart": series.max() - series.min(),
            "nb_employés": series.count()
        }

    print(f"Analyse réalisée sur {len(stats)} départements.")
    return stats
