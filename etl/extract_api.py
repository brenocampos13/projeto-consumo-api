import requests

URL_BASE = "https://viacep.com.br/ws/"

def get_dados():
    carga = []

    ceps = [
        '14060556',
        '14055494',
        '14025380',
        '15610218',
        '14060556',
        '14055494',
        '14025380',
        '15610218',
        '14060556',
        '14055494',
        '14025380',
        '15610218'
    ]

    for cep in ceps:

        url = URL_BASE + cep + "/json"

        response = requests.get(url)

        dados = response.json()

        carga.append(dados)
    
    return carga