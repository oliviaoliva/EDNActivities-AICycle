def analise_numero():
    pares = 0
    impares = 0
    
    def contar_numeros(numero):
        nonlocal pares, impares
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    
    while True:
        entrada = input("Digite um número inteiro ou 'fim' para sair: ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            contar_numeros(numero)
        except ValueError:
            print("Erro! Por favor, digite um número inteiro válido.")
            continue
    
    print("Resultado final:")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

analise_numero()
