# Guia Completo: Publicar seu Projeto no GitHub

## 1. Subir para GitHub (Primeiros Passos)

### 1.1 Criar Repositório no GitHub

1. Abra https://github.com e faça login
2. Clique em **"+"** > **"New repository"**
3. Preencha:
   - Repository name: `python-sales-analysis`
   - Description: `Analise de dados de vendas com Python - Dataset, limpeza, KPIs, graficos e relatorio Excel`
   - Visibility: **Public** (para que todos vejam)
   - **NÃO** inicialize com README, .gitignore ou license

4. Clique **"Create repository"**

### 1.2 Fazer Push via PowerShell

```powershell
# Abra PowerShell na pasta do projeto
cd "c:\Users\caiqu\OneDrive\Área de Trabalho\python-sales-analysis"

# Configure seu Git (primeira vez)
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@gmail.com"

# Inicialize o repositório
git init

# Adicione todos os arquivos
git add .

# Faça o primeiro commit
git commit -m "Initial commit: Sales Analysis project"

# Adicione o repositório remoto (copie do GitHub)
git remote add origin https://github.com/SEU_USUARIO/python-sales-analysis.git

# Envie para o GitHub
git branch -M main
git push -u origin main
```

### 1.3 Comandos Git Futuros

Depois de fazer alterações:

```powershell
git add .
git commit -m "Descricao da mudanca"
git push
```

---

## 2. Compartilhar Análises com Usuários Comuns

### OPÇÃO A: Jupyter Notebook no GitHub (RECOMENDADO)

O GitHub renderiza automaticamente notebooks `.ipynb`!

**Arquivo criado:** `analise_completa.ipynb`

Usuários comuns podem:
- Ver os gráficos e tabelas diretamente no GitHub (não precisa instalar nada)
- Clicar em **"Raw"** para baixar
- Executar no Google Colab (grátis, sem instalar Python)

**Como usar no Google Colab:**
1. Vá para https://colab.research.google.com
2. Abra "File" > "Upload notebook"
3. Selecione `analise_completa.ipynb`
4. Clique em "Runtime" > "Run all"

---

### OPÇÃO B: Publicar no Notion (Como você mencionou usar)

1. Abra seu Notion
2. Crie uma página "Sales Analysis"
3. Use "Database" > "Database from CSV" e importe:
   - `outputs/report.xlsx`
   - `data/processed/sales_clean.csv`
4. Arraste as imagens dos gráficos:
   - `outputs/figures/sales_by_month.png`
   - `outputs/figures/top_products.png`
5. Clique em "Share" e envie o link público

---

### OPÇÃO C: Dashboard Interativo com Streamlit (MAIS LEGAL!)

Vou criar um app Streamlit que qualquer pessoa pode acessar via web:

