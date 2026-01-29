import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_sales_dataset(n_rows=3000, output_path='data/raw/sales_raw.csv'):
    """
    Gera um dataset fictício de vendas
    """
    np.random.seed(42)
    
    # Gerar datas aleatórias nos últimos 365 dias
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = [start_date + timedelta(days=int(x)) for x in np.random.randint(0, 365, n_rows)]
    
    # Produtos disponíveis
    products = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Webcam', 'Headset', 'SSD', 'RAM']
    
    # Criar dataset
    data = {
        'date': dates,
        'product': np.random.choice(products, n_rows),
        'quantity': np.random.randint(1, 10, n_rows),
        'price': np.random.uniform(50, 2000, n_rows),
        'customer_id': np.random.randint(1000, 5000, n_rows),
    }
    
    df = pd.DataFrame(data)
    df['sales'] = df['quantity'] * df['price']
    df['date'] = pd.to_datetime(df['date'])
    
    # Salvar arquivo
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"✓ Dataset gerado: {output_path}")
    return df
