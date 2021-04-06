# Stacks

Stacks use LIFO ordering - the last item in is the first item that can be removed (like a stack of plates on a dining table). The last item into the stack can be accessed in constant time. Also you can add items in constant time. Stacks can be implemented using a linked list or array. They implement the following methods:

- pop() - remove and return the element on top of the stack
- peek() - show the element on the top of the stack
- push(item) - add an item to the stack
- isEmpty() - determine whether the stack is empty

Stacks are used in UI navigation or undo features.

# Queues

Queues use FIFO ordering - the first item into the queue is the first item that can be accessed (like a queue for a restaurant). 

- add(item) - add an item to the queue
- remove() - remove an item from the front of the queue
- peek() - return the top of the queue
- isEmpty() - return true if the queue is empty

A queue can also be implemented using a linked list, so long as data is added and removed from opposite sides.

