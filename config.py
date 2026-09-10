import psycopg2
import os
from dotenv import load_dotenv


load_dotenv("variaveis.env")

def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_DATABASE")
    )

    cursor = conn.cursor()

    return cursor
