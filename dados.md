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