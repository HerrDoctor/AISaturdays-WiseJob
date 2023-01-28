import streamlit as st
import pandas as pd
import numpy as np
import gzip

st.title('Nuestro dataset')
st.write('A continuación proporcionamos una sencilla herramienta con la que poder visualizar y explorar, tanto de forma directa como gráfica, el dataset utilizado para desarrollar nuestro modelo')
st.markdown("""---""")

DATE_COLUMN = 'date/time'
DATA_URL = ('dataset_reducido.csv')

#Loading datasets

def load_data(filename):
	with gzip.open(filename, 'rb') as cf:
		return pd.read_csv(cf)

dataset = load_data('datasets/dataset.csv.gz')
dataset_salary = load_data('datasets/dataset_salary.csv.gz')
dataset_rating = load_data('datasets/dataset_rating.csv.gz')


# Visualizing whole datasets

st.subheader('Visualización del dataset completo')
dataset_type = st.radio("Escoge el dataset a visualizar", ('Dataset completo', 'Dataset utilizado para inferir el salario', 'Dataset utilizado para inferir la valoración de la calidad del empleo'))

chosen_dataset = dataset

if dataset_type == 'Dataset completo':
	chosen_dataset = dataset
if dataset_type == 'Dataset utilizado para inferir el salario':
	chosen_dataset = dataset_salary
if dataset_type == 'Dataset utilizado para inferir la valoración de la calidad del empleo':
	chosen_dataset = dataset_rating

st.write(chosen_dataset)

st.markdown("""---""")

# Choosing and showing graphic
st.subheader('Representación gráfica de los datos del dataset escogido')
graphic = st.radio("Escoge la gráfica a visualizar con el dataset seleccionado", ('Valoración de la calidad del empleo', 'Salario estimado', 'Lugar de trabajo', 'Habilidad: Python', 'Habilidad: SQL', 'Habilidad: Azure'))

if graphic == 'Valoración de la calidad del empleo':
	st.subheader('Valoración entre 1 y 5')
	st.bar_chart(chosen_dataset, width=0,height=0, y='Rating', use_container_width=True)
if graphic == 'Salario estimado':
	st.subheader('Salario estimado')
	st.bar_chart(chosen_dataset, width=0,height=0, y='salary', use_container_width=True)
if graphic == 'Lugar de trabajo':
	st.subheader('Lugar de trabajo')
	st.bar_chart(dataset, width=0,height=0, y='location_cat', use_container_width=True)
if graphic == 'Habilidad: Python':
	st.subheader('Habilidad: Python')
	st.bar_chart(chosen_dataset, width=0,height=0, y='python', use_container_width=True)
if graphic == 'Habilidad: SQL':
	st.subheader('Habilidad: SQL')
	st.bar_chart(chosen_dataset, width=0,height=0, y='sql', use_container_width=True)
if graphic == 'Habilidad: Azure':
	st.subheader('Habilidad: Azure')
	st.bar_chart(chosen_dataset, width=0,height=0, y='azure', use_container_width=True)