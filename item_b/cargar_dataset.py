import pandas as pd
import zipfile
import os

# Descargar dataset
url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/master/Cancer_Pulmon.zip"
os.system(f"wget -q {url}")

# Descomprimir
with zipfile.ZipFile("Cancer_Pulmon.zip", 'r') as zip_ref:
    zip_ref.extractall(".")

# Cargar dataset en memoria
df = pd.read_csv("Cancer_Pulmon.csv")
