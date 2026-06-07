import streamlit as st
import pandas as pd

# Configuración
st.set_page_config(
    page_title="LOTOMETRIKA RD",
    page_icon="🎯",
    layout="wide"
)

# Título
st.title("🎯 LOTOMETRIKA RD")
st.subheader("Sistema Inteligente de Análisis de Loterías Dominicanas")

# Cargar datos
@st.cache_data
def cargar_datos():
    try:
        return pd.read_csv("historicos.csv")
    except Exception as e:
        st.error(f"Error cargando historicos.csv: {e}")
        return pd.DataFrame()

df = cargar_datos()

# Verificar datos
if df.empty:
    st.warning("No se encontraron datos en historicos.csv")
    st.stop()

# Información general
st.success(f"Registros cargados: {len(df)}")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total registros", len(df))

with col2:
    if "loteria" in df.columns:
        st.metric(
            "Loterías",
            df["loteria"].nunique()
        )

st.divider()

# Mostrar datos
st.subheader("Histórico")

st.dataframe(
    df,
    use_container_width=True
)

# Filtro por lotería
if "loteria" in df.columns:

    st.divider()

    loteria = st.selectbox(
        "Selecciona una lotería",
        ["Todas"] + sorted(df["loteria"].astype(str).unique().tolist())
    )

    if loteria != "Todas":

        df_filtrado = df[
            df["loteria"] == loteria
        ]

        st.subheader("Resultados filtrados")

        st.dataframe(
            df_filtrado,
            use_container_width=True
        )

# Frecuencia del primer premio
if "primero" in df.columns:

    st.divider()

    st.subheader("Top 20 números más frecuentes")

    frecuencia = (
        df["primero"]
        .value_counts()
        .head(20)
    )

    st.bar_chart(frecuencia)

st.divider()

st.success("LOTOMETRIKA RD ACTIVA")
