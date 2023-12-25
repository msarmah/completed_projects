# Question: Implement a Linked List from the Node Class.

from utils import Node, Collections, StaticArray

class LinkedList(Collections):
    def __init__(self, isSet = False, isDoubly = False, isCircular = False):
        # initialize everything
        super(LinkedList,self).__init__()
        self.head = None
        self.size = None
        self.tail = None
        self.isSet = isSet
        self.isDoubly = isDoubly
        self.isCircular = isCircular
        pass
        
        
    def __getitem__(self, index):
        if self.head == None: 
            return None # getting the index with None and return
        
        cur = self.head #initialize
        for i in range(index): #traverse through linked list to find index node
            cur = cur.next
        return cur # return node
##        cur = self.head
##        count = 0
##        while True:
##            if cur == None:
##                break
##            if count == index:
##                return cur
##            cur = cur.next
##            count += 1

    def __setitem__(self, index, value):
        if self.head == None:# nothing in LinkedList
            node = Node(value)
            self.head = node # make added node the head
            self.tail = node # make added node the tail
            if self.isCircular:
                self.next = node # point the next arrow back to the node
            if self.isDoubly:
                self.prev = node # point the previous arrow back to the node

        elif index == 0: #Adding a value in the front
            node = Node(value) #initialize node
            node.next = self.head # connect new node to existing head of list 
            if self.isDoubly:
                self.head.prev = node # old node point to new head
            if self.isCircular:
                node.prev = self.tail # head connects to list's tail
                self.tail.next = node # tail is connected to the new head
            self.head = node # change the previous head to a new node and new node as head
            
        elif index == self.get_size(): #adding to the back
            node = Node(value)
            cur = self.tail #grab last node
            cur.next = node # cur node's next is new node
            self.tail = node # tail points to new node 
            if self.isDoubly:
                node.prev = cur #point new tail to the previous tail
            if self.isCircular:
                node.next = self.head #connect tail to head
                self.head.prev = node # connect head to tail
                
        else: #grab index right before and right after
            node = Node(value)
            
            if index > self.get_size(): # if the index is greater than the size leave it
                return
            
            cur = self.head # initialize
            while index > 1: # loop through to find the index before the node we are trying to add
                cur = cur.next
                index = index - 1

            node.next = cur.next # connect new node to next to current node (connect from front end of insertion)
            cur.next = node # establish link between current node and new node (connect from back end of insertion)
            if self.isDoubly:
                node.next.prev = node # front end
                node.prev = cur # back end 

    def __delitem__(self, index):
        if self.head == None: # if it is already None return
            return
            
        elif index == 0: #deleting from front
            tmp = self.head.next # temporarily store pointer of node we are trying to delete to the next node
            self.head.next = None # remove link between deleting node and node next to it
            self.head = tmp # assign the node next to the deleted node as the head 
            if self.isDoubly:
                self.head.prev = None # cutting connection from new head to old head
            if self.isCircular:
                self.tail.next = self.head # connects tail to new head
                self.head.prev = self.tail # connects new head to tail
                self.head.prev.prev = None # cuts the connection between old head and tail
            
        elif index == self.get_size()-1: #deleting from back
            before_tail = self.head # assign head to varaible
            while before_tail.next != self.tail: # loop through until you hit node before the tail
                before_tail = before_tail.next
            self.tail=before_tail # assign tail to node before the old tail
            if self.isDoubly:
                before_tail.next.prev = None # cuts connection from old tail to new tail
            if self.isCircular:
                self.head.prev = self.tail # connects head to new tail
                self.tail.next = self.head # connects new tail to head
            before_tail.next = None # cuts connection from new tail to old tail
            
        else:
            cur = self.head
            while index > 1: # find index one before index of node you are
                cur = cur.next
                index = index - 1
            # removing cur.next node
            prv = cur
            nxt = cur.next.next
            cur.next.next = None # removing the connection between the node you are trying to delete and next node
            prv.next = nxt # making connection between node before deleting node and node after deleting node
            if self.isDoubly:
                nxt.prev = prv #connect to node before removing node
                cur.next.prev = None # cut connection between deleting node and bode before

    def append(self, value):
        if self.head == None: # appending for empty linked list
            node = Node(value)
            self.head = node # make node the head
            self.tail = node # make node the tail
            if self.isCircular:
                self.next = node # point the next arrow back to node
            if self.isDoubly:
                self.prev = node # point the previous arrow back to node
        else:
            node = Node(value)
            cur = self.tail #grab last node
            cur.next = node # cur node's next is new node
            self.tail = node # tail points to new node 
            if self.isDoubly:
                node.prev = cur #point new tail to the previous tail
            if self.isCircular:
                node.next = self.head #connect tail to head
                self.head.prev = self.tail # connect head to tail
            #self[len(self)] = value 

    def extend(self, arr): #append static array
        if self.isCircular:
            if arr.get_size() == 1: # appending to static array with one value 
                self.append(arr[0])
            else:
                for i in range(arr.get_size()): # appending when there are already values
                    self.append(arr[i])
                    print("test",arr[i])# add one value of static array
                    #while arr.head != arr.tail: # loop through the linked list 
##                    node=arr.head 
                    #arr.head = arr.head.next # move to the next 
                #self.append(arr.tail.data) # last value is the tail
        else:
            for i in range(arr.get_size()):
                self.append(arr[i])
##            while arr.head != None: # loop through the new linked list 
##                node = arr.head
##                self.append(arr.head.data) # add one value of each node of new list 
##                arr.head = arr.head.next # move to next
        

    def remove(self, value):
        cur = self.head # initialize the head
        index = 0
        while cur != None: # while head does not equal None
            if cur.data == value: #value to be removed
                self.__delitem__(index)
                break
            cur = cur.next 
            index += 1

        
    def argwhere(self, value):
       # extension from parent class
        count = 0
        for i,v in enumerate(self):
            if v == value:
                count += 1
        ret = StaticArray(count)
        for i,v in enumerate(self):
            if v == value:
                ret.append(i)
        return ret

    def __len__(self):
        if self.head == None: # length is 0 for empty linked list 
            return 0

        cur = self.head
        count = 0

        while True: # traverse through counts of nodes in linked list
            if cur == None or cur == self.tail: # count the nodes
                count = count + 1
                break
            else: # count the tail
                cur = cur.next
                count += 1
        return count 

        
    def get_size(self):
        return self.__len__() # extension of __len__() function

    def __eq__(self, arr):
        # extension from parent class
        if type(arr) == LinkedList:
            for v1,v2 in zip(self, arr):
                if v1!=v2:
                    return False
            return True
        return False

        pass

    def __repr__(self):
        cur = self.head
        while cur is not None and  cur != self.tail:
            print (cur.data)
            cur = cur.next
        if cur != None:
            print(cur.data)
            
##        cur = self.head
##        while cur is not None and cur!= self.tail:
##            print(cur.data)
##            cur = cur.next
            

    def __iter__(self):
        if self.head == None: # no need to iterate when nothing is there
            yield None
            
        cur = self.head
        while True: # iterate through the linked list
            yield cur
            cur = cur.next
            if cur == None:
                break

        pass

##lis = LinkedList(isCircular=True)
##lis[0]=1
##lis[1]=3
##lis[2]=5
###lis.remove(3)
###lis.__setitem__(2,10);
##lis.__repr__()
##
##ext = StaticArray(3)
##ext[0]=5
##ext[1]=5
##ext[2]=5
##lis.extend(ext)
###print(lis.__repr__())
###print(lis.tail.prev.data)
