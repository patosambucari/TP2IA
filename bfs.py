import random
from collections import deque

def bfs(posicion_inicial, posicion_ideal, incremento, desplazamiento_max, tolerancia):
    def meta(position):
        # Definir la función objetivo según el criterio de montaje exitoso
        return abs(position - posicion_ideal) <= tolerancia

    cola = deque([(posicion_inicial, 0)])
    visitados = set([posicion_inicial])

    print(f"Posición ideal: {posicion_ideal}")

    while cola:
        current_position, current_depth = cola.popleft()

        print(f"Posición actual: {current_position}, Movimientos realizados: {current_depth}")

        # Si alcanzamos la posición objetivo
        if meta(current_position):
            return current_depth, current_position

        # Expansión de nodos vecinos
        neighbors = [current_position - incremento, current_position + incremento]
        for neighbor in neighbors:
            if (neighbor not in visitados) and (-desplazamiento_max <= neighbor <= desplazamiento_max):
                visitados.add(neighbor)
                cola.append((neighbor, current_depth + 1))

    # Si no encontramos la posición objetivo
    return -1, None

# Parámetros del problema
posicion_inicial = 0
incremento = 0.1
desplazamiento_max = 10
tolerancia = 0.05

# Generar una posición ideal aleatoria
posicion_ideal = random.uniform(-10, 10)

# Realizar la búsqueda BFS
depth, posicion_final = bfs(posicion_inicial, posicion_ideal, incremento, desplazamiento_max, tolerancia)

if depth >= 0:
    print(f"\nPosición objetivo encontrada: {posicion_final}, Movimientos realizados: {depth}")
else:
    print("No se encontró la posición objetivo.")
