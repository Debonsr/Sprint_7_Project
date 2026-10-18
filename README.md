# Sprint 7 – Panel de anuncios de coches

Aplicación web construida con **Streamlit**, **pandas** y **Plotly** que permite explorar un conjunto de datos de anuncios de venta de coches usados en EE. UU. (`vehicles_us.csv`).

🔗 **Aplicación desplegada en Render:** https://REEMPLAZAR-CON-TU-APP.onrender.com

## Funcionalidad

- **Visor de datos:** tabla con todos los anuncios y una casilla para incluir o excluir a los fabricantes con menos de 1000 anuncios (el filtro se aplica a todo el panel).
- **Tipos de vehículo por fabricante:** histograma apilado con el número de anuncios de cada fabricante por tipo de vehículo.
- **Histograma de `condition` vs `model_year`:** distribución del año del modelo según el estado del vehículo.
- **Comparar la distribución de precios entre fabricantes:** dos listas desplegables para elegir los fabricantes y una casilla para normalizar el histograma (en porcentaje).
- **Gráfico de dispersión:** relación entre el odómetro y el precio, coloreada según el estado del vehículo.

## Estructura del proyecto

```
├── app.py                 # Código de la aplicación web
├── vehicles_us.csv        # Conjunto de datos
├── requirements.txt       # Librerías necesarias
├── notebooks/
│   └── EDA.ipynb          # Análisis exploratorio de datos
└── .streamlit/
    └── config.toml        # Configuración de Streamlit para Render
```

## Ejecución local

```bash
conda create -n vehicles_env -c conda-forge python=3.11 pandas plotly nbformat
conda activate vehicles_env
pip install streamlit
streamlit run app.py
```

La aplicación se abre en http://localhost:10000.

## Despliegue en Render

- **Build Command:** `pip install --upgrade pip && pip install -r requirements.txt`
- **Start Command:** `streamlit run app.py`
