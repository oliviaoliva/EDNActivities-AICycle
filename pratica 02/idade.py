def obter_idade(prompt):
    while True:
        try:
            idade = int(input(prompt))
            if idade < 0:
                print("Por favor, digite uma idade válida (não pode ser negativa).")
            else:
                return idade
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def categorizar_idade(idade):
    if idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    elif idade <= 120:
        return "Idoso"
    else:
        return "Múmia ou Imortal!"

idade = obter_idade("Digite uma idade: ")
categoria = categorizar_idade(idade)
print(categoria)
