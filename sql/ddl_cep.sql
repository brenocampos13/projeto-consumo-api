CREATE SCHEMA IF NOT EXISTS api_projeto;

CREATE TABLE IF NOT EXISTS api_projeto.raw_api(
    id SERIAL PRIMARY KEY,
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    endpoint VARCHAR(100),
    payload JSONB
);

CREATE TABLE IF NOT EXISTS api_projeto.dim_cep (
    uf VARCHAR(10),
    cep VARCHAR(10),
    ddd VARCHAR(10),
    gia VARCHAR(10),
    ibge VARCHAR(10),
    siafi VARCHAR(10),
    bairro VARCHAR(255),
    estado VARCHAR(20),
    regiao VARCHAR(50),
    unidade VARCHAR(50),
    localidade VARCHAR(255),
    logradouro VARCHAR(255),
    complemento VARCHAR(255)
);