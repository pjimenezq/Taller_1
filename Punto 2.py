print("Este programa lee tres número reales y determina cuál es el mayor") #Se explica cual es el propósito del programa
#Se declaran las variables; estableciendo sus nombres utilizando Camelcase y especificando que son de tipo float (dado a que el programa funciona con números reales)
numeroUno:float
numeroDos:float
numeroTres:float
#Se utiliza la función input(), para que el usuario pueda ingresar los datos al programa
numeroUno=float(input("Ingrese el primer número real: "))
numeroDos=float(input("Ingrese el segundo número real: "))
numeroTres=float(input("Ingrese el tercer número real: "))

if numeroUno>numeroDos and numeroUno>numeroTres:
        print("El número "+str(numeroUno) + " es el mayor.")#El primer número es el mayor cuando es más grande que el segundo y que el tercero
elif numeroDos>numeroTres:
        print("El número "+str(numeroDos), " es el mayor.")#Si el primer número no es mayor que el segundo y el segundo número es mayor que el tercero, el segundo número tiene que ser el mayor.
else:
        print("El número "+str(numeroTres), " es el mayor.")#Si el primer número y el segundo no son mayores que el tercero, el tercero tiene que ser el mayor.
