# adjacency list represented using dict and lists
class Graph:
    def __init__(self, num_nodes: int):
        self.adjacency_list = {i: [] for i in range(num_nodes)} 

    def add_edge(self, src: int, dest:int):
        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src)

    def print_graph(self):
        print(self.adjacency_list)

# adjacency list represented using custom classes
class AdjacencyNode:
    def __init__(self, val):
        self.val = val
        self.children = set()
    
class Graph2:
    def __init__(self, num_nodes: int):
        self.nodes = [AdjacencyNode(i) for i in range(num_nodes)]

    def add_edge(self, src: int, dest:int):
        self.nodes[src].children.add(self.nodes[dest])
        self.nodes[dest].children.add(self.nodes[src])

    def print_graph(self):
        for node in self.nodes:
            print("Node {}'s children {}".format(
                node.val, 
                [n.val for n in node.children]
            ))


if __name__ == '__main__':
    num_vertices = 5
    graph = Graph2(num_vertices)

    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()