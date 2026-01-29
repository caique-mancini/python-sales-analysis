import pandas as pd

def calculate_kpis(df):
    """
    Calcula KPIs principais
    """
    kpis = pd.DataFrame({
        'Metrica': [
            'Total de Vendas',
            'Ticket Médio',
            'Transações',
            'Produtos Únicos',
            'Clientes Únicos',
            'Venda Máxima',
            'Venda Mínima'
        ],
        'Valor': [
            f"R$ {df['sales'].sum():,.2f}",
            f"R$ {df['sales'].mean():,.2f}",
            len(df),
            df['product'].nunique(),
            df['customer_id'].nunique(),
            f"R$ {df['sales'].max():,.2f}",
            f"R$ {df['sales'].min():,.2f}"
        ]
    })
    return kpis

def sales_by_month(df):
    """
    Agrupa vendas por mês
    """
    df['month'] = pd.to_datetime(df['date']).dt.to_period('M')
    monthly = df.groupby('month')['sales'].sum().reset_index()
    monthly.columns = ['Mes', 'Total de Vendas']
    monthly['Mes'] = monthly['Mes'].astype(str)
    return monthly

def top_products(df, n=5):
    """
    Retorna top N produtos por vendas
    """
    top = df.groupby('product')['sales'].sum().sort_values(ascending=False).head(n).reset_index()
    top.columns = ['Produto', 'Total de Vendas']
    return top
