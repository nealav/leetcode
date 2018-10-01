class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
    
    def __repr__(self):
        return str(self.val)

class BST(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if val is None:
            return
        if self.root is None:
            self.root = Node(val)
            return self.root
        else:
            return self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val <= node.val:
            if node.left is None:
                node.left = self._insert(node.left, val)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = self._insert(node.right, val)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, val)

    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.left)
        print(node, end=' ')
        self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        pass
    
    def post_order_traversal(self, node):
        pass

    def row_by_row_traversal(self):
        level = []
        level.append(self.root)
        while level:
            children = []
            print(' '.join(str(level)))
            for node in level:
                if node.left is not None: children.append(node.left)
                if node.right is not None: children.append(node.right)
            level = children

def main():
    tree = BST()
    tree.insert(5)
    tree.insert(1)
    tree.insert(2)
    tree.insert(8)
    tree.insert(10)
    tree.insert(0)
    tree.insert(6)
    tree.in_order_traversal(tree.root)
    print()
    tree.row_by_row_traversal()

if __name__ == '__main__':
    main()