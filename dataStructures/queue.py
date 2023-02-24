# FIFO - First In First Out

from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, value):
        self.container.appendleft(value)

    def dequeue(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0
    
queue = Queue()

# enqueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# dequeue()
print(queue.dequeue())

# peek()
print(queue.peek())

# size()
print(queue.size())

# is_empty()
print(queue.is_empty())
