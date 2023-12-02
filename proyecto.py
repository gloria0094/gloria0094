import networkx as nx

def dijkstra(graph, start_node):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start_node] = 0

    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = sorted(priority_queue)[0]
        priority_queue.remove((current_distance, current_node))

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))

    return distances

# Crear un grafo dirigido de ejemplo
G = nx.DiGraph()

G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=1)

# Calcular las distancias mínimas utilizando Dijkstra desde el nodo 'A'
inicio_dijkstra = 'A'
resultados_dijkstra = dijkstra(G, inicio_dijkstra)

# Imprimir los resultados
for nodo, distancia in resultados_dijkstra.items():
    print(f"Distancia mínima desde {inicio_dijkstra} hasta {nodo}: {distancia}")

