 

def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = [(start, [start])]  # Tuple of vertex and its path

    paths = []
    while queue:
        vertex, path = queue.pop(0)
        if vertex not in visited:
            print(vertex)
            print(queue)
            visited.add(vertex)
            
            if vertex == end:
                paths.append(path)
            
            neighbors = graph[vertex]
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return paths



def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex)  # or perform any other operation on the vertex
            visited.add(vertex)
            neighbors = graph[vertex]
            queue.extend(neighbors)

# read adjacency matrix and make graph
f = open("adj.txt", "r")
graph = {}
for i, x in enumerate(f):
    x = x.strip().replace(" ", "")
    graph[i] = []
    for j, num in enumerate(x):
        
        if num == "1":
            graph[i].append(j)

print(graph)
#for key in graph.keys():
#    print(key, graph[key])

bfs(graph, 0)
print()
shortest = bfs_shortest_path(graph, 0, 5)
print(shortest)
