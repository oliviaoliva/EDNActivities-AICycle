def regitro_notas():
    notas = []
    while True:
        try:
            entrada = input("Digite a nota do aluno ou 'fim' para sair: ")
            if entrada.lower() == "fim":
                break
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
                continue
        except ValueError:
            print("Entrada inválida. Digite uma nota valida ou fim para sair.")

    if notas:
            media = sum(notas) / len(notas)
            print(f"Média da turma: {media:.2f}")
            print(f"Total de notas válidas registradas: {len(notas)}")
    else:
            print("Nenhuma nota registrada.")
regitro_notas()
