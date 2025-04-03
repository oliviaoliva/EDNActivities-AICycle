def palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

def main():
    frase = input("Digite sua palavra ou frase aqui: ")
    if palindromo(frase):
        resposta = "Sim"
    else:
        resposta = "Não"
        
    print(f"'{frase}' é considerado um palíndromo? {resposta}")

if __name__ == "__main__":
    main()
