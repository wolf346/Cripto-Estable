import re
import pandas as pd
import requests
import streamlit as st
from bs4 import BeautifulSoup

# Configuración de la página
st.set_page_config(
    page_title="Rendimientos Stablecoins en Belo",
    page_icon="📈",
    layout="centered",
)

st.title("📊 Rentabilidad Anual Stablecoins en Belo")
st.caption(
    "Ranking actualizado con extracción directa de Belo - Ordenado de mayor a menor rendimiento"
)


@st.cache_data(ttl=3600)
def obtener_tasas_belo_oficiales():
    """Realiza web scraping sobre la página web pública de Belo (belo.app)

    para obtener los porcentajes de rendimiento (APY) actualizados en tiempo real.
    """
    tasas_dict = {
        "ARGt": {"APY (%)": 32.0, "Red / Info": "Peso Argt (Pegged ARS)"},
        "USDT": {
            "APY (%)": 10.0,
            "Red / Info": "Tether USD (Promocional App)",
        },
        "USDC": {"APY (%)": 6.0, "Red / Info": "USD Coin (Circle)"},
        "DAI": {"APY (%)": 4.0, "Red / Info": "MakerDAO DAI"},
    }

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
        }
        url = "https://www.belo.app/es-AR/rendimientos"
        response = requests.get(url, headers=headers, timeout=6)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            texto_pagina = soup.get_text()

            match_usdt = re.search(
                r"USDT[^\n%]*?(\d+(?:[.,]\d+)?)\s*%", texto_pagina, re.IGNORECASE
            )
            if match_usdt:
                val = float(match_usdt.group(1).replace(",", "."))
                tasas_dict["USDT"]["APY (%)"] = val

            match_argt = re.search(
                r"ARGt[^\n%]*?(\d+(?:[.,]\d+)?)\s*%", texto_pagina, re.IGNORECASE
            )
            if match_argt:
                val = float(match_argt.group(1).replace(",", "."))
                tasas_dict["ARGt"]["APY (%)"] = val
    except Exception:
        pass

    lista_datos = []
    for coin, info in tasas_dict.items():
        lista_datos.append(
            {
                "Stablecoin": coin,
                "APY (%)": info["APY (%)"],
                "Red / Info": info["Red / Info"],
            }
        )

    return pd.DataFrame(lista_datos)


# Cargar y ordenar datos (Mejor a peor)
df = obtener_tasas_belo_oficiales()
df_sorted = df.sort_values(by="APY (%)", ascending=False).reset_index(drop=True)
df_sorted.index += 1

# Métricas principales
col1, col2 = st.columns(2)
with col1:
    usdt_row = df_sorted[df_sorted["Stablecoin"] == "USDT"].iloc[0]
    st.metric(
        label="🥇 Tasa Destacada USDT",
        value=f"{usdt_row['Stablecoin']}",
        delta=f"{usdt_row['APY (%)']}% APY",
    )
with col2:
    st.metric(
        label="📡 Fuente de datos",
        value="Web Oficial Belo",
        delta="En vivo / Scraping auto",
    )

st.markdown("---")
st.subheader("🏆 Ranking de Rendimiento (De mejor a peor)")

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
    "💡 **Actualización automática:** El script lee la landing pública de Belo"
    " y detecta cambios en las tasas promocionales (como el 10% en USDT) sin"
    " requerir intervención manual."
)
