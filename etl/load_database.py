from config import get_connection

def load_database():
    cursor = get_connection()

    cursor.execute(
        """
            SELECT
                *
            FROM
                api_projeto.raw
            ;
        """
    )

    retorno_db = cursor.fetchall()

    print(retorno_db)

if __name__ == "__main__":
    load_database()