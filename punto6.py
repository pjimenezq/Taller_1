vocales = ['a', 'e', 'i', 'o', 'u']
consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

letra = input("Ingrese una letra: ")

if letra in vocales:
    print("Es una vocal.")
elif letra in consonantes:
    print("Es una consonante.")
else:
    print("No es ni vocal ni consonante.")
