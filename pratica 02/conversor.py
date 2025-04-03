def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Dicionário que mapeia as conversões com base nas unidades de origem e destino
conversoes = {
    ("C", "F"): celsius_to_fahrenheit,
    ("C", "K"): celsius_to_kelvin,
    ("F", "C"): fahrenheit_to_celsius,
    ("F", "K"): fahrenheit_to_kelvin,
    ("K", "C"): kelvin_to_celsius,
    ("K", "F"): kelvin_to_fahrenheit
}

def converter_temperatura(temp, origem, destino):
    if origem == destino:
        return temp
    else:
        # Obter a função apropriada do dicionário e aplicar a temperatura
        converter_func = conversoes.get((origem, destino))
        return converter_func(temp)

# Interface do usuário
temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ")
destino = input("Digite a unidade de destino (C, F ou K): ")

resultado = converter_temperatura(temp, origem, destino)
print(f"A temperatura convertida é: {resultado:.2f} {destino}")
