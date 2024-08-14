# Case Tecnico Store Delivery
- Este projeto, desenvolvido em Python, tem como objetivo processar um arquivo de entrada fornecido como parâmetro, realizar a higienização dos dados e armazená-los em um banco de dados PostgreSQL.

# Dependências
- Docker

# Como usar

## Subir o banco de dados Postgres
- `docker compose up --build db`

## Construir o container da aplicação
- `docker compose build service`

## Executar o projeto passando o arquivo como parâmetro
- `docker compose run --rm -v "<caminho_completo_do_arquivo>:/input_file" service python main.py /input_file`