# Graph


# class Graph:
#     def __init__(self,gDict=None):
#         if gDict == None:
#             gDict = {}
#         self.gDict = gDict

#     def addEdge(self,vertex,edge):
#         self.gDict[vertex].append(edge)


# customDict = {
#     "a": ["b","c"],
#     "b":["a","e","d"],
#     "c":["a","e"],
#     "d":["b","e","f"],
#     "e":["c","b","d","f"],
#     "f":["d","e"]
# }


# graph = Graph(customDict)
# graph.addEdge('a','d')
# print(graph.gDict)


# Method 2

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list.keys():
            print(vertex, ":", self.adjacency_list[vertex])

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        else:
            return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        else:
            return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            for temp in self.adjacency_list[vertex]:
                self.adjacency_list[temp].remove(vertex)
            # del self.adjacency_list[vertex]
            self.adjacency_list.pop(vertex)
        return True
    
    def bfs(self,vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
    
    def dfs(self,vertex):
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjecent_vertex in self.adjacency_list[current_vertex]:
                if adjecent_vertex not in visited:
                    stack.append(adjecent_vertex)


        


sample = Graph()
sample.add_vertex("A")
sample.add_vertex("B")
sample.add_vertex("C")
sample.add_vertex("D")
sample.addEdge("A","B")
sample.addEdge("A","C")
sample.addEdge("A","D")
sample.addEdge("B","C")
sample.addEdge("C","D")

# sample.remove_edge("D","B")
sample.print_graph()
# print("\n")
# sample.remove_vertex("A")
# sample.print_graph()


# BFS
print("\n")
# sample.bfs("A")
sample.dfs("A")

