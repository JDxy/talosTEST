import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV generado por Talos
df = pd.read_csv("test_2/101724150858.csv")

# Mostrar las primeras filas del DataFrame para verificar los datos
print(df.columns)
print(df.head())

