import random
import heapq

#Se define la función A Star utilizando los parámetros de Inicio, objetivo, limite de desplazamiento y tolerancia.
def a_star(posicion_inicial, posicion_ideal, incremento, desplazamiento_max, tolerancia, alfa=1, beta=1):
    def meta(position):
        return abs(position - posicion_ideal) <= tolerancia

    #Se define la funciòn heurística que guiará la busqueda
    def heuristica(position):
        d = abs(posicion_ideal - position)  # Distancia al objetivo
        r = get_surface_difference(position, posicion_ideal)  # Diferencia de relieve
        return alfa * d + beta * r #Se la heuristica considerando los pesos de alfa y beta, de acuerdo a la importancia que quiera darse a cada uno

    #Se implementa una cola de prioridades, hará que se visiten primero los nodos con menor prioeridad
    cola_prioridad = [(0, posicion_inicial, 0)]
    visitados = set([posicion_inicial])

    #Se muestra en pantalla la posicion ideal buscada (A)
    #Esto podría obviarse, ya que el agente desconoce al iniciar la busqueda cual es la posición inicial, y la encuentra a través de sus sensores
    #Aquí la muestro por pantalla para saber cual será la posición que vamos a buscar, ya que se trata de una representación
    print(f"Posición ideal: {posicion_ideal}")

    #A cada paso se mostrará la posición visitada y la cantidad de movimientos realizados.
    #Se evaluarán las ubicaciones solo hacia un lado, hacia el que la exploración de relieve oriente la busqueda
    while cola_prioridad:
        _, current_position, current_depth = heapq.heappop(cola_prioridad)

        displayed_depth = current_depth if current_position < 0 else current_depth + 1

        print(f"Posición actual: {current_position}, Movimientos realizados: {displayed_depth}")

        # Si alcanzamos la posición objetivo
        if meta(current_position):
            return displayed_depth, current_position

        # Expansión de nodos vecinos
        for i in range(2):
            neighbor = current_position - incremento if i == 0 else current_position + incremento
            if (-desplazamiento_max <= neighbor <= desplazamiento_max) and (neighbor not in visitados):
                visitados.add(neighbor)
                current_depth += 1
                prioridad = current_depth + heuristica(neighbor)
                heapq.heappush(cola_prioridad, (prioridad, neighbor, current_depth))
    # Si no se encuentra solución
    return -1, None

def get_surface_difference(current_position, target_position):
    # Aquí se deberia implementar la logica para calcular el relieve de la pieza con respecto al plano
    # Para ello es necesario contar con un mapeo de superficie como prerequisito para la definición del algoritmo
    # A fines prácticos vamos a arrojar un valor aleatorio entre 0 y 1
    return random.uniform(0, 1)

# Parámetros del problema
posicion_inicial = 0
incremento = 1
desplazamiento_max = 100
tolerancia = 0.5
alfa = 1 #Peso asignado a la importancia de la distancia en el calculo
beta = 1 #Peso asignado a la importancia del calculo del relieve
        #Vamos a considerar para el caso que son igualmente importantes, ya que en principio no contamos con información sobre el relieve

# Generar una posición ideal aleatoria
posicion_ideal = random.uniform(-100, 100)

# Realizar la búsqueda por el método A Star
depth, posicion_final = a_star(posicion_inicial, posicion_ideal, incremento, desplazamiento_max, tolerancia, alfa, beta)

if depth >= 0:
    print(f"\nPosición objetivo encontrada: {posicion_final}, Movimientos realizados: {depth}")
else:
    print("No se encontró la posición objetivo.")
