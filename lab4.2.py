class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def pre_order(self, node, result):
        if node:
            result.append(node.value)
            self.pre_order(node.left, result)
            self.pre_order(node.right, result)
        return result

    def in_order(self, node, result):
        if node:
            self.in_order(node.left, result)
            result.append(node.value)
            self.in_order(node.right, result)
        return result

    def post_order(self, node, result):
        if node:
            self.post_order(node.left, result)
            self.post_order(node.right, result)
            result.append(node.value)
        return result

    def is_full(self, node=None):
        if node is None:
            node = self.root
        if not node:
            return True
        if (node.left is None and node.right is None):
            return True
        if (node.left is not None and node.right is not None):
            return self.is_full(node.left) and self.is_full(node.right)
        return False

    def is_complete(self, node, index, node_count):
        if node is None:
            return True
        if index >= node_count:
            return False
        return (self.is_complete(node.left, 2 * index + 1, node_count) and
                self.is_complete(node.right, 2 * index + 2, node_count))

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def is_perfect(self):
        node_count = self.count_nodes(self.root)
        return self.is_complete(self.root, 0, node_count) and self.is_full()

    def tree_type(self):
        if self.is_perfect():
            return "Perfect"
        elif self.is_full():
            return "Full"
        elif self.is_complete(self.root, 0, self.count_nodes(self.root)):
            return "Complete"
        else:
            return "Regular"
        


values = [6, 11, 3, 7, 4, 5, 19, 18, 13]
bst = BinarySearchTree()

for val in values:
    bst.insert(val)

print("Tree Type:", bst.tree_type())
print("Pre-order:", bst.pre_order(bst.root, []))
print("In-order:", bst.in_order(bst.root, []))
print("Post-order:", bst.post_order(bst.root, []))


