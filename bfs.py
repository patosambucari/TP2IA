import random
from collections import deque

#Se define la función BFS utilizando los parámetros de Inicio, objetivo, limite de desplazamiento y tolerancia.
def bfs(posicion_inicial, posicion_ideal, incremento, desplazamiento_max, tolerancia):
    def meta(position):
        # Definir la función objetivo según el criterio de montaje exitoso
        return abs(position - posicion_ideal) <= tolerancia

    #Se implementa una cola para almacenar y gestionar los nodos
    cola = deque([(posicion_inicial, 0)])
    visitados = set([posicion_inicial])

    #Se muestra en pantalla la posicion ideal buscada (A)
    #Esto podría obviarse, ya que el agente desconoce al iniciar la busqueda cual es la posición inicial, y la encuentra a través de sus sensores
    #Aquí la muestro por pantalla para saber cual será la posición que vamos a buscar, ya que se trata de una representación
    print(f"Posición ideal: {posicion_ideal}")

    #A cada paso se mostrará la posición visitada y la cantidad de movimientos realizados.
    #Se evaluarán las ubicaciones a un lado y otro de la posición inicial, alternadamente
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


# Parámetros del problema
posicion_inicial = 0 #Posicion inicial B
incremento = 1 #Cada movimiento incrementa 1 cm respecto del anterior
desplazamiento_max = 100 #Se limita la busqueda a 100 cm a la derecha y 100 cm a la izquierda de B
tolerancia = 0.5 #Se da un margen de tolerancia de 0,5 cm considerando el tamaño del sensor 

# Generar una posición ideal aleatoria
posicion_ideal = random.uniform(-100, 100)

# Realizar la búsqueda BFS
depth, posicion_final = bfs(posicion_inicial, posicion_ideal, incremento, desplazamiento_max, tolerancia)

if depth >= 0:
    print(f"\nPosición objetivo encontrada: {posicion_final}, Movimientos realizados: {depth}")
else:
    print("No se encontró la posición objetivo.")
