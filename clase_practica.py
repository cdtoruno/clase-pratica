import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
data = 'train.csv'
df = pd.read_csv(data)

# Mostrar las primeras 5 filas del dataset
print(df.head())

# Descripción general del dataset
print(df.info())

# Estadistica descriptiva del dataset
print(df.describe())

# Seleccionar las 5 tiendas con mayores ventas totales
top_5_stores = df.groupby('Product ID')['Sales'].sum().nlargest(5)
top_5_stores.plot(kind='bar', title='Top 5 Tiendas con Mayores Ventas')
plt.ylabel('Ventas Totales')
plt.show()

# Histograma para analizar la distribución de las ventas
plt.hist(df['Sales'], bins=20, color='skyblue')
plt.title('Distribución de las Ventas')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')
plt.show()

# Cantidad de ventas por region
sales_by_region = df.groupby('Region')['Sales'].sum()
sales_by_region.plot(kind='bar', title='Ventas por Región')
plt.ylabel('Ventas')
plt.xlabel('Región')
plt.show()



df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['mes'] = df['Order Date'].dt.month

ventas_por_mes_simple = df.groupby('mes')['Sales'].mean().reset_index()

# Graficamos la evolución del promedio de ventas por mes
plt.figure(figsize=(10, 6)) 
plt.plot(ventas_por_mes_simple['mes'], ventas_por_mes_simple['Sales'], color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)

# Ajustes estéticos
plt.title('Promedio de Ventas por Mes', fontsize=16, fontweight='bold')
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Promedio de Ventas', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(ticks=range(1, 13), labels=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
plt.tight_layout() 
plt.show()









