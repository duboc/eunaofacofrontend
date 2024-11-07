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