# Taller 1

### Nombre del grupo:
# Agrocode industry

Integrantes:
* Paula Jiménez Quiñones
* Mario Alejandro Martinez
* David Rodriguez Rueda

## Primer punto


## Segundo punto
Realice un programa que lea tres números reales y determine cuál es el mayor.

**Diagrama de flujo**
```mermaid
flowchart TD;
    A(inicio) -->B[primer número real];
    A-->C[segundo número real];
    A-->D[tercer número real];
    B-->E{El primer número real es mayor que el segundo y el tercero?};
    C-->E;
    D-->E;
    E--Sí-->F[El primer número real es el mayor.]-->J(Fin);
    E--No-->G{El segundo número real es mayor que el tercero?};
    G--Sí-->H[El segundo número real es el mayor.]-->J;
    G--No-->I[El tercer número real es el mayor]-->J;
```
## Tercer punto


## Cuarto punto

### Problema planteado:
Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.

### La solución del problema es la siguiente:
1. Lo primero que se hizo fue declarar las variables como números flotantes.
2. Seguido a esto inicializamos las variables que van a ser número ingresados por las personas que estén utilizando el programa.
3. Después condicionamos de la siguiente forma
   * Si x % y == 0 entonces, x es multiplo de y.
   * Sino entonces x no es multiplo de y.

Y de esta manera fue solucionado el problema incialmente planteado.

##### El código del rpoblema es el siguiente:
```
#declaramos variables
x : float
y : float
#inicializamos variables
print("Comprobaremos si x es multiplo de y")
x = float(input("Introduzca un valor para x: "))
y = float(input("Introduzca un valor para y: "))
#condicionamos
if x % y == 0:
    print(x, "es multiplo de", y)
else:
    print(x, "no es multiplo", y)
```

##### El diagrama de flujo representando la solución del problema es el siguiente:
```mermaid
graph TD;
Inicio(Inicio)--->Variable1
Inicio(Inicio)--->Variable2
Variable1[x : float]--->Inicializacion1
Variable2[y: float]--->Inicializacion2
Inicializacion1[Introduzca un valor para x]--->Operacion
Inicializacion2[Introduzca un valor para y]--->Operacion
Operacion{x % y == 0?}-- Sí -->Decir1
Operacion{x % y == 0?}-- No -->Decir2
Decir1[x es multiplo de y]--->Fin
Decir2[x no es multiplo de y]--->Fin
Fin(Fin)
```

## Quinto punto


## Sexto punto


## Séptimo punto


## Octavo punto

### Problema planteado:
Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.

### Solución del problema:
##### Contexto previo a la solución del problema: Tener en cuenta que la solución 

## Noveno punto


## Décimo punto


