from stack import Stack
from linked_list import LinkedList, Node

linkedlist = LinkedList()
linkedlist.insert_at_end(Node('A'))
linkedlist.insert_at_end(Node('B'))
linkedlist.insert_at_end(Node('C'))
linkedlist.insert_at_end(Node('D'))
linkedlist.insert_at_end(Node('E'))
linkedlist.insert_at_end(Node('F'))
linkedlist.insert_at_end(Node('G'))
linkedlist.insert_at_end(Node('H'))
linkedlist.insert_at_end(Node('I'))
linkedlist.insert_at_end(Node('J'))



def invert_linked_list(linked_list: LinkedList) -> LinkedList:
    stack = Stack(10)
    inverted_linked_list = LinkedList()

    print("Linked list original")
    print(linked_list)

    for node in linked_list:
        stack.push(node.data)

    while stack.top != -1:
        node = Node(stack.pop())
        inverted_linked_list.insert_at_end(node)

    print("Linked list invertida")
    print(inverted_linked_list)

invert_linked_list(linkedlist)