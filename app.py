```python
import pandas as pd
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Comparador de Rendimientos Argentina",
    page_icon="📈",
    layout="wide",
)

st.title("📊 Comparador de Rendimientos Financieros")
st.caption(
    "Argentina | Billeteras virtuales, stablecoins y exchanges"
)

st.warning(
    "Las tasas cargadas son referencias manuales del código original. "
    "No se consideran tasas actuales verificadas. Antes de invertir, "
    "comprobá la tasa, las condiciones y la disponibilidad en la "
    "plataforma correspondiente."
)

# =========================================================
# DATOS
# =========================================================
# tasa_pct: porcentaje anual informado en el código original.
# tipo_tasa: dejar como 'Pendiente' hasta comprobar si es TNA,
# TEA, APY o APR.
# verificada: False hasta comprobar la tasa en una fuente fiable.
#
# IMPORTANTE:
# No se debe interpretar una tasa pendiente como vigente.

DATOS = [
    # Plataforma, activo, categoría, tasa, tipo de tasa
    ("Personal Pay", "ARS", "Pesos", 21.0, "Pendiente"),
    ("Naranja X", "ARS", "Pesos", 19.5, "Pendiente"),
    ("Mercado Pago", "ARS", "Pesos", 19.0, "Pendiente"),

    ("Buenbit", "USDT", "Stablecoin USD", 8.5, "Pendiente"),
    ("Buenbit", "USDC", "Stablecoin USD", 8.0, "Pendiente"),
    ("Buenbit", "nuARS", "Stablecoin ARS", 25.0, "Pendiente"),

    ("Ripio", "UXD", "Stablecoin USD", 10.0, "Pendiente"),
    ("Ripio", "USDT", "Stablecoin USD", 6.0, "Pendiente"),

    ("Decrypto", "USDT", "Stablecoin USD", 7.5, "Pendiente"),
    ("Decrypto", "USDC", "Stablecoin USD", 7.0, "Pendiente"),

    ("Belo", "ARGt", "Stablecoin ARS", 32.0, "Pendiente"),
    ("Belo", "USDT", "Stablecoin USD", 10.0, "Pendiente"),
    ("Belo", "USDC", "Stablecoin USD", 6.0, "Pendiente"),
    ("Belo", "DAI", "Stablecoin USD", 4.0, "Pendiente"),

    ("Lemon", "USDT", "Stablecoin USD", 7.0, "Pendiente"),
    ("Lemon", "USDC", "Stablecoin USD", 6.5, "Pendiente"),
    ("Lemon", "DAI", "Stablecoin USD", 4.5, "Pendiente"),

    ("Bitso", "USDT", "Stablecoin USD", 3.5, "Pendiente"),
    ("Bitso", "USDC", "Stablecoin USD", 3.5, "Pendiente"),
    ("Bitso", "DAI", "Stablecoin USD", 3.0, "Pendiente"),

    ("SatoshiTango", "USDC", "Stablecoin USD", 4.0, "Pendiente"),
    ("SatoshiTango", "USDT", "Stablecoin USD", 4.0, "Pendiente"),

    ("Bitget", "USDT", "Stablecoin USD", 9.0, "Pendiente"),
    ("Binance", "USDT", "Stablecoin USD", 8.5, "Pendiente"),
    ("BingX", "USDT", "Stablecoin USD", 8.0, "Pendiente"),

    ("YouHodler", "USDT", "Stablecoin USD", 12.0, "Pendiente"),
    ("Nexo", "USDT", "Stablecoin USD", 10.0, "Pendiente"),
]

COLUMNAS = [
    "Plataforma",
    "Activo",
    "Categoría",
    "Tasa (%)",
    "Tipo de tasa",
    "Verificada",
    "Fecha de verificación",
    "Fuente oficial",
    "Condiciones",
]

# Se crea la tabla sin atribuirle actualidad a los valores.
df = pd.DataFrame(
    DATOS,
    columns=[
        "Plataforma",
        "Activo",
        "Categoría",
        "Tasa (%)",
        "Tipo de tasa",
    ],
)

df["Verificada"] = False
df["Fecha de verificación"] = None
df["Fuente oficial"] = ""
df["Condiciones"] = "Pendiente de comprobar"

# =========================================================
# ENCABEZADO Y MÉTRICAS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Plataformas incluidas",
        df["Plataforma"].nunique(),
    )

with col2:
    st.metric(
        "Productos registrados",
        len(df),
    )

with col3:
    st.metric(
        "Tasas verificadas",
        int(df["Verificada"].sum()),
    )

st.caption(
    "Fecha y hora de consulta: "
    + datetime.now(
        ZoneInfo("America/Argentina/Buenos_Aires")
    ).strftime("%d/%m/%Y %H:%M")
)

st.divider()

# =========================================================
# FILTROS
# =========================================================

st.subheader("🔎 Filtrar productos")

f1, f2, f3 = st.columns(3)

with f1:
    categorias = ["Todas"] + sorted(df["Categoría"].unique())
    categoria = st.selectbox("Tipo de activo", categorias)

with f2:
    plataformas = ["Todas"] + sorted(df["Plataforma"].unique())
    plataforma = st.selectbox("Plataforma", plataformas)

with f3:
    estados = ["Todos", "Verificados", "No verificados"]
    estado = st.selectbox("Estado de la tasa", estados)

filtrado = df.copy()

if categoria != "Todas":
    filtrado = filtrado[filtrado["Categoría"] == categoria]

if plataforma != "Todas":
    filtrado = filtrado[filtrado["Plataforma"] == plataforma]

if estado == "Verificados":
    filtrado = filtrado[filtrado["Verificada"] == True]
elif estado == "No verificados":
    filtrado = filtrado[filtrado["Verificada"] == False]

# =========================================================
# RANKING
# =========================================================

st.subheader("🏆 Ranking de rendimientos")

st.info(
    "El ranking solo ordena los porcentajes cargados. "
    "Una tasa pendiente de verificación no representa una "
    "oferta vigente ni una recomendación de inversión."
)

# Los productos se ordenan por tasa, pero el estado de
# verificación permanece visible en la tabla.
filtrado = filtrado.sort_values(
    "Tasa (%)",
    ascending=False,
    na_position="last",
).reset_index(drop=True)

filtrado.insert(0, "Puesto", range(1, len(filtrado) + 1))

st.dataframe(
    filtrado,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Tasa (%)": st.column_config.NumberColumn(
            "Tasa anual informada (%)",
            format="%.2f%%",
        ),
        "Verificada": st.column_config.CheckboxColumn(
            "Tasa verificada",
        ),
        "Fuente oficial": st.column_config.LinkColumn(
            "Consultar fuente",
            display_text="Abrir fuente",
        ),
    },
)

# =========================================================
# EXPLICACIÓN
# =========================================================

with st.expander("📘 Cómo interpretar las tasas"):
    st.markdown(
        """
        - **TNA:** tasa nominal anual. No equivale necesariamente
          al rendimiento efectivo anual.
        - **TEA:** tasa efectiva anual, que contempla la
          capitalización según sus condiciones de cálculo.
        - **APY:** rendimiento anual efectivo, normalmente
          expresado considerando la capitalización.
        - **APR:** tasa anualizada que no necesariamente incluye
          capitalización.
        - **Verificada:** indica que la tasa fue comprobada en
          una fuente identificable y en una fecha determinada.
        - **Riesgo:** una tasa elevada no garantiza que se pueda
          recuperar el capital ni que el activo conserve su valor.
        """
    )

st.caption(
    "Este comparador es informativo. No constituye asesoramiento "
    "financiero. Las tasas, condiciones y riesgos pueden cambiar."
)
```
