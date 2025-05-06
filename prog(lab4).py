class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if not node:
            return TreeNode(value)
        if value <= node.value:
            node.left = self._insert_rec(node.left, value)
        else:
            node.right = self._insert_rec(node.right, value)
        return node

    def traverse(self, node, order):
        if not node:
            return []
        if order == "pre":
            return [node.value] + self.traverse(node.left, order) + self.traverse(node.right, order)
        if order == "in":
            return self.traverse(node.left, order) + [node.value] + self.traverse(node.right, order)
        if order == "post":
            return self.traverse(node.left, order) + self.traverse(node.right, order) + [node.value]

    def tree_type(self):
        if self.is_perfect():
            return "Perfect"
        if self.is_full():
            return "Full"
        if self.is_complete():
            return "Complete"
        return "Regular"

    def is_full(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return True
        if not node.left and not node.right:
            return True
        if not node.left or not node.right:
            return False
        return self.is_full(node.left) and self.is_full(node.right)

    def is_complete(self, node=None, index=0, nodes=None):
        if nodes is None:
            nodes = self.count_nodes(self.root)
        if node is None:
            node = self.root
        if not node:
            return True
        if index >= nodes:
            return False
        return self.is_complete(node.left, 2*index+1, nodes) and self.is_complete(node.right, 2*index+2, nodes)

    def is_perfect(self):
        return self.is_full() and self.is_complete()

    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
bst = BST()
for v in values:
    bst.insert(v)

print("Tree Type:", bst.tree_type())
print("Pre-order:", bst.traverse(bst.root, "pre"))
print("In-order:", bst.traverse(bst.root, "in"))
print("Post-order:", bst.traverse(bst.root, "post"))
