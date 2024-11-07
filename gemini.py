import os
import streamlit as st
from vertexai import init
from vertexai.generative_models import GenerativeModel, GenerationConfig

# Inicializar Vertex AI
PROJECT_ID = os.getenv("GCP_PROJECT")
LOCATION = os.getenv("GCP_REGION")
init(project=PROJECT_ID, location=LOCATION)

# Configurar modelo
model = GenerativeModel("gemini-1.5-pro-002")

def gerar_conteudo(prompt):
    response = model.generate_content(
        prompt,
        generation_config=GenerationConfig(
            max_output_tokens=8192,
            temperature=1,
            top_p=0.95
        )
    )
    return response.text

st.title('Gerador de Conteúdo com LLM')
prompt = st.text_input('Digite seu prompt:')
if st.button('Gerar'):
    conteudo = gerar_conteudo(prompt)
    st.write(conteudo)