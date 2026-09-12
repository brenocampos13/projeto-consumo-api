from psycopg2.extras import Json
from config import get_connection

def load_database(dados):
    conn = get_connection()

    cursor = conn.cursor()

    sql = """
    INSERT INTO api_projeto.raw_api(
        endpoint,
        payload
    )
    VALUES (
        %s,
        %s
    )
    ;
    """

    valores = (
        "viacep",
        Json(dados)
    )

    cursor.execute(sql, valores)

    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_database()