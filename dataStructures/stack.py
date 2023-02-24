# LIFO - Last In First Out

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return len(self.container) == 0
    
stack = Stack()

# push()
stack.push(1)
stack.push(2)
stack.push(3)

# pop()
print(stack.pop())

# peek()
print(stack.peek())

# size()
print(stack.size())

# is_empty()
print(stack.is_empty())
