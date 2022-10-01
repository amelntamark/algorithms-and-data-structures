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
    
    def find(self, key):
        current = self.root

        while current:
            if current.key == key:
                return current.value
            elif current.key > key:
                current = current.right
            elif current.key < key:
                current = current.left

        if current:
            return current.value
        else:
            return None