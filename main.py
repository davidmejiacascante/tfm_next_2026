import pandas as pd
import requests
import time
import re
from datetime import datetime
#import matplotlib.pyplot as plt
from pathlib import Path
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

COMPANIES = [
		['DELOITTE',2763],
		['MICROSOFT',1651],
		['INTEL',1519],
		['CISCO',1425],
		['APPLE',1138],
		['NORTHROP_GRUMMAN',488],
		['LOCKHEED_MARTIN',404],
		['IBM',354],
		['SAP',10471],
		['TP',9779],
		['GOOGLE',9079],
		['ACCENTURE',4138],
		['CAPGEMINI',3803],
		['FIDELITY_INVESTMENTS',2786]
]

KEY_WORDS = ['burnout','exhaustion','depersonalization','reduced personal accomplishment','negative feedback','stress','excessive workload','work overload','role overload','job demands–resources model','customer-related stressors','emotional labor','difficult client','workplace incivility','abuse','psychosocial','job strain','effort–reward imbalance','employee well-being','work-related mental health','burnout','toxic','miserable','hell','bad']

# Using "with" notation
with st.sidebar:
    st.title('Asignatura 5.Fuentes y Obtención de Datos.')
    st.header('BURNOUTGUARD: Sistema De Detección Temprana De Riesgo De Burnout.')
    st.subheader('Profesaora:')
    st.text('Xisca Sorell')
    st.subheader('Integrantes:')
    st.text('David Mejía Cascante\nDaniel Vargas Salazar\nJuan Luis Chávez Mejía\nMaría Cubero Sandoval\nMelany Jiménez Nin')
    st.subheader('Enero 2026')

st.title("DASHBOARD")
st.write("Explorador simple para el dataset procesado. Ejecutar después del Notebook 02.")
tab1, tab2, tab3 = st.tabs([":rocket: API", ":floppy_disk: KAGGLE", ":racing_car: API Tables"])


#Ahora cargaremos en dataframes los diferentes archviso csv generados con los datos.
def load_company_data():
  df = pd.DataFrame()
  for company in COMPANIES:
    BASE_DIR = Path(__file__).resolve().parent
    filename = BASE_DIR / "data" / f"{company[0]}_reviews.csv"
    try:
      df_tmp = pd.read_csv(filename)
      df_tmp.insert(loc=0, column='company', value=str(company[0]))
      df_tmp.insert(loc=1, column='company_id', value=str(company[1]))
    except FileNotFoundError:
      continue
    df = pd.concat([df, df_tmp], ignore_index=True)
  return df

df = load_company_data()

#print(df.keys())

df1 = df.drop(columns=['diversity_and_inclusion_rating','culture_and_values_rating','review_link','years_of_employment','not_helpful_count','helpful_count','business_outlook_rating','ceo_rating'])


df1['review_datetime'] = pd.to_datetime(df1['review_datetime'], errors='coerce')
df1['company_id'] = pd.to_numeric(df1['company_id'], errors='coerce').astype('Int64')
df1['career_opportunities_rating'] = pd.to_numeric(df1['career_opportunities_rating'], errors='coerce').astype('Int64')
df1['compensation_and_benefits_rating'] = pd.to_numeric(df1['compensation_and_benefits_rating'], errors='coerce').astype('Int64')
df1['senior_management_rating'] = pd.to_numeric(df1['senior_management_rating'], errors='coerce').astype('Int64')
df1['work_life_balance_rating'] = pd.to_numeric(df1['work_life_balance_rating'], errors='coerce').astype('Int64')
df1['rating'] = pd.to_numeric(df1['rating'], errors='coerce').astype('Int64')
df1['is_current_employee'] = df1['is_current_employee'].astype('category')
df1['employment_status'] = df1['employment_status'].astype('category')
df1['job_title'] = df1['job_title'].astype('category')
df1['location'] = df1['location'].astype('category')
df1['language'] = df1['language'].astype('category')
df1['recommend_to_friend_rating'] = df1['recommend_to_friend_rating'].astype('category')
df1['review_id'] = df1['review_id'].fillna('n/a').astype('string')
df1['summary'] = df1['summary'].fillna('n/a').astype('string')
df1['company'] = df1['company'].fillna('n/a').astype('string')
df1['pros'] = df1['pros'].fillna('n/a').astype('string')
df1['cons'] = df1['cons'].fillna('n/a').astype('string')
df1['advice_to_management'] = df1['advice_to_management'].fillna('n/a').astype('string')

#Valores nulos
df1.isna().sum().sort_values(ascending=False)

#print("Valores duplicados en el dataset: ", df1.duplicated().sum())

df1.info()

pattern = re.compile(
    r'\b(?:' + '|'.join(map(re.escape, KEY_WORDS)) + r')\b',
    flags=re.IGNORECASE
)

