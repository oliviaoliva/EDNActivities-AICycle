import requests

def usuario_aleatorio() -> str:
    """
    Consulta a API randomuser.me para obter informações de um usuário aleatório 
    e retorna uma string formatada com o nome, email e país do usuário.

    Returns:
        str: Dados formatados do usuário ou mensagem de erro.
    """
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        if not results:
            return "Nenhum resultado encontrado."
        
        user = results[0]
        name_data = user.get("name", {})
        first_name = name_data.get("first", "N/A")
        last_name = name_data.get("last", "N/A")
        full_name = f"{first_name} {last_name}"
        email = user.get("email", "N/A")
        location = user.get("location", {})
        country = location.get("country", "N/A")
        
        return (
            f"Nome: {full_name}\n"
            f"Email: {email}\n"
            f"País: {country}"
        )
    except requests.RequestException as e:
        return f"Erro na requisição: {e}"
    except (ValueError, KeyError) as e:
        return f"Erro ao processar os dados: {e}"

def main() -> None:
    """Função principal que exibe informações de um usuário aleatório."""
    print("Criando usuário aleatório...")
    usuario_info = usuario_aleatorio()
    print(usuario_info)

if __name__ == "__main__":
    main()
