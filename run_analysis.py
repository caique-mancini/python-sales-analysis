#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '.')

from src.generate_data import generate_sales_dataset
from src.cleaning import clean_sales_data
from src.analysis import calculate_kpis, sales_by_month, top_products
from src.visuals import plot_sales_over_time, plot_top_products
import pandas as pd

print("=" * 50)
print("ANÁLISE COMPLETA DE VENDAS")
print("=" * 50)

# 1. Gerar dados
print("\n[1] Gerando dataset...")
df_raw = generate_sales_dataset(n_rows=3000, output_path='data/raw/sales_raw.csv')
print(f"   Shape: {df_raw.shape}")

# 2. Limpar dados
print("\n[2] Limpando dados...")
df_clean = clean_sales_data(df_raw, output_path='data/processed/sales_clean.csv')
print(f"   Dados originais: {df_raw.shape}")
print(f"   Dados limpos: {df_clean.shape}")
print(f"   Linhas removidas: {len(df_raw) - len(df_clean)}")

# 3. Calcular KPIs
print("\n[3] Calculando KPIs...")
kpis = calculate_kpis(df_clean)
print(kpis.to_string(index=False))

# 4. Vendas por mês
print("\n[4] Vendas por mês...")
monthly = sales_by_month(df_clean)
print(monthly.to_string(index=False))

# 5. Top produtos
print("\n[5] Top 5 produtos...")
top5 = top_products(df_clean, n=5)
print(top5.to_string(index=False))

# 6. Gerar gráficos
print("\n[6] Gerando gráficos...")
plot_sales_over_time(df_clean, output_path='outputs/figures/sales_by_month.png')
plot_top_products(df_clean, n=8, output_path='outputs/figures/top_products.png')

print("\n" + "=" * 50)
print("✓ ANÁLISE CONCLUÍDA COM SUCESSO!")
print("=" * 50)
print("\nArquivos gerados:")
print("  - data/raw/sales_raw.csv")
print("  - data/processed/sales_clean.csv")
print("  - outputs/figures/sales_by_month.png")
print("  - outputs/figures/top_products.png")
