

class StackDoble:

    def __init__(self, size: int):
        self.elements = [None] * size
        self.top1 = -1
        self.top2 = size
        self.max = size


    def __repr__(self):
        return "Stack Completo: {} | Top 1: {} | Top 2: {}".format(self.elements, self.top1, self.top2)
        


    def push1(self, val: str) -> None:
        if self.top1 + 1 == self.top2:
            print("Stack 1 Overflow")
            return None

        self.top1 += 1
        self.elements[self.top1] = val

    def push2(self, val: str) -> None:
        if self.top2 - 1 == self.top1:
            print("Stack 2 Overflow")
            return None

        self.top2 -= 1
        self.elements[self.top2] = val

    def pop1(self) -> str:
        if self.top1 == -1:
            return "Stack 1 Underflow"

        val = self.elements[self.top1]
        self.elements[self.top1] = None
        self.top1 -= 1
        return val

    def pop2(self) -> str:
        if self.top2 == self.max:
            return "Stack 2 Underflow"

        val = self.elements[self.top2]
        self.elements[self.top2] = None
        self.top2 += 1
        return val

    def peek1(self) -> str:
        if self.top1 == -1:
            return "Stack 1 Underflow"

        val = self.elements[self.top1]
        return val

    def peek2(self) -> str:
        if self.top2 == self.max:
            return "Stack 2 Underflow"

        val = self.elements[self.top2]
        return val
    

stack = StackDoble(10)
stack.push1('A1')
stack.push1('B1')
stack.push1('C1')
stack.push1('D1')
stack.push1('E1')
stack.push2('F2')
stack.push2('G2')
stack.push2('H2')
stack.push2('I2')
stack.push2('J2')

print(stack)
print("Pop 1: ", stack.pop1())
print("Pop 1: ", stack.pop1())
print("Pop 2: ", stack.pop2())
print("Pop 2: ", stack.pop2())
