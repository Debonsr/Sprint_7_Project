import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Anuncios de coches en EE. UU.', layout='wide')


@st.cache_data
def load_data():
    """Lee el conjunto de datos de anuncios de venta de coches."""
    return pd.read_csv('vehicles_us.csv')


car_data = load_data()

# Encabezado
st.header('Panel de anuncios de venta de coches en EE. UU.')
st.write(
    'Explora el conjunto de datos de anuncios de vehículos usados: '
    'marca las casillas para construir los gráficos.'
)

# Métricas generales
col1, col2, col3 = st.columns(3)
col1.metric('Anuncios', f'{len(car_data):,}')
col2.metric('Precio mediano', f"${car_data['price'].median():,.0f}")
col3.metric('Kilometraje mediano (millas)', f"{car_data['odometer'].median():,.0f}")

# Vista previa de los datos
if st.checkbox('Mostrar los datos'):
    st.dataframe(car_data.head(100))

# Histograma
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    hist_column = st.selectbox(
        'Columna para el histograma',
        ['odometer', 'price', 'model_year', 'days_listed'],
    )
    fig = px.histogram(car_data, x=hist_column, nbins=100, title=f'Distribución de {hist_column}')
    st.plotly_chart(fig, width='stretch')

# Gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter:
    st.write('Creación de un gráfico de dispersión entre el odómetro y el precio')
    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        color='condition',
        opacity=0.5,
        title='Relación entre odómetro y precio',
    )
    st.plotly_chart(fig, width='stretch')
