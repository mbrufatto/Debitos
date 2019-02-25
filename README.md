# Debitos
Para este projeto foi utilizada a linguagem Python na versão 2.7, framework Flask, banco de dados sqlite e bootstrap.

# Instrução

Para rodar essa aplicação é necessário ter o ambiente de desenvolvimento Python em sua máquina. Após a instalação do ambiente siga os seguintes passos:

- Abrir o terminal;
- Acessar a pasta do projeto;
- Criar o virtual env;
- Digite o seguinte comando:

pip install -r requirements.txt

Este comando fará a instalação de todas as bibliotecas que foram utilizadas para este projeto.

- Digite os seguintes comandos:

python run.py db init
python run.py db migrate
python run.py db upgrade

Essa sequencia de comandos fará a criação do banco de dados e a construção das tabelas.

- Digite o seguinte comando:

python populate_users.py

Este comando busca os dados da api https://jsonplaceholder.typicode.com/users e cadastra os usuários na tabela clients.

- Digite o seguinte comando:

python run.py runserver

Esse comando rodará a aplicação, para ter acesso a aplicação acesse a url http://localhost:5000 em seu browser


# API

Com a aplicação rodando é possível acessar a API da aplicação através dos seguintes endpoints:

POST: http://localhost:5000/v1/debit/new 

exemplo de parametros:
{
  "client_id": "90",
  "description": "Não pagou o cartão de crédito",
  "client_name": "Lucas",
  "value": "6000",
  "date": "2019-04-23"
}


GET: http://localhost:5000/v1/debits

Retorna um json com todos os debitos.

GET: http://localhost:5000/v1/debit/2

Retorna um json com os dados de um determinado registro.

DELETE: http://localhost:5000/v1/debit/<id_do_debito que deseja deletar>

Deleta um determinado registro.

PUT: http://localhost:5000/v1/debit/<id_do_debito que deseja editarr>/edit

Edita um determinado registro.


# Melhorias
- Colocar mascara no campo de valor;
- Implementar testes.
- Implementar login na aplicação web;
- Implementar um sistema de token na API;s
