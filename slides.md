---
marp: true
theme: default
class: 
 - lead
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .content-left {
    grid-column: 1;
    font-size: 1.1em;
    padding-right: 1rem;
    line-height: 1.5;
  }
  .code-right {
    grid-column: 2;
    background-color: #f6f8fa;
    padding: 1rem;
    border-radius: 8px;
    font-size: 0.9em;
  }
  .centered-content {
    text-align: center;
    padding: 2rem;
  }
  section::after {
    content: '';
    background-image: url('images/logo.png');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: right bottom;
    width: 100px;
    height: 40px;
    position: absolute;
    right: 30px;
    bottom: 20px;
  }
---

<!-- _backgroundColor: #2b5b84 -->
<!-- _color: white -->
# Eu não faço frontend, mas...
#### Sempre quis fazer, mas não espalha :shushing_face:

---

<!-- _backgroundColor: white -->
<div class="centered-content">

# Por que backend developers "odeiam" frontend? 

![height:250](https://api.placeholder.com/300x200)

</div>

---

<!-- _backgroundColor: white -->
<div class="columns">
<div class="content-left">

# O que é Streamlit?

### Uma nova esperança para devs backend

- Framework Python para criar apps web
- Zero conhecimento de HTML/CSS/JS
- Deploy com um comando
- Atualização em tempo real

</div>
<div class="code-right">

```bash
# Instalação
pip install streamlit

# Criar primeiro app
streamlit run app.py

# Deploy
streamlit deploy
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

# Começando com Streamlit

### É literalmente só isso 👉

Seu primeiro app em 30 segundos:
1. Instale o Streamlit
2. Crie um arquivo Python
3. Execute com `streamlit run`
4. Pronto! 🎉

</div>
<div class="code-right">

```python
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
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

## Melhor Prática #1: 
### Organize seu código

- Separe a lógica da interface
- Use funções para operações repetitivas
- Mantenha o código principal limpo
- Cache dados pesados

</div>
<div class="code-right">

```python
import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados():
    return pd.read_csv('dados.csv')

def processar_dados(df):
    return df.groupby('categoria').sum()

def main():
    st.title("Dashboard de Vendas")
    
    df = carregar_dados()
    dados_processados = processar_dados(df)
    st.line_chart(dados_processados)

if __name__ == '__main__':
    main()
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

## Widgets do Streamlit

### Interatividade fácil

- **Botão**: `st.button`
- **Controle deslizante**: `st.slider`
- **Caixa de seleção**: `st.selectbox`
- **Checkbox**: `st.checkbox`
- **Botões de opção**: `st.radio`

</div>
<div class="code-right">

```python
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
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

## Integração com Google Vertex AI

### Usando o Gemini Pro 002

- Conecte-se à API do Vertex AI
- Gere conteúdo com o modelo Gemini Pro 002
- Integração fácil com Streamlit

</div>
<div class="code-right">

```python
import os
import streamlit as st
from vertexai import init
from vertexai.generative_models import GenerativeModel, GenerationConfig

# Inicializar Vertex AI
PROJECT_ID = os.getenv("GCP_PROJECT")
LOCATION = os.getenv("GCP_REGION")
init(project=PROJECT_ID, location=LOCATION)

# Configurar modelo
model = GenerativeModel("gemini-1.5-flash-002")

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
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

## Envio Multimodal para Vertex AI

### Integração de Imagem e Texto

- Envie imagens e texto para a API do Vertex AI
- Use modelos multimodais para processamento avançado
- Integração fácil com Streamlit

</div>
<div class="code-right">

```python
import os
import streamlit as st
from vertexai import init
from vertexai.generative_models import GenerativeModel, GenerationConfig, Part

# Inicializar Vertex AI
PROJECT_ID = os.getenv("GCP_PROJECT")
LOCATION = os.getenv("GCP_REGION")
init(project=PROJECT_ID, location=LOCATION)

# Configurar modelo
model = GenerativeModel("gemini-1.5-flash-002")

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
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

## Melhor Prática #2: 
### Tratamento de Erros e Cache

- Use decoradores para cache inteligente
- Implemente retry para resiliência
- Trate erros de forma amigável
- Monitore uso de recursos

</div>
<div class="code-right">

```python
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
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

## Melhor Prática #3: 
### Configuração do Streamlit

📁 **Estrutura de Pastas**
```
meu_projeto/
├── .streamlit/
│   └── config.toml
├── pages/
   ├── 01_pagina1.py
│   └── 02_pagina2.py
├── app.py
└── requirements.txt
```

- Configure tema e comportamento
- Organize páginas múltiplas
- Defina variáveis globais
- Personalize a aparência

</div>
<div class="code-right">

```toml
# .streamlit/config.toml

[theme]
primaryColor = "#2b5b84"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
port = 8501
address = "0.0.0.0"
maxUploadSize = 200
enableXsrfProtection = true

[browser]
gatherUsageStats = false
serverAddress = "localhost"

[runner]
magicEnabled = true
fastRerenderEnabled = true

[client]
showErrorDetails = false
toolbarMode = "minimal"
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

## Conectando ao BigQuery

### Visualize seus Datasets

- Usa credenciais do `gcloud auth`
- Liste todos os datasets disponíveis
- Visualize tabelas e schemas
- Cache inteligente para queries

💡 **Dica**: Execute antes:
```bash
gcloud auth application-default login
```

</div>
<div class="code-right">

```python
import streamlit as st
from google.cloud import bigquery

# Usar credenciais padrão do ambiente
client = bigquery.Client()

@st.cache_data(ttl=600)  # Cache por 10 minutos
def listar_datasets():
    try:
        datasets = list(client.list_datasets())
        return [dataset.dataset_id 
                for dataset in datasets]
    except Exception as e:
        st.error(f"Erro ao listar datasets: {e}")
        return []

@st.cache_data
def mostrar_tabelas(dataset_id):
    tables = client.list_tables(dataset_id)
    return [table.table_id for table in tables]

st.title('Explorador de BigQuery')

# Lista datasets
datasets = listar_datasets()
if datasets:
    dataset_selecionado = st.selectbox(
        'Selecione um dataset:', datasets
    )

    if dataset_selecionado:
        # Lista tabelas do dataset
        tabelas = mostrar_tabelas(dataset_selecionado)
        st.write('### Tabelas disponíveis:')
        for tabela in tabelas:
            st.write(f'📊 {tabela}')
else:
    st.warning('Configure suas credenciais GCP!')
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

## Explorando Cloud Storage

### Navegue pelos Buckets

- Lista todos os buckets disponíveis
- Explora objetos dentro dos buckets
- Visualização hierárquica
- Cache inteligente para listagens

💡 **Dica**: Use `delimiter='/'` para 
navegar como em um sistema de arquivos

</div>
<div class="code-right">

```python
import streamlit as st
from google.cloud import storage

# Usar credenciais padrão do ambiente
client = storage.Client()

@st.cache_data(ttl=300)  # Cache por 5 minutos
def listar_buckets():
    try:
        return [bucket.name 
                for bucket in client.list_buckets()]
    except Exception as e:
        st.error(f"Erro ao listar buckets: {e}")
        return []

@st.cache_data(ttl=60)
def listar_objetos(bucket_name, prefix=""):
    try:
        bucket = client.get_bucket(bucket_name)
        blobs = bucket.list_blobs(
            prefix=prefix, 
            delimiter='/'
        )
        # Lista arquivos
        files = [blob.name for blob in blobs]
        # Lista "pastas"
        folders = list(blobs.prefixes)
        return files, folders
    except Exception as e:
        st.error(f"Erro ao listar objetos: {e}")
        return [], []

st.title('Explorador de Storage')

# Lista buckets
buckets = listar_buckets()
if buckets:
    bucket_selecionado = st.selectbox(
        'Selecione um bucket:', buckets
    )

    if bucket_selecionado:
        # Lista objetos do bucket
        files, folders = listar_objetos(bucket_selecionado)
        
        st.write('### Pastas:')
        for folder in folders:
            st.write(f'📁 {folder}')
        
        st.write('### Arquivos:')
        for file in files:
            st.write(f'📄 {file}')
else:
    st.warning('Configure suas credenciais GCP!')
```

</div>
</div>

---

<div class="columns">
<div class="content-left">

## Melhor Prática #4: 
### Logging e Monitoramento

- Use logging estruturado
- Monitore performance
- Rastreie erros
- Métricas de uso

💡 **Dica**: Use `st.experimental_get_query_params()`
para rastrear origem das requisições

</div>
<div class="code-right">

```python
import streamlit as st
import logging
import time
from datetime import datetime
from contextlib import contextmanager

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@contextmanager
def timer_block(name):
    start = time.time()
    try:
        yield
    finally:
        duration = time.time() - start
        logger.info(f"{name} levou {duration:.2f} segundos")
        if duration > 1.0:  # Alerta se demorar muito
            st.warning(f"⚠️ {name} está lento!")

def log_error(e: Exception, context: str):
    logger.error(f"Erro em {context}: {str(e)}")
    st.error(f"Ops! Algo deu errado em {context}")

def registrar_uso(funcao: str):
    with timer_block(funcao):
        try:
            # Registra métricas de uso
            logger.info(
                f"Função: {funcao}\n"
                f"Usuário: {st.session_state.get('user_id')}\n"
                f"Timestamp: {datetime.now()}"
            )
            # Seu código aqui
            resultado = processar_dados()
            return resultado
        except Exception as e:
            log_error(e, funcao)
            return None

# Exemplo de uso
if st.button('Processar'):
    with st.spinner('Processando...'):
        registrar_uso('processar_dados')
```

</div>
</div>

---

<!-- _backgroundColor: #2b5b84 -->
<!-- _color: white -->

<div class="centered-content" style="text-align: center;">

```
      🤖 
   ╭─────────╮
   │ TRHANKS │
   ╰─────────╯
      /[■]\ 
     /  ║  \
    ┌───╨───┐
    │ │   │ │
    └─┘   └─┘
```
#### Dúvidas? Me procura no:
🐦 Twitter: @duboc
💼 LinkedIn: /in/duboc
📧 Email: duboc@google.com
</div>