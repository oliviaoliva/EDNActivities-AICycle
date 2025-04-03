import requests
from datetime import datetime

def cotacao(moeda: str) -> str:
    """
    Obtém a cotação da moeda especificada em relação ao BRL utilizando a API AwesomeAPI.
    
    Parâmetros:
        moeda (str): Código da moeda (ex: USD, EUR, GBP)
    
    Retorna:
        str: Uma string formatada com os dados da cotação ou uma mensagem de erro.
    """
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave not in dados:
            return "Moeda não encontrada ou não suportada."
        
        cotacao = dados[chave]
        valor = float(cotacao.get('bid', 0))
        maximo = float(cotacao.get('high', 0))
        minima = float(cotacao.get('low', 0))
        timestamp = int(cotacao.get('timestamp', 0))
        data_hora = datetime.fromtimestamp(timestamp)
        
        resultado = (
            f"Moeda: {moeda} para BRL\n"
            f"Valor atual: R$ {valor:.4f}\n"
            f"Máxima do dia: R$ {maximo:.4f}\n"
            f"Mínima do dia: R$ {minima:.4f}\n"
            f"Data/Hora da cotação: {data_hora.strftime('%d/%m/%Y %H:%M:%S')}"
        )
        return resultado
    except requests.RequestException as e:
        return f"Erro ao obter cotação: {e}"
    except (ValueError, KeyError):
        return "Erro ao processar os dados da cotação."

def main():
    """Função principal para solicitar uma moeda ao usuário e exibir sua cotação."""
    moeda = input("Digite o código da moeda para cotação (ex: USD, EUR, GBP): ").upper().strip()
    print("\nObtendo cotação...")
    resultado = cotacao(moeda)
    print(resultado)

if __name__ == "__main__":
    main()
