from collections import deque

romania_map = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Oradea', 'Arad'],
    'Oradea': ['Sibiu', 'Zerind'],
    'Sibiu': ['Fagaras', 'Rimnicu Vilcea', 'Oradea', 'Arad'],
    'Timisoara': ['Lugoj', 'Arad'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Drobeta', 'Lugoj'],
    'Drobeta': ['Craiova', 'Mehadia'],
    'Craiova': ['Pitesti', 'Rimnicu Vilcea', 'Drobeta'],
    'Rimnicu Vilcea': ['Craiova', 'Sibiu', 'Pitesti'],
    'Pitesti': ['Bucharest', 'Craiova', 'Rimnicu Vilcea'],
    'Fagaras': ['Bucharest', 'Sibiu'],
    'Bucharest': ['Urziceni', 'Giurgiu', 'Pitesti', 'Fagaras'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Hirsova', 'Vaslui', 'Bucharest'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Neamt': ['Iasi']
}

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(node)

# Finding the shortest path from Arad to Bucharest
shortest_path = bfs_shortest_path(romania_map, 'Arad', 'Bucharest')
print(f"The shortest path from Arad to Bucharest is: {shortest_path}")
