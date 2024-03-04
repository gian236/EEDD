"""
Stack Class Implementation.
"""


class Stack:

    def __init__(self, size: int):
        self.elements = [None] * size
        self.top = -1
        self.max = size


    def __repr__(self):
        return "Stack: {} | Top: {}".format(self.elements, self.top)


    def push(self, val: str) -> None:
        if self.top == self.max - 1:
            print("Stack Overflow")
            return None

        self.top += 1
        self.elements[self.top] = val


    def pop(self) -> str:
        if self.top == -1:
            return "Stack Underflow"

        val = self.elements[self.top]
        self.elements[self.top] = None
        self.top -= 1
        return val


    def peek(self) -> str:
        if self.top == -1:
            return "Stack Underflow"

        val = self.elements[self.top]
        return val
