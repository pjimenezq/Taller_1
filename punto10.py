distancia = float(input("Ingresa la distancia en metros: "))

velocidad_luz = 299792458  # metros por segundo
velocidad_sonido = 343  # metros por segundo
velocidad_carro = 455.28  # metros por segundo (supongamos)
velocidad_bolt = 11.6  # metros por segundo (supongamos)

# Calcula los tiempos en segundos
tiempo_luz_segundos = distancia / velocidad_luz
tiempo_sonido_segundos = distancia / velocidad_sonido
tiempo_carro_segundos = distancia / velocidad_carro
tiempo_bolt_segundos = distancia / velocidad_bolt

# Convierte los tiempos en minutos
tiempo_minutos_luz = tiempo_luz_segundos / 60
tiempo_minutos_sonido = tiempo_sonido_segundos / 60
tiempo_minutos_carro = tiempo_carro_segundos / 60
tiempo_minutos_bolt = tiempo_bolt_segundos / 60

print()
print(f"El tiempo que le tomaría a la luz recorrer {distancia} metros es aproximadamente {tiempo_luz_segundos:.2f} segundos y {tiempo_minutos_luz:.2f} minutos.")
print()
print(f"El tiempo que le tomaría al sonido recorrer {distancia} metros es aproximadamente {tiempo_sonido_segundos:.2f} segundos y {tiempo_minutos_sonido:.2f} minutos.")
print()
print(f"El tiempo que le tomaría al vehículo más veloz recorrer {distancia} metros es aproximadamente {tiempo_carro_segundos:.2f} segundos y {tiempo_minutos_carro:.2f} minutos.")
print()
print(f"Usain Bolt recorrería {distancia} metros en aproximadamente {tiempo_bolt_segundos:.2f} segundos y {tiempo_minutos_bolt:.2f} minutos.")