df1['keyword_count'] = 0 # Initialize the column with zeros
df1['keyword_count'] += df1['summary'].str.count(pattern).fillna(0).astype(int)
df1['keyword_count'] += df1['pros'].str.count(pattern).fillna(0).astype(int)
df1['keyword_count'] += df1['cons'].str.count(pattern).fillna(0).astype(int)
df1['keyword_count'] += df1['advice_to_management'].str.count(pattern).fillna(0).astype(int)

df1.to_csv('reviews.csv', index=False)

with tab1:
    st.text("Este tablero presenta una exploración de compañías con entornos laborales adversos, utilizando comentarios públicos de empleados obtenidos de plataformas de reseñas laborales.\nEsta exploración permite identificar compañías que suelen hacer que sus empleados tengan estrés, se sientan sobre trabajados y eventualmente los lleve al burn out.")
    colA1, colA2, colA3, colA4 = st.columns(4)
    #Empresas distintas dentro del reporte.
    #print(df1['company'].nunique())
    colA1.metric(label='Cantidad de compañias', value = df1['company'].nunique(), border=True)

    #Cantidad de reportes.
    treview = df1['review_id'].nunique()
    colA2.metric(label='Cantidad de reportes', value = treview, border=True)

    #Promedio del rating
    #print(df1['rating'].mean())
    colA3.metric(label='Promedio del rating de empresas', value = round(df1['rating'].mean(),2), border=True)

    #Distintos Job Titles.
    #print(df1['job_title'].nunique())
    colA4.metric(label='Distintos Job Titles', value=df1['job_title'].nunique(), border=True)

    #Distintos estados de empleamiento.
    #print(df1['employment_status'].nunique())
    colA1.metric(label='Distintos estados de empleamiento', value=df1['employment_status'].nunique(), border=True)

    #promedio de oportunidades laborares.
    #print(df['career_opportunities_rating'].mean())
    colA2.metric(label='Promedio de oportunidades laborares', value=round(df['career_opportunities_rating'].mean(),2), border=True)

    #promedio de beneficios y compensacion.
    #print(df['compensation_and_benefits_rating'].mean())
    colA3.metric(label='Promedio de beneficios y compensacion', value=round(df['compensation_and_benefits_rating'].mean(),2), border=True)

    #promedio del balance vida-trabajo
    #print(df1['work_life_balance_rating'].mean())
    colA4.metric(label='Promedio del balance vida-trabajo', value=round(df1['work_life_balance_rating'].mean(),2), border=True)

    #cantidad de keywords encontrados en todos los datos.
    #print(df1['keyword_count'].sum())
    colA1.metric(label='Cantidad de keywords encontrados en todos los datos', value=df1['keyword_count'].sum(), delta=treview, border=True)

    colA2.metric(label='Porcentaje de keywords encontrados en todos los datos', value=(str(f'{round(df1['keyword_count'].sum()/df1['review_id'].nunique(),2)},%')), delta=treview, border=True)

    dftt = pd.DataFrame(df1.groupby('company')['keyword_count'].sum())
    tcount1 = dftt['keyword_count'].max()
    tcompany1 = dftt['keyword_count'].idxmax()
    colA3.metric(label='Compañia con mas keywords encontrados:', value=tcompany1, delta=tcount1, border=True)

    dft2 = pd.DataFrame(df1.groupby('company')['review_id'].count())
    tcompany2 = dftt['keyword_count'].idxmax()
    tcount2 = dft2.loc[tcompany2, 'review_id']
    colA4.metric(label='Representacion porcentual de keywords encontrados', value=str(f'{((tcount1*100)/tcount2)},%'), delta=tcount2, border=True)

with tab2:
    st.header("Analisis del conjunto de datos de Kaggle: Global Workplace Stress and Mental Health Survey.")
    st.text('Pagina bajo construcción.')
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab3:
    colC1,colC2 = st.columns(2)
    with colC1:
        #cantidad de comentarios por empresa.
        #print(df1.groupby('company')['review_id'].count())
        colC1 = st.text('Cantidad de comentarios por empresa')
        colC1 = st.dataframe(df1.groupby('company')['review_id'].count())

        #balance de trabajo y vida personal por empresa.
        #print(df1.groupby('company')['work_life_balance_rating'].mean())
        colC1 = st.text('Balance de trabajo y vida personal por empresa')
        colC1 = st.dataframe(df1.groupby('company')['work_life_balance_rating'].mean(),)
    with colC2:
        #promedio del rating por empresa.
        #print(df1.groupby('company')['rating'].mean())
        colC2 = st.text('Promedio del rating por empresa')
        colC2 = st.dataframe(df1.groupby('company')['rating'].mean())
        
        #cantidad de keywords encontrados por empresa.
        #print(df1.groupby('company')['keyword_count'].sum())
        colC2 = st.text('Cantidad de keywords encontrados por empresa')
        colC2 = st.dataframe(df1.groupby('company')['keyword_count'].sum())