class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

def pre_order(tree):
    visited_nodes=[]
    root=tree.get_root()
    def traverse(node):
        if node:
            visited_nodes.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child())
    traverse(root)
    return visited_nodes

pre_order(tree)

def in_order(tree):
    visited_nodes=[]
    root=tree.get_root()
    def in_order_traverse(node):
        if node:
            in_order_traverse(node.get_left_child())
            visited_nodes.append(node.get_value())
            in_order_traverse(node.get_right_child())
    in_order_traverse(root)
    return visited_nodes

in_order(tree)

def post_order(tree):
    visited_nodes=[]
    root=tree.get_root()
    def post_order_traverse(node):
        if node:
            post_order_traverse(node.get_left_child())
            post_order_traverse(node.get_right_child())
            visited_nodes.append(node.get_value())
    post_order_traverse(root)
    return visited_nodes

post_order(tree)
