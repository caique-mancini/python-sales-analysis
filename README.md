# Sales Analysis (Python)

Projeto simples de portfólio em Python focado em Análise de Dados.

# Dashboard App

https://python-sales-analysis.streamlit.app/

Projeto simples de portfólio em Python focado em Análise de Dados.

## Objetivo
Gerar um dataset de vendas fictício, realizar limpeza, calcular KPIs e gerar visualizações + relatório em Excel.

## Tecnologias
- Python
- pandas
- numpy
- matplotlib
- openpyxl

## Como rodar

### 1) Criar e ativar ambiente virtual (Windows/PowerShell)

\\\powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
\\\`n
### 2) Instalar dependências

\\\powershell
py -m pip install -r requirements.txt
\\\`n
### 3) Executar o projeto

\\\powershell
python src/main.py
\\\`n
## Saída esperada
- data/raw/sales_raw.csv
- data/processed/sales_clean.csv
- outputs/figures/sales_by_month.png
- outputs/figures/top_products.png
- outputs/report.xlsx

