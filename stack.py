class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]
