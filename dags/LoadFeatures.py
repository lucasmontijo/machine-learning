import pandas as pd
from dags import config
from pathlib import Path

def load_features(filter=True):
    raw_data = pd.read_csv("data/dados.csv")
    if filter == True:
        return raw_data[config.USE_COLUMNS]
    else:
        return raw_data