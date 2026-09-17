from config import get_connection
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
                api_projeto.raw_api
            ;
        """
    )

    dados = cursor.fetchall()

    cursor.close()

    conn.close()

    return dados

def get_sheet():

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    credentials = Credentials.from_service_account_file(
        "credentials.json",
        scopes=scopes
    )

    client = gspread.authorize(credentials)

    spreadsheet = client.open("PROJETO API")

    worksheet = spreadsheet.worksheet("dim_cep")

    return worksheet

def load_sheet():
    sheet = get_sheet()

    sheet.update(
        "A1",
        [
            ["cep", "cidade"],
            ["14055-494", "Ribeirão Preto"],
            ["14060-556", "Ribeirão Preto"]
        ]
    )

load_sheet()