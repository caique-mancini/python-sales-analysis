# Guia de Execução do Projeto Sales Analysis

## Passo 1: Abra o PowerShell

No VS Code, clique em `Terminal` > `New Terminal` ou pressione `Ctrl + `

## Passo 2: Crie o ambiente virtual (primeira vez)

```powershell
python -m venv .venv
```

## Passo 3: Ative o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Se receber erro de permissão, execute primeiro:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Depois ative novamente:
```powershell
.\.venv\Scripts\Activate.ps1
```

Quando ativado corretamente, voce verá `(.venv)` no inicio do terminal.

## Passo 4: Instale as dependências

```powershell
py -m pip install -r requirements.txt
```

## Passo 5: Execute o projeto

```powershell
python src/main.py
```

## Arquivos gerados

Após a execução, você terá:

- **data/raw/sales_raw.csv** - Dataset bruto com 3000 registros
- **data/processed/sales_clean.csv** - Dados limpos e processados
- **outputs/report.xlsx** - Relatório em Excel com KPIs, vendas por mês e top 10 produtos
- **outputs/figures/sales_by_month.png** - Gráfico de vendas ao longo do tempo
- **outputs/figures/top_products.png** - Gráfico dos 10 produtos mais vendidos

## O que o projeto faz

1. **Gera dados**: Cria um dataset fictício de vendas
2. **Limpa dados**: Remove duplicatas e valores inválidos
3. **Calcula KPIs**: Computa métricas importantes de vendas
4. **Cria gráficos**: Visualiza tendências e produtos top
5. **Exporta relatório**: Salva tudo em um arquivo Excel

## Troubleshooting

### Erro: "cannot be loaded because running scripts is disabled"
Execute: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

### Erro: "pip: command not found"
Use: `py -m pip` em vez de `pip`

### Erro: "No module named 'pandas'"
Execute: `py -m pip install -r requirements.txt`

Aproveite o projeto!
