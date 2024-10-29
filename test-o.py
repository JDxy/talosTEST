import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('data.csv')

# Crear el gráfico de pastel
plt.figure(figsize=(7, 7))
plt.pie(df['Value'], labels=df['Category'], autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'orange', 'pink', 'purple'])

# Añadir un título
plt.title('Gráfico de Pastel - Proporciones de Categorías')

# Asegurar que el gráfico de pastel es un círculo
plt.axis('equal')

# Mostrar el gráfico
plt.show()
