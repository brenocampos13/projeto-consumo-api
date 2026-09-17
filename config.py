import psycopg2
import os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials


load_dotenv("variaveis.env")

def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_DATABASE")
    )

    return conn

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