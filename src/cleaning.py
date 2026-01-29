import pandas as pd
import os

def clean_sales_data(df, output_path='data/processed/sales_clean.csv'):
    """
    Limpa dados de vendas removendo duplicatas e valores nulos
    """
    df = df.copy()
    
    # Remover duplicatas
    df = df.drop_duplicates()
    
    # Remover valores nulos
    df = df.dropna()
    
    # Remover vendas com valor negativo ou zero
    df = df[df['sales'] > 0]
    
    # Remover quantidade negativa ou zero
    df = df[df['quantity'] > 0]
    
    # Salvar arquivo
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"✓ Dados limpos salvos em: {output_path}")
    return df
