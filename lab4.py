class TreeNode:
    """Вузол бінарного дерева"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Бінарне дерево пошуку"""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Додає значення в дерево"""
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
        """Обхід дерева (pre, in, post)"""
        if not node: return []
        if order == "pre": return [node.value] + self.traverse(node.left, order) + self.traverse(node.right, order)
        if order == "in": return self.traverse(node.left, order) + [node.value] + self.traverse(node.right, order)
        if order == "post": return self.traverse(node.left, order) + self.traverse(node.right, order) + [node.value]

    def tree_type(self):
        """Визначення типу дерева"""
        if self.is_perfect(): return "Perfect"
        if self.is_full(): return "Full"
        if self.is_complete(): return "Complete"
        return "Regular"

    def is_full(self, node=None):
        """Перевірка на full tree"""
        if node is None: node = self.root
        if not node: return True  # Виправлено!
        if not node.left and not node.right: return True  # Листок - ок
        if not node.left or not node.right: return False  # Один нащадок - НЕ full tree
        return self.is_full(node.left) and self.is_full(node.right)

    def is_complete(self, node=None, index=0, nodes=None):
        """Перевірка на complete tree"""
        if nodes is None: nodes = self.count_nodes(self.root)
        if node is None: node = self.root
        if not node: return True
        if index >= nodes: return False
        return self.is_complete(node.left, 2*index+1, nodes) and self.is_complete(node.right, 2*index+2, nodes)

    def is_perfect(self):
        """Перевірка на perfect tree"""
        return self.is_full() and self.is_complete()

    def count_nodes(self, node):
        """Підрахунок вузлів"""
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right) if node else 0

# Приклад використання
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
bst = BST()
for v in values:
    bst.insert(v)

print("Tree Type:", bst.tree_type())  # Вивести тип дерева
print("Pre-order:", bst.traverse(bst.root, "pre"))
print("In-order:", bst.traverse(bst.root, "in"))
print("Post-order:", bst.traverse(bst.root, "post"))


def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)