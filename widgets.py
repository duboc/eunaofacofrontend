import streamlit as st

if st.button('Clique aqui'):
    st.write('Botão clicado!')

idade = st.slider('Selecione sua idade', 0, 100, 25)
st.write(f'Idade selecionada: {idade}')

opcao = st.selectbox(
    'Escolha uma opção',
    ('Opção 1', 'Opção 2', 'Opção 3')
)
st.write(f'Você escolheu: {opcao}')