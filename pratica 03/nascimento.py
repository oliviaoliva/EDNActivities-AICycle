import datetime

def idade_em_dias(ano_nascimento):
    data_atual = datetime.datetime.now()
    data_nascimento = datetime.datetime(ano_nascimento, 1, 1)
    diferenca_dias = (data_atual - data_nascimento).days
    return diferenca_dias

ano_nascimento = int(input("Digite o ano de nascimento: "))
dias_vividos = idade_em_dias(ano_nascimento)  
print(f"Sua idade em dias é: {dias_vividos} dias")
