def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

def obter_valor(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor >= 0:
                return valor
            else:
                print("Por favor, digite um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

total_conta = obter_valor("Digite o valor da conta: R$ ")
porcentagem = obter_valor("Digite a porcentagem da gorjeta: ")
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para a conta que ficou em R$ {total_conta:.2f}, a gorjeta de {porcentagem}% é de R$ {gorjeta:.2f}")
