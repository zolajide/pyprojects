# ---------------------------------------------
# Name: Zainab Olajide
# Date: 3/12/2025
# Assignment: Simple Dijkstra's Path Finder
# Description: Finds the shortest path from a 
#              starting node to all others using
#              basic Dijkstra's algorithm.
# ---------------------------------------------

def simple_dijkstra(graph, start):
    # Initialize distances: start = 0, others = infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Track visited nodes
    visited = set()

    while len(visited) < len(graph):
        # Find the unvisited node with the smallest distance
        current_node = None
        for node in graph:
            if node not in visited:
                if current_node is None or distances[node] < distances[current_node]:
                    current_node = node

        # Mark node as visited
        visited.add(current_node)

        # Update distances for neighbors
        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 5, 'D': 10},
        'C': {'A': 2, 'B': 5, 'D': 3},
        'D': {'B': 10, 'C': 3}
    }

    start = 'A'
    result = simple_dijkstra(graph, start)

    print(f"Shortest paths from {start}:")
    for node, distance in result.items():
        print(f"{start} → {node} : {distance}")
