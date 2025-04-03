def validar_senha(senha):
    """Valida a senha fornecida segundo critérios específicos."""
    erros = []
    if len(senha) < 8:
        erros.append("deve ter no mínimo 8 caracteres")
    if not any(caractere.isdigit() for caractere in senha):
        erros.append("deve conter pelo menos um número")
    if not any(caractere.isalpha() for caractere in senha):
        erros.append("deve conter pelo menos uma letra")

    return erros

def verifica_senha():
    while True:
        senha = input("Digite uma senha (ou digite 'SAIR' para encerrar): ")
        if senha.upper() == "SAIR":
            print("Programa encerrado")
            break
        
        erros = validar_senha(senha)
        if erros:
            print(f"Senha fraca: {', '.join(erros)}.")
        else:
            print("Senha forte e válida!")
            break

if __name__ == "__main__":
    verifica_senha()
