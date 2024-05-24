from src.avl_priority_queue import AVLTree


def read_input(filename):
    with open(filename, 'r') as file:
        vertexes, edges = map(int, file.readline().split())
        clients = list(map(int, file.readline().split()))
        connections = []
        for _ in range(edges):
            start, end, latency = map(int, file.readline().split())
            connections.append((start, end, latency))
    return vertexes, edges, clients, connections


def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))


def find_max_latency_from_server_to_clients(graph, start, clients):
    latencies = {vertex: float("inf") for vertex in graph}

    latencies[start] = 0
    visited = set()
    from_to = {}
    priority_queue = AVLTree(start, 0)
    while not priority_queue.is_empty():
        current = priority_queue.dequeue()
        print(current)
        current_vortex = current[0]
        neighbor_vortexes = graph[current_vortex]
        for vertex, latency in neighbor_vortexes:
            if vertex in visited:
                continue
            visited.add(vertex)
            if (latencies[current_vortex] + latency) < latencies[vertex]:
                latencies[vertex] = latencies[current_vortex] + latency
                from_to[vertex] = current
            priority_queue.insert(vertex, latencies[vertex])
    return max([latencies[x] for x in clients])


def list_of_connections_to_dict(connections):
    graph = {}
    for connection in connections:
        source, target, latency = connection
        if source not in graph:
            graph[source] = []
        if target not in graph:
            graph[target] = []
        graph[source].append((target, latency))
        graph[target].append((source, latency))
    return graph


def find_key_of_routers(vertexes, clients):
    routers = set(x for x in range(1, vertexes + 1))
    routers.difference_update(clients)
    return routers


def find_maximum_latency_for_each_router(routers, connections, clients):
    graph = list_of_connections_to_dict(connections)
    max_routers_latency = []
    for route in routers:
        max_routers_latency.append(
            find_max_latency_from_server_to_clients(graph, route, clients)
        )
    return min(max_routers_latency)


def find_minimum_latency(vertexes, clients, connections):
    routers = find_key_of_routers(vertexes, clients)
    return find_maximum_latency_for_each_router(routers, connections, clients)


def find_minimum_latency_from_file(file_input, file_output):
    vertexes, edges, clients, connections = read_input(file_input)
    result = find_minimum_latency(vertexes, clients, connections)
    write_output(file_output, result)
