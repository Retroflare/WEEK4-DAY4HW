class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, current_node):
        if data < current_node.data:
            if not current_node.left:
                current_node.left = BSTNode(data)
            else:
                self._insert_recursive(data, current_node.left)
        else:
            if not current_node.right:
                current_node.right = BSTNode(data)
            else:
                self._insert_recursive(data, current_node.right)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursive(self.root, result)
        return result

    def _in_order_traversal_recursive(self, current_node, result):
        if current_node:
            self._in_order_traversal_recursive(current_node.left, result)
            result.append(current_node.data)
            self._in_order_traversal_recursive(current_node.right, result)