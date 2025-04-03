import json
import os
from typing import List, Dict, Any

def get_file_path(filename: str) -> str:
    """Retorna o caminho absoluto do arquivo, relativo ao diretório deste script."""
    diretorio_atual = os.path.dirname(__file__)
    return os.path.join(diretorio_atual, filename)

def write_data_to_json(file_path: str, data: List[Dict[str, Any]]) -> None:
    """Escreve a lista de dicionários no arquivo JSON especificado."""
    try:
        with open(file_path, "w", encoding="utf-8") as arquivo:
            json.dump(data, arquivo, indent=4, ensure_ascii=False)
        print(f"Novos dados foram adicionados ao arquivo '{file_path}' com sucesso!")
    except Exception as e:
        print(f"Erro ao gravar os dados: {e}")

def read_data_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Lê e retorna os dados do arquivo JSON. Em caso de erro, retorna uma lista vazia."""
    try:
        with open(file_path, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{file_path}' está corrompido ou não é um JSON válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    return []

def main() -> None:
    arquivo_json = get_file_path("dados_pessoais.json")

    # Dados a serem armazenados
    dados = [
    {"Nome": "Ana", "Idade": 30, "Cidade": "Fortaleza"},
    {"Nome": "Bruno", "Idade": 27, "Cidade": "Recife"},
    {"Nome": "Carla", "Idade": 45, "Cidade": "Porto Alegre"},
    {"Nome": "Daniel", "Idade": 32, "Cidade": "Curitiba"},
    {"Nome": "Eduardo", "Idade": 38, "Cidade": "São Paulo"},
    {"Nome": "Fernanda", "Idade": 25, "Cidade": "Florianópolis"},
    {"Nome": "Gabriel", "Idade": 29, "Cidade": "Belo Horizonte"},
    {"Nome": "Helena", "Idade": 22, "Cidade": "Manaus"},
    {"Nome": "Igor", "Idade": 33, "Cidade": "Salvador"},
    {"Nome": "Juliana", "Idade": 28, "Cidade": "Rio de Janeiro"}
]


    # Escrita dos dados no arquivo JSON
    write_data_to_json(arquivo_json, dados)

    # Leitura e exibição dos dados
    dados_lidos = read_data_from_json(arquivo_json)
    if dados_lidos:
        print("Dados lidos do arquivo JSON:")
        for pessoa in dados_lidos:
            print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Cidade: {pessoa['Cidade']}")

if __name__ == "__main__":
    main()
