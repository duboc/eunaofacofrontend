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