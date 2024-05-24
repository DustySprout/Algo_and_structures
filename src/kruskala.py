"Name of file"
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, start_vertex, end_vertex, weight):
        self.edges.append([start_vertex, end_vertex, weight])

    def find(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find(parent, parent[vertex])

    def union(self, parent, rank, vertex_x, vertex_y):
        root_x = self.find(parent, vertex_x)
        root_y = self.find(parent, vertex_y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

'Correct name "Kruskal"'
    def kryskala(self):
        result = []
        edge_index, edge_count = 0, 0
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.num_vertices):
            parent.append(node)
            rank.append(0)

        while edge_count < self.num_vertices - 1:
            start_vertex, end_vertex, weight = self.edges[edge_index]
            edge_index += 1
            root_start = self.find(parent, start_vertex)
            root_end = self.find(parent, end_vertex)
            if root_start != root_end:
                edge_count += 1
                result.append([start_vertex, end_vertex, weight])
                self.union(parent, rank, root_start, root_end)

        return result

    def apply_union(self, parent, rank, param, param1):
        pass
