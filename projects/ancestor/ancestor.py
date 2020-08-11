from stack import Stack


# def __init__(self):
#     self.vertices = {}


# def add_vertex(self, vertex_id):
#     self.vertices[vertex_id] = set()


# def add_edge(self, v1, v2):
#     if v1 in self.vertices and v2 in self.vertices:
#         self.vertices[v1].add(v2)
#     else:
#         raise IndexError("Vertex does not exist")


def get_neighbors(self, vertex_id):
    return self.vertices[vertex_id]


def earliest_ancestor(self, starting_node, ending_node):
    s = Stack()
    s.push([starting_node])

    visited = set()

    while s.size() > 0:
        path = s.pop()

        last_vertex = path[-1]

        if last_vertex not in visited:
            # logic to choose lowest numeric ID if more than one earliest ancestor
            if last_vertex == ending_node:
                return path

            visited.add(last_vertex)

            for next_vertex in self.get_neighbors(last_vertex):
                path_copy = list(path)

                path_copy.append(next_vertex)

                s.push(path_copy)

    return None
