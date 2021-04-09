class ArrayStack:
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('cannot pop empty stack')
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('cannot peek empty stack')
        return self.data[-1]

class StackNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top:
            v = self.top.val
            self.top = self.top.next
            return v
        else:
            raise Exception('Cannot pop empty stack')

    def peek(self):
        if self.top:
            return self.top.val
        else:
           raise Exception('Cannot peek empty stack')

    def is_empty(self):
        if self.top:
            return False
        return True

    def push(self, item):
        node = StackNode(item)
        if not self.top:
            self.top = node
        else :
            node.next = self.top
            self.top = node


if __name__ == '__main__':
    # stack = ArrayStack()
    stack  = LinkedListStack()
    stack.push(4)
    print(stack.pop())
    stack.push(3)
    stack.push(2)
    stack.push(12)
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
