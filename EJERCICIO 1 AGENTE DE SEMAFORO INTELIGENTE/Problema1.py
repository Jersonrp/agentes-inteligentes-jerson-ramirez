import time
import random

def cambiar_semaforo(trafico):
    if trafico > 10:
        verde = 10
        amarillo = 3
        rojo = 12
    elif 5 <= trafico <= 10:
        verde = 7
        amarillo = 3
        rojo = 9
    else:
        verde = 5
        amarillo = 2
        rojo = 6
    
    print("Semáforo en VERDE - Tiempo:", verde, "segundos")
    time.sleep(verde)
    
    print("Semáforo en AMARILLO - Tiempo:", amarillo, "segundos")
    time.sleep(amarillo)
    
    print("Semáforo en ROJO - Tiempo:", rojo, "segundos")
    time.sleep(rojo)

while True:
    trafico_encontrado  = random.randint(0, 20)  # Deteccion de vehiclos 
    print("Vehículos detectados:", trafico_encontrado)
    cambiar_semaforo(trafico_encontrado)
