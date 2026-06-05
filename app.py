import streamlit as st
import pandas as pd

st.set_page_config(page_title="LOTOMETRIKA RD")

st.title("🎯 LOTOMETRIKA RD")

df = pd.read_csv("historicos.csv")

st.subheader("Histórico cargado")
st.dataframe(df)

st.subheader("Estadísticas rápidas")

st.write("Total sorteos:", len(df))

frecuencia = df["primero"].value_counts().head(10)

st.write("Top 10 números en primera posición")
st.bar_chart(frecuencia)
