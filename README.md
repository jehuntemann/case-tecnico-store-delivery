# Case Tecnico Store Delivery
- Este projeto, desenvolvido em Python, tem como objetivo processar um arquivo de entrada fornecido como parâmetro, realizar a higienização dos dados e armazená-los em um banco de dados PostgreSQL.

## Dependências
- Docker

## Como usar

#### 1 - Subir o banco de dados Postgres
- `docker compose up --build db`

#### 2 - Construir o container da aplicação
- `docker compose build service`

#### 3 - Executar o projeto passando o arquivo como parâmetro
- `docker compose run --rm -v "<caminho_completo_do_arquivo>:/input_file" service python main.py /input_file`


## Executar testes unitários
- `docker compose run --rm service pytest -v --cov=.`

## Executar Code Convention
- `docker compose run --rm service flake8`
- `docker compose run --rm service pycodestyle`

