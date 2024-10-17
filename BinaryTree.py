class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def pre_order(self, node):
        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value)

    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current_node = queue.pop(0) 
            print(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def search(self, value):
        if not self.root:
            return "Tree is empty"
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node.value == value:
                return "Found"
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return "Not found"

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if not current_node.left:
                current_node.left = new_node
                return "Node inserted successfully"
            else:
                queue.append(current_node.left)
            if not current_node.right:
                current_node.right = new_node
                return "Node inserted successfully"
            else:
                queue.append(current_node.right)

    def delete(self, value):
        if not self.root:
            return "Tree is empty"
        queue = [self.root]
        node_to_delete = None
        last_node = None
        while queue:
            current_node = queue.pop(0)
            if current_node.value == value:
                node_to_delete = current_node
            last_node = current_node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        if node_to_delete:
            node_to_delete.value = last_node.value
            self._delete_deepest(last_node)
            return "Node deleted successfully"
        return "Node not found"

    def delete_deepest(self, deep_node):
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node.left == deep_node:
                current_node.left = None
                return
            elif current_node.left:
                queue.append(current_node.left)
            if current_node.right == deep_node:
                current_node.right = None
                return
            elif current_node.right:
                queue.append(current_node.right)

    def delete_tree(self):
        self.root = None
        return "Tree deleted successfully"

