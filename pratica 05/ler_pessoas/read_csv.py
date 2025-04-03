import pandas as pd

arquivo_csv ="pratica 05\ler_pessoas\dados.csv"

try:
    frame = pd.read_csv(arquivo_csv)
    print("Dados do arquivo: ")
    print(frame)
except pd.errors.ParserError as e:
    print(f"Erro de análise do arquivo CSV: {e}")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
else:
    print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")