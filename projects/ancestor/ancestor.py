from stack import Stack


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    s = Stack()
    s.push([starting_node])

    visited = set()

    path_list = list()
    path_len_list = list()

    while s.size() > 0:
        path = s.pop()

        last_vertex = path[-1]

        if last_vertex not in visited:

            path_list.append(path)
            path_len_list.append(len(path))

            visited.add(last_vertex)

            for next_vertex in graph.get_neighbors(last_vertex):
                path_copy = list(path)

                path_copy.append(next_vertex)

                s.push(path_copy)
    print(path_list)
    max_len = max(path_len_list)
    tied_earliest = list()

    if max_len == 1:
        return -1
    else:
        for path in path_list:
            if len(path) == max_len:
                tied_earliest.append(path[-1])
        return min(tied_earliest)
