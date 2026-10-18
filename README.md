# Sprint 7 – Panel de anuncios de coches

Aplicación web construida con **Streamlit**, **pandas** y **Plotly** que permite explorar un conjunto de datos de anuncios de venta de coches usados en EE. UU. (`vehicles_us.csv`).

🔗 **Aplicación desplegada en Render:** https://REEMPLAZAR-CON-TU-APP.onrender.com

## Funcionalidad

- Encabezado y métricas generales (número de anuncios, precio mediano y kilometraje mediano).
- Casilla para mostrar una vista previa de los datos.
- Casilla para construir un **histograma** interactivo; se puede elegir la columna (odómetro, precio, año del modelo o días publicados).
- Casilla para construir un **gráfico de dispersión** de odómetro frente a precio, coloreado según el estado del vehículo.

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
