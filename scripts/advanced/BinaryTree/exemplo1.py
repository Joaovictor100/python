

class Node:
    def __init__(self, data):
        self.node = data
        _self.left = None
        _self.right = None

    def __str__(self):
        return str(self.node)


class BinaryTree:
    def __init__(self, raiz):
        self.raiz = Node(raiz)
        

arvore = BinaryTree('A')
