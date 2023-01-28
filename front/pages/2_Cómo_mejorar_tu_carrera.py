import streamlit as st
import pandas as pd
import numpy as np
import gzip

import joblib
import sklearn
#import re


st.title('CÓMO MEJORAR TU CARRERA')
st.write('Selecciona en el siguiente formulario cuál es tu situación laboral actual, cuáles son tus habilidades y cuáles son tus preferencias sobre tu puesto de trabajo')


#Loading models

def load_model(filename):
	with gzip.open(filename, 'rb') as cf:
		return joblib.load(filename)
		
def load_dataset_line(filename):
	with gzip.open(filename, 'rb') as cf:
		return pd.read_csv(cf, nrows=1)

model_salary = load_model('models/model_salary.joblib.gz')
model_rating = load_model('models/model_rating.joblib.gz')

dataset_salary = load_dataset_line('datasets/dataset_salary.csv.gz').drop(columns=['Unnamed: 0', 'Job Title', 'Salary Estimate', 'Job Description', 'Location', 'Rating', 'Headquarters', 'Size', 'desc_words', 'salary'])
dataset_rating = load_dataset_line('datasets/dataset_rating.csv.gz').drop(columns=['Unnamed: 0', 'Job Title', 'Salary Estimate', 'Job Description', 'Location', 'Rating', 'Headquarters', 'Size', 'scope_DataAnalyst', 'scope_DataEngineer', 'scope_DataScientist', 'desc_words', 'salary'])

salary_columns = dataset_salary.columns.tolist()
rating_columns = dataset_rating.columns.tolist()

row_salary = [0.0] * dataset_salary.shape[1]
row_rating = [0.0] * dataset_rating.shape[1]

st.title('Tu puesto de trabajo')

job_types = salary_columns[0:3]
job_types = [item.replace("scope_","") for item in job_types]
job_type = st.radio("¿Cuál de las siguientes categorías se ajusta más a tu puesto de trabajo actual?", np.array(job_types))

row_salary[salary_columns.index("scope_" + job_type)] = 1.0

st.markdown("""---""")

locations = salary_columns[43:82]
locations = [item.replace("location_cat_","") for item in locations]
location = st.radio("¿Dónde se ubica tu puesto de trabajo actual?", np.array(locations))

row_salary[salary_columns.index("location_cat_" + location)] = 1.0
row_rating[rating_columns.index("location_cat_" + location)] = 1.0

st.markdown("""---""")


# Salary preference

salary_preference = st.slider('Señala en una escala del 0 al 100 si das mayor preferencia al salario (100) o a la calidad del trabajo (0)', 0, 100, 100)

st.markdown("""---""")


# Abilities-related features


# Degrees or qualifications

st.title('Tus titulaciones')
st.write('Marca aquellas titulaciones que poseas')

degrees_names = {}
degrees_names['Estadística'] = 'statistics'
degrees_names['Física'] = 'physics'
degrees_names['Doctorado (en carreras técnicas)'] = 'phd'
degrees_names['Ingeniería de software'] = 'software engineer'
degrees_names['Desarrollo de software'] = 'software developer'
degrees_names['Titulaciones relacionadas con economía y finanzas'] = 'financial service'
degrees_names['Titulaciones relacionadas con la salud'] = 'health'
degrees_names['Ciencias de la computación'] = 'computer science'
degrees_names['Matemáticas'] = 'mathematics'
degrees_names['Licenciatura (en carreras técnicas)'] = 'bachelor\'s degree'

for feature in degrees_names.items():
	checkbox = st.checkbox(feature[0])
	if feature[1] in salary_columns:
		if checkbox:
			row_salary[salary_columns.index(feature[1])] = 1.0
		else:
			row_salary[salary_columns.index(feature[1])] = 0.0
			
	if feature[1] in rating_columns:
		if checkbox:
			row_rating[rating_columns.index(feature[1])] = 1.0
		else:
			row_rating[rating_columns.index(feature[1])] = 0.0

st.markdown("""---""")

			
# Abilities and knowledges

st.title('Tus habilidades y conocimientos')
st.write('Marca aquellas habilidades y conocimientos que consideras que dominas')

abilities_names = {}
abilities_names['Machine Learning'] = 'machine learning'
abilities_names['Deep Learning'] = 'deep learning'
abilities_names['Experiencia con SOs Linux'] = 'linux'
abilities_names['Metodologías Agile'] = 'agile'
abilities_names['Computación en la nube con Azure'] = 'azure'
abilities_names['Experiencia con SOs Windows'] = 'windows'
abilities_names['Data Science'] = 'data scientist'
abilities_names['Data Analitycs'] = 'data analyst'
abilities_names['Data Engineering'] = 'data engineer'
abilities_names['Data Visualization'] = 'data visualization'
abilities_names['Data Mining'] = 'data mining'
abilities_names['Integración continua'] = 'continuous integration'
abilities_names['Web Scrapping'] = 'web scraping'
abilities_names['Computación en la nube con AWS'] = 'aws'
abilities_names['Procesamiento de Lenguaje Natural (NLP)'] = 'nlp'
abilities_names['Metodología Scrum'] = 'scrum'
abilities_names['Experiencia en entornos Unix'] = 'unix'
abilities_names['Data pipelines'] = 'data pipeline'
abilities_names['Diseño e integración de APIs'] = 'api integration'

