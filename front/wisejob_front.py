import streamlit as st
import pandas as pd
import numpy as np

st.title('WISEJOB')
st.subheader('Sistema de priorización del aprendizaje')
st.subheader('_______________________________________')

with st.sidebar:
    st.title('WISEJOB - Saturdays AI Bilbao 22-23')
    st.subheader('__________________________________________')
    st.title('Autoría:')
    st.subheader('Ana Patricia Bautista, Samuel Vidal,')
    st.subheader('Valentina González, Victor Barahona')
    st.subheader('__________________________________________')

DATE_COLUMN = 'date/time'
DATA_URL = ('dataset_reducido.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

with st.sidebar:
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Cargando datos del dataframe...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(10000)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text("Dataframe cargado! (usando la función st.cache)")
    if st.checkbox('Mostrar datos en bruto'):
        st.subheader('Datos del Dataframe')
        st.write(data)
    st.subheader('__________________________________________')
    # Radio selector para escoger tipo de gráfica
    grafico = st.radio("Elige tipo de gráfica", ('Valoración del empleo', 'Salario Estimado', 'Lugar de trabajo'))

    if grafico == 'Valoración del empleo':
        st.subheader('Valoración del empleo de 1 a 5')
        st.bar_chart(data, width=0,height=0, y='Rating')
    if grafico == 'Salario Estimado':
        st.subheader('Salario Estimado')
        st.bar_chart(data, width=0,height=0, y='Salary Estimate')
    if grafico == 'Lugar de trabajo':
        st.subheader('Lugar de trabajo')
        st.bar_chart(data, width=0,height=0, y='Location')
