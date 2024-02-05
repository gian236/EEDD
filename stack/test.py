'''
Stack Class Testing.
'''


from stack import Stack


# Stack object initialization
stack = Stack(5)
print(stack)

# First push
stack.push('A')
print(stack)

# Other pushes
stack.push('B')
stack.push('C')
stack.push('D')
stack.push('E')
print(stack)
stack.push('F')  # Stack overflow

# First Pop
stack.pop()
print(stack)

# Other pops
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack)
stack.pop()  # Stack underflow

# Peeks
stack.push('D')
stack.push('C')
print(stack)
print('Peek: ', stack.peek())
stack.push('E')
print(stack)
print('Peek: ', stack.peek())
