import streamlit as st
import pandas as pd
from utils import predict_flores

# Título de la aplicación
st.title('Mide el pétalo y sépalo desde un CSV')
st.image('floriris.jpg', caption='Imagen de iris', use_column_width=True)

# Widget para cargar un archivo CSV
uploaded_file = st.file_uploader("Selecciona el CSV", type=['csv'])

# Si se carga un archivo
if uploaded_file is not None:
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(uploaded_file)

    # Mostrar una vista previa de los primeros registros del DataFrame
    st.write('**DataFrame:**')
    st.write(df.head())

    # Sección para realizar la predicción
    st.subheader('Realizar la predicción')

    # Widget para seleccionar las columnas a utilizar para la predicción
    feature_cols = st.multiselect('Selecciona las columnas para la predicción', df.columns)

    # Botón para realizar la predicción con las columnas seleccionadas
    if st.button('Realizar Predicción con CSV'):
        # Realizar la predicción utilizando las columnas seleccionadas
        predicted_values = predict_flores(df[feature_cols])

        # Mostrar los resultados de la predicción
        st.success('Éxito al realizar la predicción!')
        st.write('Los resultados son:')
        st.write(predicted_values)

        # Convertir los resultados de la predicción a un DataFrame
        predictions_df = pd.DataFrame(predicted_values, columns=['Predicciones'])

        # Widget para descargar el archivo CSV de las predicciones
        st.subheader('Descargar como CSV')
        st.download_button(label='Descargar CSV',
            data=predictions_df.to_csv(index=False),
            file_name='predicciones.csv',
            mime='text/csv')


