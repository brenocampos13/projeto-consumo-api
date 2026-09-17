from config import get_connection, get_sheet
import gspread
from google.oauth2.service_account import Credentials

def extract_dim_cep():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                *
            FROM
                api_projeto.dim_cep
            ;
        """
    )

    dados = cursor.fetchall()

    cursor.close()

    conn.close()

    print(dados)

    return dados

def transform_dim_cep(dados):

    lista = []

    for registro in dados:
        lista.append(list(registro))

    print(lista)

    return lista

def load_sheet(lista):

    cabecalho = [
        [
        "UF",
        "CEP",
        "DDD",
        "Gia",
        "IBGE",
        "Siafi",
        "Bairro",
        "Estado",
        "Regiao",
        "Unidade",
        "Localidade",
        "Logradouro",
        "Complemento"
        ]
    ]

    sheet = get_sheet()


    sheet.update(
        "A1",
        cabecalho + lista
    )

def pipeline_db_sheets():

    dados = extract_dim_cep()

    registros = transform_dim_cep(dados)

    load_sheet(registros)

if __name__ == "__main__":
    pipeline_db_sheets()