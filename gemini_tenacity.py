import streamlit as st
from tenacity import retry, stop_after_attempt
from vertexai.generative_models import GenerativeModel

@st.cache_data(ttl=3600)  # Cache por 1 hora
def carregar_modelo():
    return GenerativeModel("gemini-1.5-flash-002")

@retry(stop=stop_after_attempt(3))
def gerar_resposta_segura(prompt):
    try:
        with st.spinner('Gerando resposta...'):
            modelo = carregar_modelo()
            response = modelo.generate_content(prompt)
            return response.text
    except Exception as e:
        st.error(f"Erro: {str(e)}")
        return None

# Interface principal
st.title('App Resiliente')
prompt = st.text_input('Seu prompt:')
if st.button('Gerar'):
    resultado = gerar_resposta_segura(prompt)
    if resultado:
        st.success('Gerado com sucesso!')
        st.write(resultado)