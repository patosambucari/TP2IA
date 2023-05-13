import heapq

def a_estrella(inicio, objetivo, incremento, max_desplazamiento, heuristica):
    abiertos = [(0, 0, inicio)]  # (costo_total, profundidad, posicion)
    visitados = set()

    while abiertos:
        costo_total, profundidad, posicion_actual = heapq.heappop(abiertos)

        if posicion_actual in visitados:
            continue
        visitados.add(posicion_actual)

        if objetivo(posicion_actual):
            return profundidad, posicion_actual

        vecinos = [posicion_actual - incremento, posicion_actual + incremento]
        for vecino in vecinos:
            if vecino not in visitados and -max_desplazamiento <= vecino <= max_desplazamiento:
                costo = profundidad + 1 + heuristica(vecino)
                heapq.heappush(abiertos, (costo, profundidad + 1, vecino))

    #Si no se encuentra solución
    return -1, None

def objetivo(posicion):
    return abs(posicion - posicion_ideal) <= tolerancia

def heuristica(posicion):
    return abs(posicion - posicion_ideal) / incremento

# Parámetros del problema
posicion_inicial = 0
incremento = 0.1
max_desplazamiento = 5
posicion_ideal = 1.5
tolerancia = 0.05

# Realizar la búsqueda A*
profundidad, posicion_final = a_estrella(posicion_inicial, objetivo, incremento, max_desplazamiento, heuristica)

if profundidad >= 0:
    print(f"Posición objetivo encontrada: {posicion_final}, movimientos realizados: {profundidad}")
else:
    print("No se encontró la posición objetivo.")












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
                cola.append((neighbor, current_depth + 1))  # Incrementar current_depth en cada movimiento

    # Si no encontramos la posición objetivo
    return -1, None
