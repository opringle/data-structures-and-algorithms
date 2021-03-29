class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        out = []
        while current is not None:
            out.append('{}'.format(current.value))
            current = current.next
        print('<->'.join(out))

    def append(self, value):
        node = Node(value)

        current = self.head
        if current is None:
            self.head = node
            return

        # iterate to the penultimate item in the list
        while current.next is not None:
            current = current.next
        
        # insert the element at the next position
        node.prev = current
        current.next = node

    def insert(self, value, position: int):
        node = Node(value)
        current = self.head
        current_position = 0

        if position == 0:
            node.next = self.head
            self.head = node
            self.head.next.prev = node
            return

        while current.next is not None:
            # print('current position = {}'.format(current_position))
            if current_position + 1 == position:
                # insert the node
                node.next = current.next
                current.next = node
                node.prev = current
                node.next.prev = node
                return
            current = current.next
            current_position += 1
        raise Exception('Position {} does not exist in linked list of length {}'.format(position, current_position+1))


if __name__ == '__main__':
    l = DoublyLinkedList()
    l.append(16)
    l.show()
    l.append(19)
    l.show()
    l.insert(8, 0)
    l.show()
    l.insert(80, 0)
    l.show()
    l.insert(81, 2)
    l.show()
    l.insert(8, 4)
    l.show()