for feature in abilities_names.items():
	checkbox = st.checkbox(feature[0])
	if feature[1] in salary_columns:
		if checkbox:
			row_salary[salary_columns.index(feature[1])] = 1.0
		else:
			row_salary[salary_columns.index(feature[1])] = 0.0
			
	if feature[1] in rating_columns:
		if checkbox:
			row_rating[rating_columns.index(feature[1])] = 1.0
		else:
			row_rating[rating_columns.index(feature[1])] = 0.0

st.markdown("""---""")


# Programming languages

st.title('Tu experiencia como programador')
st.write('Marca aquellos lenguajes informáticos que consideras que dominas')

programs_names = {}
programs_names['Scala'] = 'scala'
programs_names['Perl'] = 'perl'
programs_names['Django'] = 'django'
programs_names['React'] = 'react'
programs_names['Java'] = 'java'
programs_names['Spark'] = 'spark'
programs_names['Hadoop'] = 'hadoop'
programs_names['SAS'] = 'sas'
programs_names['SQL'] = 'sql'
programs_names['Python'] = 'python'
programs_names['javascript'] = 'Javascript'
programs_names['Typescript'] = 'Typescript'
programs_names['MySQL'] = 'mysql'
programs_names['C#'] = 'c#'
programs_names['Ruby'] = 'ruby'
programs_names['Swift'] = 'swift'
programs_names['Rust'] = 'rust'
programs_names['MongoDB'] = 'mongodb'
programs_names['Bash'] = 'bash'

for feature in programs_names.items():
	checkbox = st.checkbox(feature[0])
	if feature[1] in salary_columns:
		if checkbox:
			row_salary[salary_columns.index(feature[1])] = 1.0
		else:
			row_salary[salary_columns.index(feature[1])] = 0.0
			
	if feature[1] in rating_columns:
		if checkbox:
			row_rating[rating_columns.index(feature[1])] = 1.0
		else:
			row_rating[rating_columns.index(feature[1])] = 0.0

st.markdown("""---""")

			
#Tools, Programs, libraries & Others

st.title('Tu dominio de herramientas y aplicaciones')
st.write('Marca aquellas herramientas, programas, librerías, etc., que consideres que manejas o dominas')

tools_names = {}
tools_names['Mathematica'] = 'mathematica'
tools_names['Kubernetes'] = 'kubernetes'
tools_names['Tableau'] = 'tableau'
tools_names['Apache Kafka'] = 'kafka'
tools_names['AWS Kinesis'] = 'kinesis'
tools_names['Azure ML'] = 'azure m'
tools_names['Project Management'] = 'project manage'
tools_names['Herramientas de testeo de código'] = 'testing'
tools_names['Talend'] = 'talend'
tools_names['OnBase'] = 'onbase'
tools_names['Redshift'] = 'redshift'
tools_names['BigQuery'] = 'bigquery'
tools_names['Jupyter'] = 'jupyter'
tools_names['Librería matplotlib'] = 'matplotlib'
tools_names['Natural Language Toolkit (NLTK)'] = 'nltk'
tools_names['Python Pandas'] = 'pandas'
tools_names['NumPy'] = 'numpy'
tools_names['RapidMiner'] = 'rapidminer'
tools_names['Minitab'] = 'minitab'
tools_names['DataRobot'] = 'datarobot'
tools_names['SSRS'] = 'ssrs'
tools_names['Altair Data Analytics'] = 'altair'
tools_names['Databricks'] = 'databricks'
tools_names['Git'] = 'git'
tools_names['AWS EC2'] = 'ec2'
tools_names['PySpark'] = 'pyspark'
tools_names['HDFS'] = 'hdfs'
tools_names['Microsoft Office'] = 'microsoft office'
tools_names['XML'] = 'xml'

for feature in tools_names.items():
	checkbox = st.checkbox(feature[0])
	if feature[1] in salary_columns:
		if checkbox:
			row_salary[salary_columns.index(feature[1])] = 1.0
		else:
			row_salary[salary_columns.index(feature[1])] = 0.0
			
	if feature[1] in rating_columns:
		if checkbox:
			row_rating[rating_columns.index(feature[1])] = 1.0
		else:
			row_rating[rating_columns.index(feature[1])] = 0.0

st.markdown("""---""")


X_salary = dataset_salary[0:0]
X_salary.loc[len(X_salary)] = row_salary

X_rating = dataset_rating[0:0]
X_rating.loc[len(X_rating)] = row_rating

