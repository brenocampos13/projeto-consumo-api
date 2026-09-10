CREATE SCHEMA IF NOT EXISTS api_projeto;

CREATE TABLE IF NOT EXISTS api_projeto.raw(
    cep integer,
    logradouro VARCHAR(50),
    complemento VARCHAR(50),
    unidade VARCHAR(30),
    localidade VARCHAR(30),
    uf VARCHAR(5),
    estado VARCHAR(30),
    regiao VARCHAR(40),
    ibge integer,
    gia integer,
    ddd integer,
    siafi integer
);