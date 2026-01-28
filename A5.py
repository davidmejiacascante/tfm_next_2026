import streamlit as st

st.set_page_config(
    page_title="BurnoutGuard - Exploración inicial", 
    layout="wide",
    page_icon="🧊",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:david.mejia.cascante@gmail.com',
        'About': "# Created by David Mejia for te *TFM*."
    }
    )
st.set_option("client.showSidebarNavigation", True)

st.logo("img/logo.png")
st.title('Asignatura 5.Fuentes y Obtención de Datos.')
st.header('BURNOUTGUARD: Sistema De Detección Temprana De Riesgo De Burnout.')

col1,col2 = st.columns([1,4])
with col1:
    st.subheader('Profesaora:')
    st.text('Xisca Sorell')
    st.subheader('Integrantes:')
    st.text('David Mejía Cascante\nDaniel Vargas Salazar\nJuan Luis Chávez Mejía\nMaría Cubero Sandoval\nMelany Jiménez Nin')
    st.subheader('Enero 2026')
with col2:
    st.title("DASHBOARD")
    st.write("Explorador simple para el dataset procesado. Ejecutar después del Notebook 02.")