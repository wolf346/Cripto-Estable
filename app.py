import pandas as pd
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Rendimientos Stablecoins y Billeteras Argentina",
    page_icon="📈",
    layout="centered",
)

st.title("📊 Ranking General de Rentabilidad (Fintechs Argentina)")
st.caption(
    "Comparativa de APY/TNA en Mercado Pago, Personal Pay, Naranja X, Belo, Lemon, Buenbit, Ripio, Decrypto, Bitso, SatoshiTango, Binance, Bitget, BingX, Nexo y YouHodler"
)


@st.cache_data(ttl=3600)
def obtener_datos_completos():
    """Consolida las tasas de rendimiento (APY / TNA) de billeteras virtuales,
    plataformas locales e internacionales que operan en Argentina.
    """
    datos = [
        # --- BILLETERAS VIRTUALES Y CUENTAS REMUNERADAS (PESOS ARS) ---
        {
            "Plataforma": "Personal Pay",
            "Stablecoin": "Pesos (ARS)",
            "APY (%)": 21.0,
            "Operación": "Pesos (ARS)",
            "Red / Info": "Cuenta Remunerada ARS (FCI Delta / TNA)",
        },
        {
            "Plataforma": "Naranja X",
            "Stablecoin": "Pesos (ARS)",
            "APY (%)": 19.5,
            "Operación": "Pesos (ARS)",
            "Red / Info": "Cuenta Remunerada ARS (TNA)",
        },
        {
            "Plataforma": "Mercado Pago",
            "Stablecoin": "Pesos (ARS)",
            "APY (%)": 19.0,
            "Operación": "Pesos (ARS)",
            "Red / Info": "Fondo Común de Inversión BIND (TNA)",
        },
        # --- NUEVAS INCORPORACIONES (BUENBIT, RIPIO, DECRYPTO) ---
        {
            "Plataforma": "Buenbit",
            "Stablecoin": "USDT",
            "APY (%)": 8.5,
            "Operación": "Pesos (ARS) / USD",
            "Red / Info": "Buenbit Earn Flexible",
        },
        {
            "Plataforma": "Buenbit",
            "Stablecoin": "USDC",
            "APY (%)": 8.0,
            "Operación": "Pesos (ARS) / USD",
            "Red / Info": "Buenbit Earn Flexible",
        },
        {
            "Plataforma": "Buenbit",
            "Stablecoin": "nuARS",
            "APY (%)": 25.0,
            "Operación": "Pesos (ARS)",
            "Red / Info": "Peso Digital NuARS",
        },
        {
            "Plataforma": "Ripio",
            "Stablecoin": "UXD",
            "APY (%)": 10.0,
            "Operación": "Pesos (ARS)",
            "Red / Info": "Ripio Earn (Criptodólar UXD)",
        },
        {
            "Plataforma": "Ripio",
            "Stablecoin": "USDT",
            "APY (%)": 6.0,
            "Operación": "Pesos (ARS) / USD",
            "Red / Info": "Ripio Earn Flexible",
        },
        {
            "Plataforma": "Decrypto",
            "Stablecoin": "USDT",
            "APY (%)": 7.5,
            "Operación": "Pesos (ARS) / USD",
            "Red / Info": "Inversión Decrypto",
        },
        {
            "Plataforma": "Decrypto",
            "Stablecoin": "USDC",
            "APY (%)": 7.0,
            "Operación": "Pesos (ARS) / USD",
            "Red / Info": "Inversión Decrypto",
        },
        # --- FINTECHS Y EXCHANGES LOCALES ---
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
        # --- EXCHANGES GLOBAL CON P2P / ARS ---
        {
            "Plataforma": "Bitget",
            "Stablecoin": "USDT",
            "APY (%)": 9.0,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "Bitget Savings Flexible",
        },
        {
            "Plataforma": "Binance",
            "Stablecoin": "USDT",
            "APY (%)": 8.5,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "Binance Simple Earn (USDT)",
        },
        {
            "Plataforma": "BingX",
            "Stablecoin": "USDT",
            "APY (%)": 8.0,
            "Operación": "P2P Pesos (ARS)",
            "Red / Info": "BingX Wealth Flexible",
        },
        # --- PLATAFORMAS INTERNACIONALES ---
        {
            "Plataforma": "YouHodler",
            "Stablecoin": "USDT",
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
        delta=f"{best['APY (%)']}% APY/TNA",
    )
with col2:
    st.metric(
        label="🌐 Plataformas monitoreadas",
        value=f"{len(df['Plataforma'].unique())} Billeteras & Exchanges",
        delta="Cobertura completa ARS / USD",
    )

st.markdown("---")
st.subheader("🏆 Ranking General de Rendimientos (Mejor a Peor)")

# Visualización interactiva de la lista completa
st.dataframe(
    df_sorted.style.highlight_max(subset=["APY (%)"], color="#d4edda"),
    use_container_width=True,
    column_config={
        "APY (%)": st.column_config.NumberColumn(
            "Rendimiento Anual (APY / TNA)", format="%.2f %%"
        )
    },
)

st.info(
    "💡 **Nota sobre Cuentas Remuneradas y Fintechs:** Las tasas de las cuentas"
    " en pesos varían diariamente según las tasas del mercado financiero y los"
    " Fondos Comunes de Inversión (FCI) adheridos."
)
