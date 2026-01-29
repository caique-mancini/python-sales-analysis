import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_sales_over_time(df, output_path='outputs/figures/sales_by_month.png'):
    """
    Cria gráfico de vendas ao longo do tempo
    """
    df['month'] = pd.to_datetime(df['date']).dt.to_period('M')
    monthly = df.groupby('month')['sales'].sum()
    
    plt.figure(figsize=(12, 6))
    monthly.plot(kind='line', marker='o')
    plt.title('Vendas ao Longo do Tempo')
    plt.xlabel('Mês')
    plt.ylabel('Vendas (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    print(f"✓ Gráfico salvo em: {output_path}")

def plot_top_products(df, n=8, output_path='outputs/figures/top_products.png'):
    """
    Cria gráfico dos top N produtos
    """
    top = df.groupby('product')['sales'].sum().sort_values(ascending=False).head(n)
    
    plt.figure(figsize=(12, 6))
    top.plot(kind='barh')
    plt.title(f'Top {n} Produtos por Vendas')
    plt.xlabel('Vendas (R$)')
    plt.ylabel('Produto')
    plt.tight_layout()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    print(f"✓ Gráfico salvo em: {output_path}")
