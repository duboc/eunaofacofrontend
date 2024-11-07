import os
import streamlit as st
from vertexai import init
from vertexai.generative_models import GenerativeModel, GenerationConfig, Part

# Inicializar Vertex AI
PROJECT_ID = os.getenv("GCP_PROJECT")
LOCATION = os.getenv("GCP_REGION")
init(project=PROJECT_ID, location=LOCATION)

# Configurar modelo
model = GenerativeModel("gemini-1.5-pro-002")

def gerar_conteudo_multimodal(imagem, texto):
    image_part = Part.from_data(imagem, mime_type="image/jpeg")
    response = model.generate_content(
        [image_part, texto],
        generation_config=GenerationConfig(
            max_output_tokens=8192,
            temperature=1,
            top_p=0.95
        )
    )
    return response.text

st.title('Envio Multimodal para Vertex AI')
imagem = st.file_uploader('Envie uma imagem', type=['jpg', 'jpeg'])
texto = st.text_input('Digite seu texto:')
if st.button('Gerar'):
    if imagem and texto:
        conteudo = gerar_conteudo_multimodal(imagem.read(), texto)
        st.write(conteudo)
    else:
        st.warning('Por favor, envie uma imagem e digite um texto.')