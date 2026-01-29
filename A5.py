import streamlit as st

st.set_page_config(
    page_title="BurnoutGuard - Exploración inicial", 
    layout="wide",
    page_icon=":ambulance:",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:david.mejia.cascante@gmail.com',
        'About': "# Created by David Mejia for te *TFM*."
    }
    )
st.set_option("client.showSidebarNavigation", True)

st.logo("img/logo.png")


# Using "with" notation
with st.sidebar:
    st.title('Asignatura 5.Fuentes y Obtención de Datos.')
    st.header('BURNOUTGUARD: Sistema De Detección Temprana De Riesgo De Burnout.')
    st.subheader('Profesaora:')
    st.text('Xisca Sorell')
    st.subheader('Integrantes:')
    st.text('David Mejía Cascante\nDaniel Vargas Salazar\nJuan Luis Chávez Mejía\nMaría Cubero Sandoval\nMelany Jiménez Nin')
    st.subheader('Enero 2026')

# col1,col2 = st.columns([1,4])
# with col1:
#     st.subheader('Profesaora:')
#     st.text('Xisca Sorell')
#     st.subheader('Integrantes:')
#     st.text('David Mejía Cascante\nDaniel Vargas Salazar\nJuan Luis Chávez Mejía\nMaría Cubero Sandoval\nMelany Jiménez Nin')
#     st.subheader('Enero 2026')
# with col2:
#     st.title("DASHBOARD")
#     st.write("Explorador simple para el dataset procesado. Ejecutar después del Notebook 02.")

st.title("DASHBOARD")
st.write("Explorador simple para el dataset procesado. Ejecutar después del Notebook 02.")
tab1, tab2, tab3 = st.tabs([":rocket: API", ":floppy_disk: KAGGLE", ":notebook: TEST"])

with tab1:
    st.header("Este tablero presenta una identificación exploratoria de compañías con entornos laborales adversos, utilizando comentarios públicos de empleados obtenidos de plataformas de reseñas laborales.")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
    st.image("https://static.streamlit.io/examples/dog.jpg", width=300)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab3:
    col1,col2 = st.columns(2)
    with col1:
        st.header("COL 1")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with col2:
        st.header("COL 2")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)