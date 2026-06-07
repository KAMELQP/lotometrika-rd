import streamlit as st

st.title("LOTOMETRIKA RD")    st.metric("Total registros", len(df))

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
