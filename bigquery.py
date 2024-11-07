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