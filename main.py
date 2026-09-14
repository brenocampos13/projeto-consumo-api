from etl.extract_api import get_dados
from etl.load_database import load_database, ver_ceps, truncate
from etl.etl_json_db import pipeline_raw_dim_json

def main():

    print("Iniciando consumo de API...")

    dados = get_dados()

    print("Dados adquiridos.")
    print("Iniciando carga...")

    load_database(dados)

    print("Carga finalizada no banco.")
    print("Iniciando ETL raw para dim...")

    pipeline_raw_dim_json()

    print("ETL Finalizado!")

if __name__ == "__main__":
    main()