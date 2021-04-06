
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def in_order_traversal(node: Node) -> None:
    while node:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)
        return

def pre_order_traversal(node: Node) -> None:
    while node:
        print(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
        return
def post_order_traversal(node: Node) -> None:
    while node:
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
        print(node.data)
        return

if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.right = Node(2)
    print('\nin-order traversal:\n')
    in_order_traversal(root)
    print('\npre-order traversal:\n')
    pre_order_traversal(root)
    print('\npost-order traversal:\n')
    post_order_traversal(root)

