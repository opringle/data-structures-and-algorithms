# Stacks

Stacks use LIFO ordering - the last item in is the first item that can be removed (like a stack of plates on a dining table). The last item into the stack can be accessed in constant time. Also you can add items in constant time. Stacks can be implemented using a linked list or array. They implement the following methods:

- pop() - remove and return the element on top of the stack
- peek() - show the element on the top of the stack
- push(item) - add an item to the stack
- isEmpty() - determine whether the stack is empty

Stacks are used in UI navigation or undo features.

# Graphs

A graph is a collection of nodes (somtimes called vertices) with edges between some of them (trees are a type of graph). Graphs can be directed (edges can be traversed in on direction) or undirected (edges can be traversed in both directions). 

- *Connect graphs* have a path between every pair of vertices. A tree is an example of this.
- *Asyclic graphs* have no cycles. A tree is an example of this.

### Adjacency list

This is the most common way to represent a graph. For each node, store it's adjacent nodes.

```python
class Graph:
    def __init__(self, nodes: List[GraphNode]):
        self.nodes = nodes

class GraphNode:
    def __init__(self, val, children: List[GraphNode]):
        self.val = val
        # the node's adjacent nodes
        self.children = children
```

Notice that the GraphNode is the same as you would use in a tree, however, there can be any number of children to a given node. The Graph class is necessary because there may not be a root node from which you can reach every other node.

You don't need to define a class to store the adjacency list. For example:

```python
graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [2],
    4: [6],
    5: [4],
    6: [5]
}
```

Here we can see node 2 is adjacent to nodes 0 and 3.

It's recommended to use node and graph classes unless told not to.

### Adjacency matrix

Boolean matrix of size n*n where n is the number of nodes in the graph. A True value at matrix[i][j] represents an edge from node i to node j. If the graph is undirected this matrix willl be symetric.

The disadvantage of the adjacency matrix is that you need to iterate through all the nodes to determine a given node's neighbours. In the example below, to determine node 2's neighbours we need to check [:, 2] and [2, :].

|idx|0|1|2|3|
|---|-|-|-|-|
| 0 |0|1|0|0|
| 1 |0|0|1|0|
| 2 |1|0|0|0|
| 3 |0|0|1|0|

### Graph search

- *Depth first search* - Start at an arbitrarily selected node and explore each branch completely before moving onto the next branch.
- *Breadth first search* - Start at an arbitrarily selected node and explore all the neighbours before moving to their children.
- *Bidirectional search* - This algorithm finds the shortest path between a source and destination node. You run two BFS's from the source and destination nodes. When the searches collide, you have found the shortest path. This is much more efficient than using BFS because at each level of the search the time complexity increase by a factor of K, where K is the maximum number of adjacent nodes. If BFS traverses 4 levels it moved through k^4 children. Bidirectional search would move through 2 * K^2 children.

Depth first search is simpler if you want to visit every node in the graph. However, to find a path between two nodes, BFS is generally better. (think finding if Ash is Sarah's friend in the facebook contacts graph)

```python
# DFS (similar to preorder tree traversal)
def depth_first_search(root: GraphNode):
    if not root:
        return
    print('visited node {}'.format(root.val))
    root.visited = True
    for node in root.children:
        if not node.visited:
            depth_first_search(node)
```

BFS can be implemented using a queue. This ensures that nodes are visited in the order they are inserted into the queue.

```python
# BFS (NOT recursive)

def breath_first_search(root: GraphNode):
    queue = []
    root.visited = True
    queue.insert(0, root) # enqueue

    while len(queue) > 0:  # queue not empty
        node = queue.pop()  # dequeue
        print('visited node {}'.format(node.val))
        for child in node.children:
            if not child.visited:
                child.visited = True
                queue.insert(0, child)
```