predictions_salary = model_salary.predict(X_salary)[0] * 1000
predictions_rating = model_rating.predict(X_rating)[0]


st.title('Cuál debería ser tu salario y la calidad de tu empleo')
st.write('Estimación ealizada en base a las preferencias y habilidades arriba mencionadas')

st.subheader("Salario promedio según tus preferencias y habilidades")
st.title(round(predictions_salary, 0))

st.subheader("Valoración promedio (de 1 a 5) de tu empresa")
st.title(round(predictions_rating, 2))

st.markdown("""---""")
st.title('Mejores alternativas: cómo mejorar tu carrera')
st.write('Estimación de la mejor alternativa en cada categoría, realizada en base a tus preferencias y habilidades. Se tendrá en cuenta para la recomendación el balance entre salario y calidad de empleo que has indicado arriba')

st.subheader("¿Dónde podría mudarme?")

chosen_location = location
better_salary = predictions_salary
better_rating = predictions_rating
current_coefficient = (predictions_salary * salary_preference) / 191500 + (predictions_rating * (100 - salary_preference)) / 4
better_coefficient = current_coefficient

for location_alter in locations:
	if location_alter == location:
		continue
	row_salary_alter = row_salary
	row_salary_alter[salary_columns.index("location_cat_" + location)] = 0.0
	row_salary_alter[salary_columns.index("location_cat_" + location_alter)] = 1.0
	X_salary = dataset_salary[0:0]
	X_salary.loc[len(X_salary)] = row_salary_alter
	salary_alter = model_salary.predict(X_salary)[0] * 1000

	row_rating_alter = row_rating
	row_rating_alter[rating_columns.index("location_cat_" + location)] = 0.0
	row_rating_alter[rating_columns.index("location_cat_" + location_alter)] = 1.0
	X_rating = dataset_rating[0:0]
	X_rating.loc[len(X_rating)] = row_rating_alter
	rating_alter = model_rating.predict(X_rating)[0]
	
	new_coefficient = (salary_alter * salary_preference) / 191500 + (rating_alter * (100 - salary_preference)) / 4
	
	if new_coefficient > better_coefficient:
		better_coefficient = new_coefficient
		chosen_location = location_alter
		better_salary = salary_alter
		better_rating = rating_alter
		
st.title("Mejor opción: " + chosen_location)
st.write("Nuevo salario promedio: " + str(round(better_salary, 0)) + "   Diferencia: " + str(round(better_salary - predictions_salary, 0)))
st.write("Nuevo rating promedio: " + str(round(better_rating, 2)) + "   Diferencia: " + str(round(better_rating - predictions_rating, 2)))

st.markdown("""---""")


alter_texts = ["¿Qué titulación debería obtener?", "¿Qué habilidad o conocimiento debería adquirir?", "¿Qué lenguaje informático debería dominar?", "¿Que herramientas y aplicaciones debería aprender a manejar?"]

i = -1

for abilities_list in [degrees_names, abilities_names, programs_names, tools_names]:

	i += 1
	st.subheader(alter_texts[i])

	chosen_option = "No one"
	better_salary = predictions_salary
	better_rating = predictions_rating
	current_coefficient = (predictions_salary * salary_preference) / 191500 + (predictions_rating * (100 - salary_preference)) / 4
	better_coefficient = current_coefficient

	for alter in abilities_list.items():
		if 	alter[1] not in salary_columns or row_salary[salary_columns.index(alter[1])] == 1.0:
			continue
		row_salary_alter = row_salary
		row_salary_alter[salary_columns.index(alter[1])] = 1.0
		X_salary = dataset_salary[0:0]
		X_salary.loc[len(X_salary)] = row_salary_alter
		salary_alter = model_salary.predict(X_salary)[0] * 1000
		
		if 	alter[1] not in rating_columns or row_rating[rating_columns.index(alter[1])] == 1.0:
			continue
		row_rating_alter = row_rating
		row_rating_alter[rating_columns.index(alter[1])] = 1.0
		X_rating = dataset_rating[0:0]
		X_rating.loc[len(X_rating)] = row_rating_alter
		rating_alter = model_rating.predict(X_rating)[0]
	
		new_coefficient = (salary_alter * salary_preference) / 191500 + (rating_alter * (100 - salary_preference)) / 4
	
		if new_coefficient > better_coefficient:
			better_coefficient = new_coefficient
			chosen_option = alter[0]
			better_salary = salary_alter
			better_rating = rating_alter
		
	st.title("Mejor opción: " + chosen_option)
	st.write("Nuevo salario promedio: " + str(round(better_salary, 0)) + "   Diferencia: " + str(round(better_salary - predictions_salary, 0)))
	st.write("Nuevo rating promedio: " + str(round(better_rating, 2)) + "   Diferencia: " + str(round(better_rating - predictions_rating, 2)))
	st.markdown("""---""")