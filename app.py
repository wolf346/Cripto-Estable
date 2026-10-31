import pandas as pd
import requests
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Rendimientos Globales de Stablecoins",
    page_icon="📈",
    layout="centered",
)

st.title("📊 Ranking de Rentabilidad Anual (Stablecoins)")
st.caption(
    "Comparativa de tasas APY en Belo, Lemon, Bitso, SatoshiTango, Nexo y"
    " YouHodler - Ordenado de mayor a menor"
)


@st.cache_data(ttl=3600)
def obtener_datos_completos():
    """Consolida las tasas de rendimiento de las plataformas locales e

    internacionales de criptomonedas.
    """
    datos = [
        # Belo
        {
            "Plataforma": "Belo",
            "Stablecoin": "ARGt",
            "APY (%)": 32.0,
            "Red / Info": "Peso Argt (Pegged ARS)",
        },
        {
            "Plataforma": "Belo",
            "Stablecoin": "USDT",
            "APY (%)": 10.0,
            "Red / Info": "Tether USD (Promocional App)",
        },
        {
            "Plataforma": "Belo",
            "Stablecoin": "USDC",
            "APY (%)": 6.0,
            "Red / Info": "USD Coin (Circle)",
        },
        {
            "Plataforma": "Belo",
            "Stablecoin": "DAI",
            "APY (%)": 4.0,
            "Red / Info": "MakerDAO DAI",
        },
        # Lemon Cash
        {
            "Plataforma": "Lemon",
            "Stablecoin": "USDT",
            "APY (%)": 7.0,
            "Red / Info": "Earn Semanal USDT",
        },
        {
            "Plataforma": "Lemon",
            "Stablecoin": "USDC",
            "APY (%)": 6.5,
            "Red / Info": "Earn Semanal USDC",
        },
        {
            "Plataforma": "Lemon",
            "Stablecoin": "DAI",
            "APY (%)": 4.5,
            "Red / Info": "Earn Semanal DAI",
        },
        # Bitso
        {
            "Plataforma": "Bitso",
            "Stablecoin": "USDT",
            "APY (%)": 3.5,
            "Red / Info": "Bitso Yield (USDT)",
        },
        {
            "Plataforma": "Bitso",
            "Stablecoin": "USDC",
            "APY (%)": 3.5,
            "Red / Info": "Bitso Yield (USDC)",
        },
        {
            "Plataforma": "Bitso",
            "Stablecoin": "DAI",
            "APY (%)": 3.0,
            "Red / Info": "Bitso Yield (DAI)",
        },
        # SatoshiTango
        {
            "Plataforma": "SatoshiTango",
            "Stablecoin": "USDC",
            "APY (%)": 4.0,
            "Red / Info": "Rendimientos Stg (USDC)",
        },
        {
            "Plataforma": "SatoshiTango",
            "Stablecoin": "USDT",
            "APY (%)": 4.0,
            "Red / Info": "Rendimientos Stg (USDT)",
        },
        # Nexo (Tasas base / lealtad estándar)
        {
            "Plataforma": "Nexo",
            "Stablecoin": "USDT",
            "APY (%)": 10.0,
            "Red / Info": "Nexo Earn (Flexible estándar)",
        },
        {
            "Plataforma": "Nexo",
            "Stablecoin": "USDC",
            "APY (%)": 10.0,
            "Red / Info": "Nexo Earn (Flexible estándar)",
        },
        {
            "Plataforma": "Nexo",
            "Stablecoin": "DAI",
            "APY (%)": 9.0,
            "Red / Info": "Nexo Earn (Flexible estándar)",
        },
        # YouHodler
        {
            "Plataforma": "YouHodler",
            "Stablecoin": "USDT",
            "APY (%)": 12.0,
            "Red / Info": "YouHodler Savings Account",
        },
        {
            "Plataforma": "YouHodler",
            "Stablecoin": "USDC",
            "APY (%)": 12.0,
            "Red / Info": "YouHodler Savings Account",
        },
    ]

    return pd.DataFrame(datos)


# Cargar y ordenar datos de mayor a menor APY
df = obtener_datos_completos()
df_sorted = df.sort_values(by="APY (%)", ascending=False).reset_index(drop=True)
df_sorted.index += 1  # El ranking arranca en 1

# Métricas principales destacando el podio
col1, col2 = st.columns(2)
with col1:
    best = df_sorted.iloc[0]
    st.metric(
        label="🥇 Mejor Opción Global",
        value=f"{best['Plataforma']} ({best['Stablecoin']})",
        delta=f"{best['APY (%)']}% APY",
    )
with col2:
    st.metric(
        label="🌐 Cobertura",
        value="6 Plataformas",
        delta="Belo, Lemon, Bitso, Stg, Nexo, YouHodler",
    )

st.markdown("---")
st.subheader("🏆 Ranking General de Rendimiento (De mejor a peor)")

# Visualización en tabla interactiva
st.dataframe(
    df_sorted.style.highlight_max(subset=["APY (%)"], color="#d4edda"),
    use_container_width=True,
    column_config={
        "APY (%)": st.column_config.NumberColumn(
            "Rendimiento Anual (APY)", format="%.2f %%"
        )
    },
)

st.info(
    "💡 **Nota:** Las tasas internacionales (como Nexo y YouHodler) suelen"
    " requerir condiciones específicas de lealtad, plazos fijos o tenencia de"
    " tokens nativos de la plataforma para alcanzar los rendimientos máximos."
)
