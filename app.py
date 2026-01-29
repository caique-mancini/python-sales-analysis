import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.generate_data import generate_sales_dataset
from src.cleaning import clean_sales_data
from src.analysis import calculate_kpis, sales_by_month, top_products

# Configurar pagina
st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="chart_with_upwards_trend",
    layout="wide"
)

st.title("Sales Analysis Dashboard")
st.markdown("Analise completa de dados de vendas - Dataset ficticio de 3000 registros")

# Sidebar
st.sidebar.title("Opcoes")
modo = st.sidebar.radio(
    "Escolha o que visualizar:",
    ["Resumo", "Dados Brutos", "Dados Limpos", "KPIs", "Vendas por Mes", "Top Produtos", "Sobre"]
)

# Carregar dados
@st.cache_data
def load_data():
    df_raw = generate_sales_dataset(n_rows=3000, output_path="data/raw/sales_raw.csv")
    df_clean = clean_sales_data(df_raw, output_path="data/processed/sales_clean.csv")
    return df_raw, df_clean

df_raw, df_clean = load_data()

# ==================== RESUMO ====================
if modo == "Resumo":
    st.header("Resumo Executivo")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Vendas", f"R$ {df_clean['sales'].sum():,.2f}")
    
    with col2:
        st.metric("Ticket Medio", f"R$ {df_clean['sales'].mean():,.2f}")
    
    with col3:
        st.metric("Transacoes", len(df_clean))
    
    with col4:
        st.metric("Produtos", df_clean['product'].nunique())
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Vendas por Mes")
        monthly = sales_by_month(df_clean)
        st.line_chart(monthly.set_index("Mes")["Total de Vendas"])
    
    with col2:
        st.subheader("Top 5 Produtos")
        top5 = top_products(df_clean, n=5)
        st.bar_chart(top5.set_index("Produto")["Total de Vendas"])

# ==================== DADOS BRUTOS ====================
elif modo == "Dados Brutos":
    st.header("Dados Brutos")
    st.write(f"Total de linhas: {len(df_raw)}")
    
    if st.checkbox("Mostrar primeiras 100 linhas"):
        st.dataframe(df_raw.head(100))
    
    if st.checkbox("Download CSV"):
        st.download_button(
            label="Baixar dados brutos",
            data=df_raw.to_csv(index=False),
            file_name="sales_raw.csv"
        )

# ==================== DADOS LIMPOS ====================
elif modo == "Dados Limpos":
    st.header("Dados Limpos")
    st.write(f"Total de linhas: {len(df_clean)}")
    st.write(f"Linhas removidas: {len(df_raw) - len(df_clean)}")
    
    if st.checkbox("Mostrar primeiras 100 linhas"):
        st.dataframe(df_clean.head(100))
    
    if st.checkbox("Download CSV"):
        st.download_button(
            label="Baixar dados limpos",
            data=df_clean.to_csv(index=False),
            file_name="sales_clean.csv"
        )

# ==================== KPIs ====================
elif modo == "KPIs":
    st.header("KPIs Principais")
    
    kpis = calculate_kpis(df_clean)
    
    for idx, row in kpis.iterrows():
        st.metric(row['Metrica'], row['Valor'])

# ==================== VENDAS POR MES ====================
elif modo == "Vendas por Mes":
    st.header("Vendas por Mes")
    
    monthly = sales_by_month(df_clean)
    
    # Grafico de linha
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(range(len(monthly)), monthly['Total de Vendas'], marker='o', linewidth=2, color='steelblue')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Vendas (R$)')
    ax.set_title('Tendencia de Vendas')
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    # Tabela
    st.subheader("Dados Detalhados")
    st.dataframe(monthly)

# ==================== TOP PRODUTOS ====================
elif modo == "Top Produtos":
    st.header("Produtos Mais Vendidos")
    
    n = st.slider("Quantos produtos mostrar?", 5, 20, 10)
    top = top_products(df_clean, n=n)
    
    # Grafico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(top['Produto'], top['Total de Vendas'], color='steelblue')
    ax.set_xlabel('Produto')
    ax.set_ylabel('Vendas (R$)')
    ax.set_title(f'Top {n} Produtos Mais Vendidos')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Tabela
    st.subheader("Dados Detalhados")
    st.dataframe(top)

# ==================== SOBRE ====================
elif modo == "Sobre":
    st.header("Sobre o Projeto")
    
    st.markdown("""
    ### Sales Analysis Dashboard
    
    Projeto de analise de dados desenvolvido em Python.
    
    **Tecnologias Utilizadas:**
    - Python 3.13
    - Pandas (manipulacao de dados)
    - Matplotlib (visualizacoes)
    - Streamlit (dashboard interativo)
    
    **Dataset:**
    - 3000 registros de vendas fictícios
    - Periodo: Jan 2023 - Dez 2024
    - 5 categorias de produtos
    - 5 regioes geograficas
    
    **Pipeline:**
    1. Geracao de dados
    2. Limpeza e validacao
    3. Analise e calculo de KPIs
    4. Visualizacao interativa
    
    **Autor:** Seu Nome
    **GitHub:** https://github.com/seu_usuario/python-sales-analysis
    """)

st.divider()
st.markdown("---")
st.markdown("Dashboard criado com Streamlit | [GitHub](https://github.com) | [Documentacao](https://docs.streamlit.io)")
