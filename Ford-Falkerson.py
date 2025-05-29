def bfs(r_graph, source, sink, parent):
    V = len(r_graph)
    visited = [False] * V
    queue = []
    queue.append(source)
    visited[source] = True
    parent[source] = -1
    while queue:
        u = queue.pop(0)
        for v in range(V):
            if not visited[v] and r_graph[u][v] > 0:
                queue.append(v)
                parent[v] = u
                visited[v] = True
    return visited[sink]

def ford_fulkerson(graph, source, sink):
    V = len(graph)
    residual_graph = [[graph[u][v] for v in range(V)] for u in range(V)]
    parent = [-1] * V
    max_flow = 0
    while bfs(residual_graph, source, sink, parent):
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = parent[v]
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
        max_flow += path_flow
    return max_flow
graph = [
    [0, 5, 4, 0, 0],
    [0, 0, 0, 3, 2],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0]
    ]
print(f"Максимальный поток: {ford_fulkerson(graph, 0, 4)}")