# Eu não faço frontend, mas...

Workshop de Streamlit para Google Cloud Engineers que mostra como criar aplicações web de forma rápida e eficiente usando Python.

## 🚀 Setup

Execute o script abaixo para configurar seu ambiente:

```bash
# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Instalar dependências
pip install streamlit
pip install google-cloud-bigquery
pip install google-cloud-storage
pip install vertexai
pip install tenacity

# Configurar Google Cloud
gcloud auth application-default login
gcloud config set project SEU_PROJETO_ID
```

## 📁 Estrutura do Projeto

```
meu_projeto/
├── .streamlit/
│   └── config.toml
├── pages/
│   ├── 01_vertex.py
│   ├── 02_multimodal.py
│   ├── 03_bigquery.py
│   └── 04_storage.py
├── app.py
└── requirements.txt
```

## 🎯 Exemplos

### 1. Aplicação Básica
```bash
streamlit run app.py
```
Demonstra os conceitos básicos do Streamlit com um exemplo simples de interface.

### 2. Integração com Vertex AI
```bash
streamlit run pages/01_vertex.py
```
Mostra como usar o Gemini Pro 002 para gerar conteúdo.

### 3. Envio Multimodal
```bash
streamlit run pages/02_multimodal.py
```
Exemplo de como enviar imagens e texto para o Vertex AI.

### 4. Explorador de BigQuery
```bash
streamlit run pages/03_bigquery.py
```
Lista datasets e tabelas do BigQuery.

### 5. Navegador de Storage
```bash
streamlit run pages/04_storage.py
```
Explora buckets e objetos no Cloud Storage.

## ⚙️ Configuração

1. Configure o tema e comportamento do Streamlit:
```toml
# .streamlit/config.toml
[theme]
primaryColor = "#2b5b84"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

2. Configure as variáveis de ambiente:
```bash
export GCP_PROJECT="seu-projeto"
export GCP_REGION="sua-regiao"
```

## 🔍 Melhores Práticas Implementadas

1. **Organização de Código**
   - Separação de lógica e interface
   - Uso de funções reutilizáveis
   - Cache de dados pesados

2. **Tratamento de Erros e Cache**
   - Decoradores para cache
   - Retry para resiliência
   - Tratamento amigável de erros

3. **Configuração do Streamlit**
   - Tema personalizado
   - Múltiplas páginas
   - Configurações otimizadas

4. **Logging e Monitoramento**
   - Logging estruturado
   - Monitoramento de performance
   - Métricas de uso

## 📝 Notas

- Certifique-se de ter as permissões adequadas no GCP
- Use `gcloud auth application-default login` antes de executar os exemplos
- Monitore o uso de recursos e implemente cache quando necessário

## 🤝 Contribuindo

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

## 📫 Contato

- Twitter: @duboc
- LinkedIn: /in/duboc
- Email: duboc@google.com
