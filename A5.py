import streamlit as st


st.logo("img/logo.png")
st.image("img\\logo.png")
hello = st.write('Hello world as variable!')
print(hello)
st.title('Titulo')
st.header('header')
st.subheader('subheader')
st.code('ejemplo de codigo')
st.text('ejemplo de texto')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header('1')
with col2:
    st.header('2')
with col3:
    st.header('3')
with col4:
    st.header('4')