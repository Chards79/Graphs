"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue the starting node
        q.enqueue(starting_vertex)

        # make a set to track if it's been here before
        visited = set()

        # while the queue isn't empty (still vertices in the queue)
        while q.size() > 0:
            # dequeue whatever's at the front of the line, this is the current_node
            current_node = q.dequeue()
            # if that node hasn't been visited yet,
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
                print(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of the neighbors,
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on the starting node
        s.push(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while the stack isn't empty
        while s.size() > 0:
            # pop off whatever's on top, this is current_node
            current_node = s.pop()
        # if we haven't visited this vertex before
            if current_node not in visited:
                # run function / print
                print(current_node)
        # mark as visited
                visited.add(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of the neighbors
                for neighbor in neighbors:
                    # add to the stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # instantiate visited to a set if None
        if visited is None:
            visited = set()
        # check if vertex has been visited
        if starting_vertex not in visited:
            # mark this vertex as visited
            visited.add(starting_vertex)
            print(starting_vertex)
        # for each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            # if it's not visited
            if neighbor not in visited:
                # recurse on the neighbor
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # make a set to track nodes we've visited
        visited = set()

        path = [starting_vertex]
        q.enqueue(path)

        # while queue isn't empty
        while q.size() > 0:
            # dequeue the path at the front of the line
            current_path = q.dequeue()
            current_node = current_path[-1]

        # if this node is our target node
            if current_node == destination_vertex:
                # return it!! return TRUE
                return current_path

        # if not visited
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each neighbor
                for neighbor in neighbors:
                    # copy path so we don't mutate the original path for different nodes
                    path_copy = current_path[:]
                    path_copy.append(neighbor)

                # add to our queue
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        s = Stack()
        # make a set to track nodes we've visited
        visited = set()

        path = [starting_vertex]
        s.push(path)

        # while queue isn't empty
        while s.size() > 0:
            # dequeue the path at the front of the line
            current_path = s.pop()
            current_node = current_path[-1]

        # if this node is our target node
            if current_node == destination_vertex:
                # return it!! return TRUE
                return current_path

        # if not visited
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each neighbor
                for neighbor in neighbors:
                    # copy path so we don't mutate the original path for different nodes
                    path_copy = current_path[:]
                    path_copy.append(neighbor)

                # add to our queue
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize visited and/or path if None:
        if visited is None:
            visited = set()

        if path is None:
            path = []

        # check if starting vertex has been visited
        # if it hasn't been visited, mark it as visited
        visited.add(starting_vertex)

        # add to path
        path = path + [starting_vertex]

        # check if it's the targeted vertex:
        if starting_vertex == destination_vertex:
            # if it is, return the path - END POINT
            return path

        # otherwise, check neighbors of current vertex
        for next_vertex in self.get_neighbors(starting_vertex):
            # if neighbor not visited:
            if next_vertex not in visited:
                # call dfs_recursive on neighbor w/ updated path
                new_path = self.dfs_recursive(
                    next_vertex, destination_vertex, visited, path)
                # get back either None or valid path to destination vertex
                # if valid path, return it back up the chain
                if new_path:
                    return new_path
        # if not target and all neighbors visited, return none END?
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
