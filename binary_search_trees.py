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

# Working search method (iterative)
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

# Working search method (recursive)
    def find_helper(self, current, key):
        # Base case: current key matches key or current key is None
        if not current:
            return None
        elif current.key == key:
            return current.value
        # Recursive case: current key does not match key
        elif current.key > key:
            return(self.find_helper(current.left, key))
        else: # current.key is less than key
            return(self.find_helper(current.right, key))

    def find_recursively(self, key):
        return self.find_helper(self.root, key)


# Working insertion method (iterative)
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

            if not self.root:
                self.root = new_node
                return
            else:
                self.add_recursively_helper(self.root, new_node)
            
# Working delete method (recursive) (by Ada Developer's Academy)

# If the right or left subtree of node we want to delete is empty:
#   Have it's parent node point to it's child
# If node to delete has both left and right children
#   Find the minimum node in the right subtree
#   Have node to be deleted's parent point to min node in right subtree (smallest node on right tree because 
#       it should be greater than first node of left tree, but smaller than other nodes of right tree)

    def min_node(self, node):
        while node.left:
            node = node.left
        return node.key, node.value

    def delete_helper(self, current, key):
        # If key is less than current key, recur down left side of tree
        if key < current.key:
            current.left = self.delete_helper(current.left, key)
        # If key is greater than current key, recur down right side of tree
        elif key > current.key:
            current.right = self.delete_helper(current.right, key)
        # Base case: key is to be deleted
        else: 
            # if node has no left subtree
            if not current.left:
                return current.right # this node's new parent will be the parent of the node being deleted
            # if node has no right subtree
            elif not current.right:
                return current.left # this node's new parent will be the parent of the node being deleted
            # if node has both left and right subtree
            else:
                current.key, current.value = self.min_node(current.right) # replace node to be deleted with min node in right subtree
                current.right = self.delete_helper(current.right, current.key) # delete the min node in the right subtree that has just changed places
        return current
    
    def delete(self, key):
        if not self.root:
            return

        self.root = self.delete_helper(self.root, key)

    # Working height finder (recursive) (by Ada Developer's Academy)
    def height_helper(self, current):
        # base case – node is None
        if not current:
            return 0

        # recursive case – at least one subtree to search
        return 1 + max(self.height_helper(current.right), self.height_helper(current.left))
    
    def height(self):
        return self.height_helper(self.root)
        
