import streamlit as st
import pandas as pd
import numpy as np
import gzip

from PIL import Image

st.set_page_config(
    page_title="WiseJob - Impulsa tu carrera",
    page_icon="💡",
)

st.title('WISEJOB')
st.subheader('Impulsa tu carrera')
st.write('WiseJob es una herramienta que utiliza inteligencia artificial para ofrecerte recomendaciones personalizadas que te orienten a la hora de escoger en qué conocimientos o habilidades enfocar tu formación futura para maximizar tu éxito laboral y profesional. Además, WiseJob te permite conocer en qué lugares podrías aumentar tu salario o mejorar tus condiciones laborales, en caso de que estés pensando en cambiar de aires para impulsar tu carrera.')
st.write('Nuestras recompendaciones están basadas en una encuesta sobre tu formación, experiencia y preferencias que puedes rellenar en menos de dos minutos. Nuestro modelo de inteligencia artificial cotejará tu perfil con el de muchos otros trabajadores, ofreciéndote aquellas recomendaciones que optimicen el resultado que desees para el futuro de tu carrera.')
st.write('Haz click en "Cómo mejorar tu carrera" en el panel de la izquieerda, ¡y lleva tu carrera al siguiente nivel con Wisejob!')
st.markdown("""---""")

st.title('Nuestro equipo')

image = Image.open('team_photo.png')

st.image(image, caption='')

st.write('Víctor Barahona')
st.write('Ana Patricia Bautista')
st.write('Valentina González')
st.write('Samuel Vidal')
st.markdown("""---""")

st.subheader('Proyecto presentado en el Saturdays.AI Bilbao, 2022')
st.markdown("""---""")