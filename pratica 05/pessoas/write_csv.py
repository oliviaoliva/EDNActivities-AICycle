import csv

arquivo_csv = "pessoas.csv"

dados = [
    ["Nome", "Idade", "Cidade"], 
    ["Olivia", 22, "João Pessoa"],
    ["Ricardo", 30, "São Paulo"],
    ["Cesar", 18, "Belo Horizonte"]
]
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print(f"Arquivo '{arquivo_csv}' criado com sucesso!")