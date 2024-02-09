class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.key < other.key


class BinarySearchTree:
    def __init__(self, values=None, other_tree=None):
        self.root = None
        if values is not None:
            for value in values:
                self.insert(value)
        if other_tree is not None:
            self.root = self.copy_tree(other_tree.root)

    def copy_tree(self, node):
        if node is None:
            return None
        new_node = TreeNode(node.key)
        new_node.left = self.copy_tree(node.left)
        new_node.right = self.copy_tree(node.right)
        return new_node

    def insert_recursive(self, key, node):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self.insert_recursive(key, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self.insert_recursive(key, node.right)

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self.insert_recursive(key, self.root)

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete_node(self, key, node):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete_node(key, node.left)
        elif key > node.key:
            node.right = self.delete_node(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self.find_min(node.right).key
            node.right = self.delete_node(node.key, node.right)

        return node

    def delete(self, key):
        self.root = self.delete_node(key, self.root)

    def destructor(self, node):
        if node is not None:
            self.destructor(node.left)
            self.destructor(node.right)
            del node

    def delete_tree(self):
        self.destructor(self.root)
        self.root = None

    def preorder_traversal(self, node):
        if node is not None:
            print(node.key, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def preorder(self):
        self.preorder_traversal(self.root)
        print()

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)

    def inorder(self):
        self.inorder_traversal(self.root)
        print()

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=' ')

    def postorder(self):
        self.postorder_traversal(self.root)
        print()

    def breadth_first_traversal(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.key, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()