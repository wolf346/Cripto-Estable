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
            "APY (%)": 21.0,  # TNA estimada de FCI
            "Operación": "Pesos (ARS)",
            "Red / Info": "Cuenta Remunerada ARS (FCI Delta / TNA)",
        },
        {
            "Plataforma": "Naranja X",
            "Stablecoin": "Pesos (ARS)",
            "APY (%)": 19.5,  # TNA estimada (con tope de saldo)
            "Operación": "Pesos (ARS)",
            "Red / Info": "Cuenta Remunerada ARS (TNA)",
        },
        {
            "Plataforma": "Mercado Pago",
            "Stablecoin": "Pesos (ARS)",
            "APY (%)": 19.0,  # TNA del FCI BIND
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
            "Red / Info": "Invers
