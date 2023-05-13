import random
from collections import deque

# Inicialización de las variables
posicion_objetivo = round(random.uniform(-100, 100), 2)
posicion_actual = 0
desplazamiento_max = 100
incremento = 1
visitados = {posicion_actual: 0}  # Guardamos la profundidad mínima de cada posición
cola = deque([(posicion_actual, 0)])  # Usamos una deque en lugar de una lista para la cola

def meta(pos):
    return abs(pos - posicion_objetivo) <= incremento

while cola:
    current_position, current_depth = cola.popleft()

    print(f"Posición actual: {current_position}, Movimientos realizados: {current_depth}")

    # Si alcanzamos la posición objetivo
    if meta(current_position):
        print(f"Posición objetivo encontrada: {current_position}, Movimientos realizados: {current_depth}")
        break

    # Expansión de nodos vecinos
    neighbors = [current_position - incremento, current_position + incremento]
    for neighbor in neighbors:
        if (-desplazamiento_max <= neighbor <= desplazamiento_max) and (neighbor not in visitados or visitados[neighbor] > current_depth + 1):
            visitados[neighbor] = current_depth + 1
            cola.append((neighbor, current_depth + 1))  # Incrementar current_depth en cada movimiento
