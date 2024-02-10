# Binary Search Tree Algorithm

Binary Search Tree (BST) is a fundamental data structure that provides efficient insertion, deletion, and search operations. This implementation includes a specialized extension, `BinarySearchTree_Particular`, designed to solve a specific problem related to managing records (check the problem statemant bellow).

## Overview

The BST is a data structure where each node has at most two children, referred to as the left child and the right child. The left child's key is less than the parent's key, and the right child's key is greater than the parent's key.

## BinarySearchTree Class

### Methods

#### `__init__(self, values=None, other_tree=None)`

- Constructor for the BinarySearchTree class.
- Optional parameters `values` and `other_tree` allow initialization with values or by copying another tree.

#### `insert(self, key)`

- Inserts a key into the Binary Search Tree.

#### `delete(self, key)`

- Deletes a node with the specified key from the Binary Search Tree.

#### `search(self, key)`

- Searches for a node with the specified key in the Binary Search Tree.

#### `preorder(self)`, `inorder(self)`, `postorder(self)`

- Performs a print in pre-order, in-order, and post-order traversals of the Binary Search Tree, respectively.

#### `breadth_first_traversal(self)`

- Performs a breadth-first traversal of the Binary Search Tree.

#### `find_min(self, node)`

- Finds the node with the minimum key in the given subtree.

#### `destructor(self, node)`, `delete_tree(self)`

- Destructor methods for the BinarySearchTree class.

## Problem Statement

The specialized extension, `BinarySearchTree_Particular`, addresses a specific problem related to record management where each record has a unique key (CPF - Cadastro de Pessoas Físicas) and position in a linear data structure. The `BinarySearchTree_Particular` class allows efficient management of records by associating positions with keys.

## Usage Example

```python
from binary_search_tree import BinarySearchTree, BinarySearchTree_Particular

# Create BinarySearchTree instance
bst = BinarySearchTree()

# Insert keys into the tree
bst.insert(50)
bst.insert(30)
bst.insert(70)
# ...

# Perform a search
result = bst.search(30)
print("Search Result:", result)

# Delete a node
bst.delete(50)

# Print tree in-order
bst.inorder()
