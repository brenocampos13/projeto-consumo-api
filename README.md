# Projeto Consumo API

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de Engenharia de Dados através da construção de um pipeline completo de ingestão, transformação e disponibilização de dados.

A aplicação consome dados da API pública ViaCEP, armazena os registros brutos em uma camada RAW no PostgreSQL, realiza transformações para uma camada dimensional (DIM) e disponibiliza os dados estruturados em uma planilha do Google Sheets.

O projeto foi desenvolvido utilizando Python, PostgreSQL, Docker e Google Sheets API.

---

## Arquitetura

```text
ViaCEP API
    │
    ▼
Python (Requests)
    │
    ▼
PostgreSQL - RAW
(JSON Completo)
    │
    ▼
Transformação Python
    │
    ▼
PostgreSQL - DIM
(Dados Estruturados)
    │
    ▼
Google Sheets
```

---

## Tecnologias Utilizadas

- Python
- PostgreSQL
- Docker
- Docker Compose
- Requests
- Psycopg2
- Google Sheets API
- Google Cloud Service Account
- Gspread
- Python Dotenv

---

## Estrutura do Projeto

```text
Projeto Consumo API
│
├── etl
│   ├── extract_api.py
│   ├── load_database.py
│   ├── etl_json_db.py
│   └── etl_db_sheets.py
│
├── sql
│   └── ddl_cep.sql
│
├── config.py
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Fluxo do Pipeline

### 1. Extração

Os dados são consumidos da API ViaCEP utilizando a biblioteca Requests.

Exemplo:

```json
{
  "cep": "14060-556",
  "logradouro": "Rua Porto Seguro",
  "bairro": "Vila Albertina",
  "localidade": "Ribeirão Preto"
}
```

### 2. Camada RAW

Os dados são armazenados sem transformação em uma tabela RAW utilizando JSON.

Exemplo:

| id  | endpoint | payload         |
| --- | -------- | --------------- |
| 1   | viacep   | {json completo} |

**Objetivos da camada RAW:**

- Auditoria
- Reprocessamento
- Histórico da carga
- Preservação dos dados originais

### 3. Transformação

Os registros JSON são extraídos da camada RAW e convertidos para uma estrutura tabular.

Campos transformados:

- UF
- CEP
- DDD
- GIA
- IBGE
- SIAFI
- Bairro
- Estado
- Região
- Unidade
- Localidade
- Logradouro
- Complemento

### 4. Camada DIM

Os dados estruturados são armazenados em uma tabela dimensional para consumo.

Exemplo:

| UF  | CEP       | Bairro         | Localidade     |
| --- | --------- | -------------- | -------------- |
| SP  | 14060-556 | Vila Albertina | Ribeirão Preto |

### 5. Disponibilização

Os dados da camada DIM são enviados automaticamente para uma planilha do Google Sheets utilizando a Google Sheets API.

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/brenocampos13/projeto-consumo-api.git
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Criar um arquivo `.env`:

```env
DB_HOST=postgres
DB_USER=admin
DB_PASSWORD=1234
DB_DATABASE=api_projeto
DB_PORT=5432
```

### 4. Configurar credenciais Google

Adicionar o arquivo de credenciais da Service Account:

```text
credentials.json
```

A conta de serviço deve possuir acesso de **Editor** à planilha utilizada pelo projeto.

### 5. Executar com Docker

```bash
docker compose up -d
```

---

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Consumo de APIs REST
- Manipulação de JSON
- Estruturas de dados em Python (List, Tuple e Dict)
- ETL e ELT
- PostgreSQL
- Modelagem RAW e DIM
- Integração com Google Sheets
- Dockerização de aplicações
- Organização de pipelines de dados

---

## Próximos Passos

- Cargas incrementais
- Orquestração com Apache Airflow
- Transformações com dbt
- Armazenamento em nuvem (AWS)

---

## Autor

**Breno Campos Franco**

Projeto desenvolvido com foco em aprendizado prático de Engenharia de Dados, simulando um fluxo real de ingestão, transformação e disponibilização de dados.
