Documentação do Projeto – Resumo de Vendas
1. Visão Geral
Este projeto utiliza FastAPI e SQLite para consultar vendas e exibir:

Produto mais vendido na última semana do mês escolhido.

Top 5 produtos do mês escolhido.

O frontend é renderizado utilizando templates Jinja2.

2. Estrutura do Projeto
A estrutura recomendada do projeto é:

bash
Copy
sales_insights_api_gpt/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── queries.py
│   ├── rag_handler.py
│   └── templates/
│       ├── selecionar_mes.html
│       └── resumo_dinamico.html
│
├── venv/
├── requirements.txt
└── test(1).db  (banco SQLite gerado)
3. Banco de Dados
O banco SQLite é armazenado em:

bash
Copy
C:\Users\User\Python_Projects\Projeto_SQLite\test(1).db
Criação do Banco
Execute o script criar_banco.py para gerar o banco com dados de teste:

bash
Copy
python criar_banco.py
Ele criará as tabelas:

products

customers

sales

E populá-las com dados fornecidos.

4. Código Principal
O arquivo main.py contém as rotas principais:

Rota inicial: / – mostra a página para selecionar mês e ano.

Rota de resumo: /resumo-vendas?mes=2&ano=2025 – exibe os dados do mês/ano informado.

5. Templates
selecionar_mes.html: formulário para escolha de mês e ano.

resumo_dinamico.html: exibe o produto mais vendido e o top 5 do mês.

6. Instalação de Dependências
Crie e ative o ambiente virtual:

bash
Copy
python -m venv venv
venv\Scripts\activate
Instale os pacotes do projeto:

bash
Copy
pip install -r requirements.txt
7. Arquivo requirements.txt
O arquivo requirements.txt deve conter:

makefile
Copy
fastapi==0.116.1
uvicorn==0.35.0
jinja2
sqlalchemy==2.0.41
pydantic==2.11.7
python-dotenv==1.1.1
requests==2.32.4
8. Executando o Servidor
Na raiz do projeto:

bash
Copy
uvicorn app.main:app --reload
Você verá:

nginx
Copy
Uvicorn running on http://127.0.0.1:8000
Acesse no navegador:

cpp
Copy
http://127.0.0.1:8000/
9. Testando
Na página inicial, informe Mês=2 e Ano=2025.

Clique em "Ver Resumo".

A API mostrará:

O produto mais vendido entre os últimos 7 dias do mês.

O Top 5 produtos do mês escolhido.

10. Debug Comum
Internal Server Error → Verifique se:

O template resumo_dinamico.html está correto.

O banco test(1).db existe no caminho definido no database.py.

enumerate undefined → Foi corrigido, use loop.index no Jinja2.


