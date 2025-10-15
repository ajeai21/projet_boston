import pandas as pd
import os
import tempfile
from mon_projet.etl import extract_boston_salary, transform, load, analyse

def test_extract_returns_dataframe():
    
    URL = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"
    df = extract_boston_salary(URL)
    assert isinstance(df, pd.DataFrame)  
    
    assert df.shape[0] > 0


def test_transform_simple():
    df = pd.DataFrame({
        "NAME": ["Alice", "Bob"],
        "TOTAL EARNINGS": ["1000", "2000"],
        "TITLE": ["Engineer", "Manager"],
        "DEPARTMENT_NAME": ["IT", "HR"]
    })
    df_clean = transform(df)
    
    
    assert df_clean["TOTAL EARNINGS"].dtype == float
    
    
    assert df_clean.shape[0] == 2
    
    
    assert set(df_clean.columns) == {"NAME", "TITLE", "DEPARTMENT_NAME", "TOTAL EARNINGS"}

def test_load_creates_file():
    df = pd.DataFrame({
        "NAME": ["Alice"],
        "TOTAL EARNINGS": [1000],
        "TITLE": ["Engineer"],
        "DEPARTMENT_NAME": ["IT"]
    })
    
    
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    tmpfile.close()
    
    load(df, tmpfile.name)
    
    
    assert os.path.exists(tmpfile.name)
    assert os.path.getsize(tmpfile.name) > 0
    
    
    os.remove(tmpfile.name)

def test_analyse_returns_dict():
    df = pd.DataFrame({
        "NAME": ["Alice", "Bob"],
        "TOTAL EARNINGS": [1000, 2000],
        "TITLE": ["Engineer", "Manager"],
        "DEPARTMENT_NAME": ["IT", "IT"]
    })
    
    stats = analyse(df)
    

    assert isinstance(stats, dict)
    

    assert "IT" in stats
    
    
    assert stats["IT"]["min"] == 1000
    assert stats["IT"]["max"] == 2000
    assert stats["IT"]["moyenne"] == 1500
    assert stats["IT"]["mediane"] == 1500
