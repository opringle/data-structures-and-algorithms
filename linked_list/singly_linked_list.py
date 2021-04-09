class Node:
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        element = self.head

        if element is None:
            self.head = node
            return
        
        while element.next is not None:
            element = element.next

        # insert the node
        element.next = node

    def print(self):
        current = self.head
        out = []
        while current is not None:
            out.append(str(current.value))
            current = current.next
        print('->'.join(out))

    def delete(self, value: int):
        current = self.head

        # if the node is at the head just remove it
        if current.value == value:
            self.head = current.next
            return
        
        # if the node is anywhere else, move prev pointer
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def prepend(self, node):
        node.next = self.head
        self.head = node

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

if __name__ == '__main__':
    singly_linked_list = SinglyLinkedList()
    node_1 = Node(5)
    node_2 = Node(1)
    node_3 = Node(17)
    singly_linked_list.append(node_1)
    singly_linked_list.append(node_2)
    singly_linked_list.append(node_3)
    singly_linked_list.print()
    singly_linked_list.delete(value=1)
    singly_linked_list.print()
    singly_linked_list.delete(value=5)
    singly_linked_list.print()
    singly_linked_list.append(Node(13))
    singly_linked_list.print()
    singly_linked_list.prepend(Node(12))
    singly_linked_list.print()
    print(singly_linked_list.search(4))
    print(singly_linked_list.search(12))
