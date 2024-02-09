from bst import TreeNode, BinarySearchTree

class TreeNode_Particular(TreeNode):
    def __init__(self, key, position):
        self.key = key
        self.position = position
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.key < other.key


class BinarySearchTree_Particular(BinarySearchTree):
    def insert_recursive(self, key, position, node):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode_Particular(key, position)
            else:
                self.insert_recursive(key, position, node.left)

        elif key > node.key:
            if node.right is None:
                node.right = TreeNode_Particular(key, position)
            else:
                self.insert_recursive(key, position, node.right)

    def insert(self, key, position):
        if self.root is None:
            self.root = TreeNode_Particular(key, position)
        else:
            self.insert_recursive(key, position, self.root)

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

            min_right_subtree = self.find_min(node.right)
            node.key, node.position = min_right_subtree.key, min_right_subtree.position
            node.right = self.delete_node(node.key, node.right)
        return node

    def delete(self, key):
        self.root = self.delete_node(key, self.root)

    def search_position_recursive(self, key, node):
        if node is None:
            return None
        if key == node.key:
            return node.position
        elif key < node.key:
            return self.search_position_recursive(key, node.left)
        else:
            return self.search_position_recursive(key, node.right)

    def search_position(self, key):
        return self.search_position_recursive(key, self.root)


class Record:
    def __init__(self, cpf, name, dob):
        self.cpf = cpf
        self.name = name
        self.dob = dob # date of birthday

    def __str__(self):
        return f"CPF: {self.cpf}, Name: {self.name}, DoB: {self.dob}"


class FileAccess:
    def __init__(self):
        self.records = []
        self.bst = BinarySearchTree_Particular()

    def insert_record(self, record):
        position = len(self.records)
        self.records.append(record)
        self.bst.insert(record.cpf, position)

    def delete_record(self, cpf):
        position = self.bst.search_position(cpf)
        if position is not None:
            # Actually remove the record from the list
            self.records[position] = None
            # Remove the key from the BST
            self.bst.delete(cpf)

    def search_record(self, cpf):
        position = self.bst.search_position(cpf)
        if position is not None and self.records[position] is not None:
            return self.records[position]
        return None

    def print_ordered_records(self):
        ordered_positions = self.inorder_traversal_positions(self.bst.root)
        for position in ordered_positions:
            if self.records[position] is not None:
                print(self.records[position])

    def inorder_traversal_positions(self, node, skip_position=None):
        if node is None:
            return []

        left_positions = self.inorder_traversal_positions(node.left, skip_position)

        # Skip the deleted node's position
        if node.position != skip_position:
            current_position = node.position

        right_positions = self.inorder_traversal_positions(node.right, skip_position)

        if node.position != skip_position:
            return left_positions + [current_position] + right_positions


def main():
    file_access = FileAccess()
    
    # Insert some records
    file_access.insert_record(Record("790", "Bob Smith", "1985-10-20"))
    file_access.insert_record(Record("123", "John Doe", "2000-01-01"))
    file_access.insert_record(Record("456", "Jane Doe", "1990-05-15"))
    file_access.insert_record(Record("987", "Alice Johnson", "1988-07-30"))
    file_access.insert_record(Record("654", "David Williams", "1975-12-05"))
    file_access.insert_record(Record("321", "Emily Brown", "1995-03-22"))
    file_access.insert_record(Record("555", "Michael Davis", "1982-09-12"))
    file_access.insert_record(Record("888", "Sophia Wilson", "1998-11-18"))
    file_access.insert_record(Record("222", "Oliver Taylor", "1970-04-25"))
    file_access.insert_record(Record("444", "Isabella Moore", "1992-08-08"))
    file_access.insert_record(Record("777", "Ethan Martinez", "1987-06-15"))
    file_access.insert_record(Record("666", "Ava Anderson", "1978-02-28"))
    file_access.insert_record(Record("333", "Mia Garcia", "1993-07-10"))
    file_access.insert_record(Record("111", "Jackson Brown", "2005-09-03"))
    file_access.insert_record(Record("999", "Emma Harris", "1980-12-14"))
    file_access.insert_record(Record("876", "William Clark", "1991-01-08"))
    file_access.insert_record(Record("234", "Madison Turner", "1973-06-20"))
    file_access.insert_record(Record("789", "Liam Turner", "1997-04-01"))
    file_access.insert_record(Record("345", "Abigail Hill", "1989-03-17"))
    file_access.insert_record(Record("567", "Henry Green", "1983-11-27"))
    
    # Test search
    print("Search some records:")
    for cpf in [456, 555, 345, 220, 789, 110]:
        result = file_access.search_record(str(cpf))
        if result:  print(f"Record with CPF {cpf} found:", "---", result)
        else:       print(f"Record with CPF {cpf} not found")
        print("\n")
        
        # Test organize / print all records
        print("Organize records in order:")
        file_access.print_ordered_records()
        print("\n")
        
        # Test delete
        result = file_access.search_record("222")
        if result:      print("Record with CPF 222 found:", "---", result)
        else:           print("Record with CPF 222 not found")
        
        print("Delete record with CPF=222 and try search it:")
        file_access.delete_record("222")
        result = file_access.search_record("222")
        if result:      print("Record with CPF 222 found:", "---", result)
        else:           print("Record with CPF 222 not found")
        print("\n")
        
        # Print all records after delete
        print("Records in order:")
        file_access.print_ordered_records()
        print("\n")

if __name__ == "__main__":
    main()