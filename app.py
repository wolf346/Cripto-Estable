import pandas as pd
import requests
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Rendimientos Stablecoins & Fintechs Argentina",
    page_icon="📈",
    layout="centered",
)

st.title("📊 Ranking de Rentabilidad Stablecoins en Argentina")
st.caption(
    "Comparativa de APY en Belo, Lemon, Bitso, SatoshiTango, Binance, Bitget, BingX, Nexo y YouHodler"
)


@st.cache_data(ttl=3600)
def obtener_datos_completos():
    """Consolida las tasas de rendimiento de las fintech y exchanges

    locales e internacionales que operan con pesos o dólares en Argentina.
    """
    datos = [
        # --- FINTECHS Y EXCHANGES LOCALES (ARS / ARGt / USD) ---
        {
            "Plataforma": "Belo",
            "Stablecoin": "ARGt",
            "APY (%)": 32.0,
            "Operación": "Pesos (ARS)",
            "Red / Info": "Peso Argt (Pegged ARS)",
        },
        {
            "Plataforma": "Belo",
            "Stablecoin": "USDT",
            "APY (%)": 10.0,
            "Operación": "Pesos / USD",
            "Red / Info": "Tether USD (Promocional App)",
        },
        {
            "Plataforma": "Belo",
            "Stablecoin": "USDC",
            "APY (%)": 6.0,
            "Operación": "Pesos / USD",
            "Red / Info": "USD Coin (Circle)",
        },
        {
            "Plataforma": "Belo",
            "Stablecoin": "DAI",
            "APY (%)": 4.0,
            "Operación": "Pesos / USD",
            "Red / Info": "MakerDAO DAI",
        },
        {
            "Plataforma": "Lemon",
            "Stablecoin": "USDT",
            "APY (%)": 7.0,
            "Operación": "Pesos / USD",
            "Red / Info": "Earn Semanal USDT",
        },
        {
            "Plataforma": "Lemon",
            "Stablecoin": "USDC",
            "APY (%)": 6.5,
            "Operación": "Pesos / USD",
            "Red / Info": "Earn Semanal USDC",
        },
        {
            "Plataforma": "Lemon",
            "Stablecoin": "DAI",
            "APY (%)": 4.5,
            "Operación": "Pesos / USD",
            "Red / Info": "Earn Semanal DAI",
        },
        {
            "Plataforma": "Bitso",
            "Stablecoin": "USDT",
            "APY (%)": 3.5,
            "Operación": "Pesos / USD",
            "Red / Info": "Bitso Yield (USDT)",
        },
        {
            "Plataforma": "Bitso",
            "Stablecoin": "USDC",
            "APY (%)": 3.5,
            "Operación": "Pesos / USD",
            "Red / Info": "Bitso Yield (USDC)",
        },
        {
            "Plataforma": "Bitso",
            "Stablecoin": "DAI",
            "APY (%)": 3.0,
            "Operación": "Pesos / USD",
            "Red / Info": "Bitso Yield (DAI)",
        },
        {
            "Plataforma": "SatoshiTango",
            "Stablecoin": "USDC",
            "APY (%)": 4.0,
            "Operación": "Pesos / USD",
            "Red / Info": "Rendimientos Stg (USDC)",
        },
        {
            "Plataforma": "SatoshiTango",
            "Stablecoin": "USDT",
            "APY (%)": 4.0,
            "Operación": "Pesos / USD",
            "Red / Info": "Rendimientos Stg (USDT)",
        },
        # --- EXCHANGES GLOBAL CON P2P / ENTRADA EN PESOS ---
        {
            "Plataforma": "Binance",
            "Stablecoin": "USDT",
            "APY (%)": 8.5,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "Binance Simple Earn (USDT)",
        },
        {
            "Plataforma": "Binance",
            "Stablecoin": "USDC",
            "APY (%)": 6.0,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "Binance Simple Earn (USDC)",
        },
        {
            "Plataforma": "Binance",
            "Stablecoin": "FDUSD",
            "APY (%)": 7.5,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "Binance Simple Earn (FDUSD)",
        },
        {
            "Plataforma": "Bitget",
            "Stablecoin": "USDT",
            "APY (%)": 9.0,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "Bitget Savings Flexible",
        },
        {
            "Plataforma": "Bitget",
            "Stablecoin": "USDC",
            "APY (%)": 5.5,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "Bitget Savings Flexible",
        },
        {
            "Plataforma": "BingX",
            "Stablecoin": "USDT",
            "APY (%)": 8.0,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "BingX Wealth Flexible",
        },
        {
            "Plataforma": "BingX",
            "Stablecoin": "USDC",
            "APY (%)": 5.0,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "BingX Wealth Flexible",
        },
        # --- PLATAFORMAS INTERNACIONALES DE RENDIMIENTO ---
        {
            "Plataforma": "YouHodler",
            "Stablecoin": "USDT",
            "APY (%)": 12.0,
            "Operación": "Crypto / USD",
            "Red / Info": "Savings Account",
        },
        {
            "Plataforma": "YouHodler",
            "Stablecoin": "USDC",
            "APY (%)": 12.0,
            "Operación": "Crypto / USD",
            "Red / Info": "Savings Account",
        },
        {
            "Plataforma": "Nexo",
            "Stablecoin": "USDT",
            "APY (%)": 10.0,
            "Operación": "Crypto / USD",
            "Red / Info": "Nexo Earn Flexible",
        },
        {
            "Plataforma": "Nexo",
            "Stablecoin": "USDC",
            "APY (%)": 10.0,
            "Operación": "Crypto / USD",
            "Red / Info": "Nexo Earn Flexible",
        },
        {
            "Plataforma": "Nexo",
            "Stablecoin": "DAI",
            "APY (%)": 9.0,
            "Operación": "Crypto / USD",
            "Red / Info": "Nexo Earn Flexible",
        },
    ]

    return pd.DataFrame(datos)


# Cargar y ordenar datos de mayor a menor APY
df = obtener_datos_completos()
df_sorted = df.sort_values(by="APY (%)", ascending=False).reset_index(drop=True)
df_sorted.index += 1  # Iniciar ranking en 1

# Métricas destacadas
col1, col2 = st.columns(2)
with col1:
    best = df_sorted.iloc[0]
    st.metric(
        label="🥇 Líder del Ranking",
        value=f"{best['Plataforma']} ({best['Stablecoin']})",
        delta=f"{best['APY (%)']}% APY",
    )
with col2:
    st.metric(
        label="🌐 Plataformas monitoreadas",
        value="9 Exchanges / Fintechs",
        delta="Nivel Local & Global P2P",
    )

st.markdown("---")
st.subheader("🏆 Ranking General de Rendimientos (Mejor a Peor)")

# Visualización interactiva
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
    "💡 **Operativa en Argentina:** Las plataformas como Binance, Bitget y"
    " BingX permiten ingresar pesos argentinos (ARS) mediante sus mercados P2P"
    " oficiales con acreditación en cuentas bancarias locales (CVU/CBU)."
)
