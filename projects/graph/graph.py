"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if not vertex in self.vertices:
            self.vertices[vertex] = set()
        else:
            print("Warning: Vertex already exists.")

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1) #  for if bi-directional edge
        else:
            print("Warning: One or more of the vertices do not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create empty queue, enqueue the starting vertex - FIFO
        # Create a set to store the visited vertices
        # While queue is not empty...
            # Dequeue the first vertex
            # If that vertex has not been visited...
                # Mark visited
                 # Add all of its neighbors (node's siblings/share same parent/those nodes on the same level) to the back of queue
        q = Queue()
        q.enqueue(starting_vertex)
        visited = []
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.append(v)

                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)

        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        # Create a Set to store visited vertices
        # While the stack is not empty...
            # Pop the first vertex
            # If that vertex has not been visited...
                # Mark it as visited...
                # Then add all of its neighbors to the top/end of the stack

        s = Stack()
        s.push(starting_vertex)
        visited = []

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.append(v)

                for next_vert in self.vertices[v]:
                    s.push(next_vert)

        return visited

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None: # or use visited=[] as arg in place of this if statement
            visited = []

        visited.append(starting_vertex)

        for vertex in self.vertices[starting_vertex]:
            if vertex not in visited:
                self.dft_recursive(vertex, visited) # add visited as arg so we can share the same list of visited and not reset it to [] for each recursion
        

        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        q.enqueue([starting_vertex])

        visited = []

        while q.size() > 0:
            path = q.dequeue() # path = returned first item in queue
            v = path[-1] # current vert = last item in path

            if v not in visited:
                if v == destination_vertex:
                    return path

                visited.append(v)

                for next_vert in self.vertices[v]:
                    """ 
                    a = 5
                    b = a
                    a += 1
                    print(a, b) --> 6, 5
                    new_path is the same data as path, but we want an actual copy, not just point to the same reference, so we use list(path)
                    since we want to explore different paths
                    """
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
           

        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push([starting_vertex])

        visited = []

        while s.size() > 0:
            path = s.pop() # path = returned first item in queue
            v = path[-1] # last item in path

            if v not in visited:
                if v == destination_vertex:
                    return path
                visited.append(v)

                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)
           

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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
