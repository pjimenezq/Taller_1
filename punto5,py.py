num1 = float (input("ingrese el primer numero: "))
num2 = float (input("ingrese el segundo numero: "))
num3 = float (input("ingrese el tercer numer: "))

suma = num1 + num2

if suma > num3:
   print ("la suma es mayor que el tercer numero")
elif suma < num3:
   print ("la suma es menor que el tercer numero")
elif suma == num3:
   print ("la suma es igual al tercer numero")