import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Título de la aplicación
st.title("Simulación de llenado de bolsas de globos")

# Entrada de datos
num_simulations = st.number_input("Número de simulaciones:", min_value=1, value=1000, step=1)
peso_minimo = st.number_input("Peso mínimo por unidad (gramos):", min_value=0.0, value=0.5, format="%.3f")
peso_maximo = st.number_input("Peso máximo por unidad (gramos):", min_value=0.0, value=1.5, format="%.3f")
peso_configurar = st.number_input("Peso a configurar en la máquina (gramos):", min_value=0.0, value=1.0, format="%.3f")
unidades_por_bolsa = st.number_input("Unidades por bolsa:", min_value=1, value=10, step=1)

# Botón para realizar la simulación
if st.button("Realizar simulación"):
    # Simulación de pesos
    pesos = np.random.uniform(peso_minimo, peso_maximo, (num_simulations, unidades_por_bolsa))
    
    # Calcular el peso total por bolsa
    pesos_totales = np.sum(pesos, axis=1)
    
    # Contar cuántas bolsas se empacan según el peso configurado
    conteo_bolsas = np.floor(pesos_totales / peso_configurar).astype(int)

    # Crear un DataFrame para contar la frecuencia de cada resultado
    conteo_df = pd.Series(conteo_bolsas).value_counts().sort_index()

    # Crear la gráfica de barras para cantidad de bolsas
    fig, ax = plt.subplots()
    conteo_df.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_title("Cantidad de bolsas según cantidad de globos")
    ax.set_xlabel("Cantidad de globos en una bolsa")
    ax.set_ylabel("Cantidad de bolsas")
    ax.set_ylim(0, conteo_df.max() * 1.1)  # Aumentar el límite superior para mejor visualización
    ax.grid(axis='y')

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)




