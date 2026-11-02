```python
import pandas as pd
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="Rendimientos Fintech Argentina",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Ranking de Rendimientos Fintech Argentina")

st.caption(
    "Comparador de billeteras virtuales, stablecoins y "
    "plataformas de inversión."
)

# ==========================================================
# AVISO IMPORTANTE
# ==========================================================

st.warning(
    "Las tasas de esta versión provienen de valores cargados "
    "manualmente. No están verificadas en tiempo real y no "
    "deben interpretarse como ofertas vigentes. Consultá las "
    "condiciones de cada plataforma antes de invertir."
)

# ==========================================================
# DATOS
# ==========================================================
# Las tasas son las del script original del usuario.
# No se afirma que estén vigentes.
#
# "Tipo de tasa" se deja como "Sin verificar" porque no se
# comprobó si cada valor corresponde a TNA, TEA, APY o APR.
#
# La fecha de consulta de la aplicación NO es la fecha de
# verificación de las tasas.

DATOS = [
    {
        "Plataforma": "Personal Pay",
        "Activo": "ARS",
        "Categoría": "Cuenta remunerada en pesos",
        "Tasa (%)": 21.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.personalpay.com.ar/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Naranja X",
        "Activo": "ARS",
        "Categoría": "Cuenta remunerada en pesos",
        "Tasa (%)": 19.5,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.naranjax.com/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Mercado Pago",
        "Activo": "ARS",
        "Categoría": "FCI en pesos",
        "Tasa (%)": 19.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.mercadopago.com.ar/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Rendimiento variable; consultar el fondo",
    },
    {
        "Plataforma": "Buenbit",
        "Activo": "USDT",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 8.5,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.buenbit.com/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Buenbit",
        "Activo": "USDC",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 8.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.buenbit.com/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Buenbit",
        "Activo": "nuARS",
        "Categoría": "Criptoactivo vinculado al peso",
        "Tasa (%)": 25.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.buenbit.com/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Ripio",
        "Activo": "UXD",
        "Categoría": "Criptoactivo; vinculación por comprobar",
        "Tasa (%)": 10.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.ripio.com/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Verificar activo y producto",
    },
    {
        "Plataforma": "Ripio",
        "Activo": "USDT",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 6.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.ripio.com/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Decrypto",
        "Activo": "USDT",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 7.5,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.decrypto.la/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Decrypto",
        "Activo": "USDC",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 7.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www.decrypto.la/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Belo",
        "Activo": "ARGt",
        "Categoría": "Criptoactivo vinculado al peso",
        "Tasa (%)": 32.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www belo.app/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Verificar activo, tasa y disponibilidad",
    },
    {
        "Plataforma": "Belo",
        "Activo": "USDT",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 10.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www belo.app/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Verificar promoción y requisitos",
    },
    {
        "Plataforma": "Belo",
        "Activo": "USDC",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 6.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www belo.app/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Belo",
        "Activo": "DAI",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 4.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://www belo.app/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Lemon",
        "Activo": "USDT",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 7.0,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://lemon.me/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Verificar producto y periodicidad",
    },
    {
        "Plataforma": "Lemon",
        "Activo": "USDC",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 6.5,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://lemon.me/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Lemon",
        "Activo": "DAI",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 4.5,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://lemon.me/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Pendientes de comprobar",
    },
    {
        "Plataforma": "Bitso",
        "Activo": "USDT",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 3.5,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://bitso.com/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Verificar disponibilidad regional",
    },
    {
        "Plataforma": "Bitso",
        "Activo": "USDC",
        "Categoría": "Criptoactivo vinculado al dólar",
        "Tasa (%)": 3.5,
        "Tipo de tasa": "Sin verificar",
        "Fuente oficial": "https://bitso.com/",
        "Verificada": False,
        "Fecha de verificación": None,
        "Condiciones": "Verificar disponibilidad regional",
    },
    {
        "Plataforma": "Bitso",
        "Activo": "DA
