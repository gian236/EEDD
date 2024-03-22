class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return '({})'.format(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.recursive_insert(self.root, data)

    def recursive_insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.recursive_insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.recursive_insert(node.right, data)

    def traverse(self):
        return self.recursive_traverse(self.root)
    
    def recursive_traverse(self, node):
        if node is None:
            return []
        return self.recursive_traverse(node.left) + [node.data] + self.recursive_traverse(node.right)

   