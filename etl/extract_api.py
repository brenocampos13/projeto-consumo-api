import requests

URL_BASE = "https://viacep.com.br/ws/"

def get_dados(cep):
    url = URL_BASE + cep + "/json"

    response = requests.get(url)

    dados = response.json()

    return dados
