def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

def dfs(graph, start, goal):
    visited = set()
    path = []
    _dfs(graph, start, goal, visited, path)
    return path

def _dfs(graph, node, goal, visited, path):
    if node == goal:
        path.append(node)
        return True

    visited.add(node)
    path.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if _dfs(graph, neighbor, goal, visited, path):
                return True

    path.pop()
    return False

def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()

    if start == goal:
        return [start]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            visited.add(node)

    return []

graph = {}
add_edge(graph, 'A Block', 'B Block')
add_edge(graph, 'B Block', 'C Block')
add_edge(graph, 'C Block', 'D Block')
add_edge(graph, 'D Block', 'E Block')
add_edge(graph, 'E Block', 'F Block')
add_edge(graph, 'E Block', 'B Block')
add_edge(graph, 'F Block', 'D Block')
add_edge(graph, 'F Block', 'B Block')

print("\t\t\tThis is the PDEU Map")
source_block = input("Enter the source block: ")
goal_block = input("Enter the goal block: ")

dfs_path = dfs(graph, source_block, goal_block)
bfs_path = bfs(graph, source_block, goal_block)

print(f"DFS Path: {dfs_path}")
print(f"BFS Path: {bfs_path}")