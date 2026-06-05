
import streamlit as st
import pandas as pd

st.title("LOTOMETRIKA RD")

df = pd.read_csv("historicos.csv")

st.subheader("Histórico cargado")
st.dataframe(df)

st.write("Cantidad de sorteos:", len(df))

frecuencia = pd.concat([
    df["primero"],
    df["segundo"],
    df["tercero"]
]).value_counts()

st.subheader("Top 20 números más frecuentes")
st.dataframe(frecuencia.head(20))
