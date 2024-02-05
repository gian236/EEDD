'''
Stack Use Case: Reversing a List.
'''


from stack import Stack


original_list = ['1', '33', '14', '16', '55']
print('\nOriginal list:', original_list)
stack = Stack(5)

print('\nPushing to stack...\n')
for element in original_list:
    stack.push(element)
    print(stack)

reversed_list = []

print('\nPopping from stack into new list...\n')
while stack.peek() != 'Stack Underflow':
    reversed_list.append(stack.pop())
    print(stack)
    print('New list:', reversed_list)

print('\nReversed list:', reversed_list)
