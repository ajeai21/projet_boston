import json
import urllib.request
import pandas as pd


def extract_boston_salary(url: str) -> pd.DataFrame:
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            records = data['result']['records']
            df = pd.DataFrame(records)
            print(f" Extraction réussie : {df.shape[0]} lignes récupérées.")
            return df
    except Exception as e:
        print(f" Erreur lors de l'extraction : {e}")
        return pd.DataFrame()
    



def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie et transforme les données de salaires.
    - Convertit TOTAL EARNINGS en float
    - Supprime les lignes avec valeurs manquantes sur TOTAL EARNINGS
    - Garde les colonnes principales
    """
    if df.empty:
        print("⚠️ DataFrame vide, rien à transformer.")
        return df

    # On standardise le nom de la colonne
    df.columns = [col.strip().upper() for col in df.columns]

    # Conversion de TOTAL EARNINGS en numérique
    if "TOTAL EARNINGS" in df.columns:
        df["TOTAL EARNINGS"] = (
            df["TOTAL EARNINGS"]
            .astype(str)
            .str.replace(",", "")  # supprime les virgules
            .str.replace("$", "")  # supprime les $
            .astype(float)
        )
    else:
        print("⚠️ Colonne TOTAL EARNINGS introuvable.")
        return df

    # On supprime les lignes où TOTAL EARNINGS est manquant
    df = df.dropna(subset=["TOTAL EARNINGS"])

    # On garde les colonnes utiles
    colonnes_utiles = [
        "NAME",
        "TITLE",
        "DEPARTMENT_NAME",
        "TOTAL EARNINGS"
    ]
    df = df[colonnes_utiles]

    print(f"✅ Transformation terminée : {df.shape[0]} lignes conservées.")
    return df


