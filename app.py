import streamlit as st

st.title('Meu Primeiro App')

nome = st.text_input(
    'Qual seu nome?'
)

if nome:
    st.write(f'Olá {nome}! 👋')
    
    if st.button('Ganhar um café'):
        st.balloons()
        st.success('☕ Café na fila!')