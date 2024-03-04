

class Node:
    
    def __init__(self, data: str):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return '| Data: {} |'.format(self.data)




class LinkedListDoble:

    def __init__(self):
        self.start = None


    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(node.data)

        nodes.append("NIL")
        return " <--> ".join(nodes)


    def insert_at_beginning(self, new_node: Node):
        new_node.next = self.start
        if self.start is not None:
            self.start.prev = new_node
        self.start = new_node


    def insert_at_end(self, new_node: Node):
        if self.start is None:
            self.start = new_node
        else:
            current_node = self.start
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node


    def insert_before(self, reference_node_key: str, new_node: Node):
        if self.start is None:
            print('Linked List is empty')
            return

        if self.start.data == reference_node_key:
            return self.insert_at_beginning(new_node)

        previous_node = self.start

        for current_node in self:
            if current_node.data == reference_node_key:
                previous_node.next = new_node
                new_node.prev = previous_node
                new_node.next = current_node
                current_node.prev = new_node
                return
            
            previous_node = current_node

        print('Reference node key {} not found in linked list...'.format(reference_node_key))


    def traverse_iter(self):
        for current_node in self:
            print(current_node)


    def delete(self, node_key: str):
        if self.start is None:
            print('Linked List Underflow')
            return   

        if self.start.data == node_key:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            return
        
        previous_node = self.start

        for current_node in self:
            if current_node.data == node_key:
                previous_node.next = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = previous_node
                return

            previous_node = current_node

        print('Node key {} not found in linked list...'.format(node_key))

    
my_list = LinkedListDoble()
node1 = Node("Nodo 1")
node2 = Node("Nodo 2")
node3 = Node("Nodo 3")
my_list.insert_at_beginning(node1)
my_list.insert_at_beginning(node2)
my_list.insert_at_end(node3)
my_list.traverse_iter()
my_list.delete("Nodo 2")
my_list.traverse_iter()