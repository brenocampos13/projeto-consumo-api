CREATE SCHEMA IF NOT EXISTS api_projeto;

CREATE TABLE IF NOT EXISTS api_projeto.raw_api(
    id SERIAL PRIMARY KEY,
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    endpoint VARCHAR(100),
    payload JSONB
);