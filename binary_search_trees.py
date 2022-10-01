class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

# Working search method (iterative) (by me)
    def find(self, key):
        current = self.root

        while current:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            elif current.key > key:
                current = current.left

        return None

# Working insertion method (iterative) (by me)
    def add(self, key, value = None):
        current = self.root
        new_node = TreeNode(key, value)
        
        if current == None:
            self.root = new_node
            return
        
        while current:
            if key >= current.key:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right
            elif key < current.key:
                if not current.left:
                    current.left = new_node
                    return
                current = current.left

# Working insertion method (recursive)
    def add_recursively_helper(self, current, new_node):
            # Base case: root is none
            if not current:
                self.root = new_node
                return

            # Recursive case: not a leaf
            if new_node.key >= current.key:
                if not current.right: # Base case: leaf found
                    current.right = new_node
                    return
                else:
                    self.add_recursively_helper(current.right, new_node)
            if new_node.key < current.key:
                if not current.left:
                    current.left = new_node
                    return
                else:
                    self.add_recursively_helper(current.left, new_node)

    def add_recursively(self, key, value = None):
            new_node = TreeNode(key, value)
            self.add_recursively_helper(self.root, new_node)
            return
