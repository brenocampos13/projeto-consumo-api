from config import get_connection

def extract_raw_db():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT payload
        FROM api_projeto.raw_api
        """

    )

    dados = cursor.fetchall()

    print(dados)

    return dados

def transform_json_db(dados):

    linhas = []

    for registro in dados:
        payload = registro[0]

        linhas.append(
            (
            payload.get("uf"),
            payload.get("cep"),
            payload.get("ddd"),
            payload.get("gia"),
            payload.get("ibge"),
            payload.get("siafi"),
            payload.get("bairro"),
            payload.get("estado"),
            payload.get("regiao"),
            payload.get("unidade"),
            payload.get("localidade"),
            payload.get("logradouro"),
            payload.get("complemento")
            )
        )
    for e in linhas:
        print(e)

    return linhas

def load_json_db(dados):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
        INSERT INTO api_projeto.dim_cep(
            uf,
            cep,
            ddd,
            gia,
            ibge,
            siafi,
            bairro,
            estado,
            regiao,
            unidade,
            localidade,
            logradouro,
            complemento
        ) VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """

    cursor.executemany(sql, dados)

    conn.commit()

    cursor.close()

    conn.close()

def pipeline_raw_dim_json():

    dados = extract_raw_db()

    registros = transform_json_db(dados)

    load_json_db(registros)