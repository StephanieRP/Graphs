class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        verts = self.vertices
        if verts.get(vertex) == None:
            verts[vertex] = set()

    def add_parents(self, v1, v2):
        verts = self.vertices
        if v1 not in verts:
            self.add_vertex(v1)
        if v2 not in verts:
            self.add_vertex(v2)
        if v1 in verts and v2 in verts:
            verts[v2].add(v1)
        else:
            raise Exception

    def _unvisited_edges(self, vertex, visited):
        return [i for i in self.vertices.get(vertex) if i not in visited]

        
def earliest_ancestor(ancestors, starting_node):
    pass