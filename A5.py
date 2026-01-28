import streamlit as st

st.set_page_config(page_title="BurnoutGuard - Exploración inicial", layout="wide")
st.logo("img/logo.png")
#st.title('Asignatura 5.Fuentes y Obtención de Datos.')
#st.header('BURNOUTGUARD: SISTEMA DE DETECCIÓN TEMPRANA DE RIESGO DE BURNOUT')
#st.subheader('Profesaora:')
#st.text('Xisca Sorell')
#st.subheader('Integrantes:')
#st.text('David Mejía Cascante | Daniel Vargas Salazar | Juan Luis Chávez Mejía | María Cubero Sandoval | Melany Jiménez Nin')


col1,col2,col3,col4 = st.columns(4)
with col1:
    st.title('Asignatura 5.Fuentes y Obtención de Datos.')
    st.header('BURNOUTGUARD: SISTEMA DE DETECCIÓN TEMPRANA DE RIESGO DE BURNOUT')
    st.subheader('Profesaora:')
    st.text('Xisca Sorell')
    st.subheader('Integrantes:')
    st.text('David Mejía Cascante \n Daniel Vargas Salazar \n Juan Luis Chávez Mejía \n María Cubero Sandoval \n Melany Jiménez Nin')
with col2:
    st.title("DASHBOARD")
    st.write("Explorador simple para el dataset procesado. Ejecutar después del Notebook 02.")
    data_path = Path("data_processed/burnoutguard_dataset.csv")
    if not data_path.exists():
        st.warning("No encuentro data_processed/burnoutguard_dataset.csv. Ejecuta notebooks/02_clean_prepare.ipynb primero.")
        st.stop()

    df = pd.read_csv(data_path)

    st.sidebar.header("Filtros")
    cols = df.columns.tolist()
    col_select = st.sidebar.multiselect("Columnas a mostrar", cols, default=cols[:10])

    st.dataframe(df[col_select].head(100))
with col3:
    st.subheader("Resumen")
    st.write(df.describe(include="all").transpose().head(30))
with col4:
    st.header('4')