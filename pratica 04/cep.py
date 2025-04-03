import requests

def consulta_cep(cep: str) -> str:
    """
    Consulta o CEP usando a API ViaCEP e retorna uma string formatada com os dados do endereço.
    """
    cep = cep.strip()  # Remove espaços extras
    if not cep.isdigit() or len(cep) != 8:
        return "CEP inválido. Certifique-se de digitar 8 dígitos numéricos."
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("erro"):
            return "CEP não encontrado."
        
        # Monta a resposta utilizando os valores retornados, com valores padrão se não encontrados
        result = (
            f"CEP: {data.get('cep', 'N/A')}\n"
            f"LOGRADOURO: {data.get('logradouro', 'N/A')}\n"
            f"BAIRRO: {data.get('bairro', 'N/A')}\n"
            f"CIDADE: {data.get('localidade', 'N/A')}\n"
            f"ESTADO: {data.get('uf', 'N/A')}"
        )
        return result
    except requests.RequestException as e:
        return f"Erro na consulta: {e}"
    except ValueError:
        return "Erro ao processar a resposta do servidor."

def main():
    cep = input("Digite um CEP válido (somente números, 8 dígitos): ")
    print("Consultando CEP ...")
    resultado = consulta_cep(cep)
    print(resultado)

if __name__ == "__main__":
    main()
