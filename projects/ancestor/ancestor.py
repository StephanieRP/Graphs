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

    def find_earliest(self, child):
        verts = self.vertices

        queue = [[child]]
        visited = {child}
        ancestries = []

        for i in range(len(verts)):
            try:
                path = queue.pop(0)
                visit = path[-1]
                visited.add(visit)
                branches = set(self._unvisited_edges(visit, visited))
                if len(branches) == 0:
                    ancestries.append(path)
                else:
                    for i in branches:
                        queue.append(path + [i])
            except IndexError:
                longest_lineage = max([len(i) for i in ancestries])
                earliest_ancestries = [
                    i for i in ancestries if len(i) >= longest_lineage]
                earliest_ancestor = min([i[-1] for i in earliest_ancestries])
                break
            except TypeError:
                earliest_ancestor = -1
                break

        if earliest_ancestor == child:
            earliest_ancestor = -1

        return earliest_ancestor


def earliest_ancestor(ancestors, child):
    graph = Graph()
    for j, k in ancestors:
        graph.add_parents(j, k)

    return graph.find_earliest(child)
