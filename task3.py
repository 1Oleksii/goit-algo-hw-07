# Клас вузла дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Клас двійкового дерева пошуку
class BST:
    def __init__(self):
        self.root = None

    # Додавання нового значення
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = Node(value)

# Функція для обчислення суми всіх значень у дереві
def sum_tree(node):
    if node is None:
        return 0
    # Сума поточного значення + сума в лівому піддереві + сума в правому піддереві
    return node.value + sum_tree(node.left) + sum_tree(node.right)

# Тестовий приклад
if __name__ == "__main__":
    tree = BST()
    for value in [10, 5, 20, 3, 7, 15, 30]:
        tree.insert(value)
    print("Сума всіх значень:", sum_tree(tree.root))  # Очікується: 100
