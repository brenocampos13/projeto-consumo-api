from etl.extract_api import get_dados
from etl.load_database import load_database

def main():
    print("Extraindo dados...")
    dados = get_dados("14060556")
    print("Extraído com sucesso!")
    print("Preparando carga...")
    load_database(dados)
    print("Carregado com sucesso!")

if __name__ == "__main__":
    main()