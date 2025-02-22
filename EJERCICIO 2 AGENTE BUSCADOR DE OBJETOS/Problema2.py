import random
import time

def imprimir_cuadricula(agente, objeto):
    for i in range(5):
        for j in range(5):
            if (i, j) == agente:
                print(" A ", end="")  
            elif (i, j) == objeto:
                print(" X ", end="")  
            else:
                print(" . ", end="")  
        print()
    print("-" * 15)

def mover_agente(agente, objeto):
    ax, ay = agente
    ox, oy = objeto
    
    if ax < ox:
        ax += 1  
    elif ax > ox:
        ax -= 1 
    elif ay < oy:
        ay += 1  
    elif ay > oy:
        ay -= 1 
    
    return (ax, ay)


agente = (random.randint(0, 4), random.randint(0, 4))
objeto = (random.randint(0, 4), random.randint(0, 4))

while agente == objeto:
    objeto = (random.randint(0, 4), random.randint(0, 4))  

# Ejecución del agente
while agente != objeto:
    imprimir_cuadricula(agente, objeto)
    time.sleep(0.5)  
    agente = mover_agente(agente, objeto)

imprimir_cuadricula(agente, objeto)
print("¡El agente ha encontrado al objeto!")
