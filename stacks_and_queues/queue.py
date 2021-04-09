
class ListQueue:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.insert(0, item)
        print('pushed {} to queue'.format(item))
    
    def pop(self):
        if self.is_empty():
            raise Exception('Cannot call pop() on empty queue')
        return self.data.pop()
    
    def peek(self):
        if self.is_empty():
            raise Exception('Cannot call peek() on empty queue')
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

class QueueNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.first = None  # the start of the linked list
        self.last = None  # the end of the linked list
    
    def push(self, item):
        node = QueueNode(item)
        if not self.last:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
    
    def pop(self):
        if self.is_empty():
            raise Exception('Cannot pop empty queue')
        else:
            val = self.first.val
            self.first = self.first.next
            return val

    def peek(self):
        if self.is_empty():
            raise Exception('Cannot peek empty queue')
        return self.first.val

    def is_empty(self):
        if not self.first:
            return True
        return False



if __name__ == '__main__':
    # queue = ListQueue()
    queue = LinkedListQueue()
    queue.push(3)
    queue.push(2)
    queue.push(1)
    queue.push(0)
    print(queue.pop())
    print(queue.peek())
    print(queue.pop())
    print(queue.peek())
    print(queue.pop())
    print(queue.peek())
    print(queue.pop())
