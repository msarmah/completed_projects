# Question: From BinaryTree create a Binary Search Tree.

from utils import BinaryTree, TreeNode
    
class BST(BinaryTree):
    def __init__(self, arr, sort = False):
        super().__init__()
        self.sort = sort
        if len(arr) > 0 and self.sort == False: # when sort is false
            for n in arr:
                self.addNode(n) # add node one at a time
        elif len(arr) > 0 and self.sort == True: # when sort is true
            self.addNode(arr) # add node like BST
            
    def addNode(self, data):
        if self.root is None and isinstance(data, list) == False:
            self.root = TreeNode(data) #first time call, so create a node - this is the root at the beginning
            return # we create the root 
        else:
            if self.sort == True and data is not None and isinstance(data, list) == True:
                data.sort()
                # print('data', data)
                self.create_balanced_bst(data) # add using balanced bst 
            else: # is not sorted 
                self.insertNode(self.root, data)

    #recursive method to insert in a binary tree
    def insertNode(self, root, data):
        if root.data == data:
            return # duplicate, so simply return
        elif data < root.data:
            if root.less: #subtree is not empty
                self.insertNode(root.less, data)
                return
            else: #subtree is empty
                root.less = TreeNode(data)
                return
                
        else: # for data > self.root.data 
            if root.more: #subtree is not empty
                self.insertNode(root.more, data)
                return
            else: #subtree is empty
                root.more = TreeNode(data)
                return
                
    def create_balanced_bst(self, nums):  
        #print('create_balanced_bst', nums)
        if not nums:
            return None # ends here
        
        mid_val = len(nums)//2 # find the mid value
        
        node = TreeNode(nums[mid_val]) # node is the mid value
        
        if self.root is None:
            self.root = node # root is a node

        # change until we find proper center
        node.less = self.create_balanced_bst(nums[:mid_val])
        node.more = self.create_balanced_bst(nums[mid_val+1:])
        
        return node

    def removeNode(self,data):
        # use delte method call 
        self.delete_Node(self.root, data)
    
    
    def delete_Node(self, node, data):
        
        #if root doesn't exist, just return it     
        if node is None: 
            return None
        
        if node.data == data: 
            # Leaf node
            if node.less is None and node.more is None:
                return None
            
            # Only right child exists
            if node.less is None:
                return node.more

            # Only left child exists
            elif node.more is None:
                return node.less

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            tmp = node.more
            while tmp.less:
                tmp = tmp.less;
                        

            # Copy the min node's
            # content to this node
            node.data = tmp.data

            # Delete the node that we just copy
            node.more = self.delete_Node(node.more, tmp.data)
        
        # Find the node in the left subtree if data is less than root data
        elif node.data > data: 
            node.less = self.delete_Node(node.less, data)
        
        # Find the node in right subtree if data  is greater than root data, 
        else: #elif node.data < data: 
            node.more = self.delete_Node(node.more, data)
        
        return node

    def search(self, data):
        # use exists method call
        return self.exists(self.root, data)
    
    # recurrsive method to search     
    def exists(self, root, data):

        # exists at the root 
        if root.data == data:
            return True          
        
        elif data < root.data: # to the left of root
            if root.less is None:
                return False # there is no value there
            else:
                return self.exists(root.less, data) # it exists
        else: # to the right of node
            if root.more is None:
                return False # there is no value there
            else:
                return self.exists(root.more, data) # it exists
                        
    def tolist(self):
        vals = []
        #print('tolist', self.root.data)
        self.inorder(self.root, vals) # puts the nodes in order
        return vals
    
    #recurssive method to inorder traversing of binary tree
    def inorder(self, root, vals):
        if root is not None: # it has leaves
            if root.less is not None: # 
                self.inorder(root.less, vals) # there exists smaller values so put in order
            if root.data is not None: 
                vals.append(root.data) # there exists a leaf so add it
            if root.more is not None:
                self.inorder(root.more, vals) # there exists larger values so put in order
        return vals
            
    def height(self, data):

        node = self.root
        while node is not None: #Using while loop to search the node.     
            #print(data, node.data)
            # accumulating the node.less and node.more for depth method call
            if data < node.data: 
                node = node.less 
            elif data > node.data:
                node = node.more
            else:
                #node.data == data: found the node               
                break
                
        return self.depth(node)
        
    def depth(self, node):
        if node is None: # only the root
            return 0
        
        leftHeight  = self.depth(node.less) # smaller values on the left 
        rightHeight = self.depth(node.more) # larger values on the right 
        max_height= leftHeight 
        
        if rightHeight > max_height: # when right is greater than left 
            max_height = rightHeight # we use right height
        return max_height+1 # and add 1 for the new leaf
    
    def balancefactor(self, data):
        node = self.root
        while node is not None: #Using while loop to search the node.     
            #print(data, node.data)
            # accumulating the node.less and node.more for depth method call
            if data < node.data:
                node = node.less 
            elif data > node.data:
                node = node.more
            else:
                #node.data == data: found the node               
                break
                
        return self.heightDiffBetweenLeftAndRight(node)
    
    def heightDiffBetweenLeftAndRight(self, node):
        # Base condition
        if node is None:
            return True
 
        # for left and right subtree height
        left_height  = self.depth(node.less)
        right_height = self.depth(node.more)
        
        return abs(left_height - right_height) # the difference in heights 
        
