# Sistema simples de contas bancárias (Python + SQLite)

Esse projeto é um sistema básico que eu desenvolvi para praticar integração entre Python e banco de dados usando SQLite.

A ideia aqui foi simular um cadastro de contas bancárias, com informações como titular, saldo e CPF.

## O que eu pratiquei nesse projeto

- Criação de banco de dados com SQLite
- Criação de tabela com restrições (PRIMARY KEY, UNIQUE, NOT NULL)
- Inserção de dados no banco
- Consulta de dados com SELECT
- Integração do Python com banco usando sqlite3

## Tecnologias utilizadas

- Python 3
- SQLite (nativo do Python)

## Estrutura do banco

Tabela: `contas_bancarias`

| Campo   | Tipo    | Descrição               |
|--------|--------|------------------------|
| id     | INTEGER | Identificador único    |
| titular| TEXT    | Nome do titular        |
| saldo  | FLOAT   | Saldo da conta         |
| cpf    | TEXT    | CPF único              |
