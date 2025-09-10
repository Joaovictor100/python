

class Node:
    def __init__(self, data):
        self.node = data
        self._left = None
        self._right = None

    def __str__(self):
        return str(self.node)


class BinaryTree:
    def __init__(self, raiz):
        self.raiz = Node(raiz)
        

arvore = BinaryTree('A')
