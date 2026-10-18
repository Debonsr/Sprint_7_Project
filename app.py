import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Anuncios de coches en EE. UU.')


@st.cache_data
def load_data():
    """Lee el conjunto de datos y añade la columna del fabricante."""
    df = pd.read_csv('vehicles_us.csv')
    # El fabricante es la primera palabra del modelo (p. ej. 'ford f-150' -> 'ford')
    df['manufacturer'] = df['model'].str.split().str[0]
    return df


car_data = load_data()

st.title('Panel de anuncios de venta de coches en EE. UU.')

# --- Visor de datos ---
st.header('Visor de datos')
include_small = st.checkbox('Incluir fabricantes con menos de 1000 anuncios', value=True)

if not include_small:
    ads_per_manufacturer = car_data['manufacturer'].value_counts()
    big_manufacturers = ads_per_manufacturer[ads_per_manufacturer >= 1000].index
    car_data = car_data[car_data['manufacturer'].isin(big_manufacturers)]

st.dataframe(car_data)

# --- Tipos de vehículo por fabricante ---
st.header('Tipos de vehículo por fabricante')
fig = px.histogram(car_data, x='manufacturer', color='type')
st.plotly_chart(fig, width='stretch')

# --- Histograma de condición vs año del modelo ---
st.header('Histograma de `condition` vs `model_year`')
fig = px.histogram(car_data, x='model_year', color='condition')
st.plotly_chart(fig, width='stretch')

# --- Comparar la distribución de precios entre fabricantes ---
st.header('Comparar la distribución de precios entre fabricantes')
manufacturers = sorted(car_data['manufacturer'].unique())
manufacturer_1 = st.selectbox(
    'Selecciona el fabricante 1',
    manufacturers,
    index=manufacturers.index('chevrolet') if 'chevrolet' in manufacturers else 0,
)
manufacturer_2 = st.selectbox(
    'Selecciona el fabricante 2',
    manufacturers,
    index=manufacturers.index('hyundai') if 'hyundai' in manufacturers else 0,
)
normalize = st.checkbox('Normalizar histograma', value=True)

compare_data = car_data[car_data['manufacturer'].isin([manufacturer_1, manufacturer_2])]
fig = px.histogram(
    compare_data,
    x='price',
    color='manufacturer',
    nbins=30,
    histnorm='percent' if normalize else None,
    barmode='overlay',
)
st.plotly_chart(fig, width='stretch')

# --- Gráfico de dispersión ---
st.header('Relación entre odómetro y precio')
if st.checkbox('Construir gráfico de dispersión', value=True):
    fig = px.scatter(car_data, x='odometer', y='price', color='condition', opacity=0.5)
    st.plotly_chart(fig, width='stretch')
