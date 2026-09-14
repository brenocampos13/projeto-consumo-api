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

    for dado in dados:

        cursor.execute(
            sql,
            (
                "viacep",
                Json(dado)
            )
        )


    conn.commit()

    cursor.close()
    
    conn.close()

def ver_ceps():

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM api_projeto.raw_api
    ;
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    cursor.close()

    conn.close()

    print(dados)

def truncate():

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
    TRUNCATE TABLE api_projeto.raw_api
    """

    cursor.execute(sql)

    cursor.close()

    conn.close()


if __name__ == "__main__":
    load_database()