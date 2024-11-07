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