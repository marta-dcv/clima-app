import streamlit as st
import duckdb
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()

CIUDAD = os.getenv("CIUDAD", "Vigo")

st.title("🌤️ App del Clima con DuckDB")

conn = duckdb.connect('clima.duckdb')

df = conn.execute("SELECT * FROM clima ORDER BY fecha DESC").fetchdf()

st.subheader("📋 Historial de datos guardados")
st.dataframe(df)

if not df.empty:
    st.subheader("📈 Gráfico de temperatura a lo largo del tiempo")
    fig, ax = plt.subplots()
    ax.plot(df["fecha"], df["temperatura"], marker='o', color='tab:blue')
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Temperatura (°C)")
    ax.set_title(f"Temperatura en {CIUDAD}")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.info("No hay datos en la base de datos todavía.")
