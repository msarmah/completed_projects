# Question: Using DynamicCollection and LinkedList implement Stacks and Queues.
from utils import *
from arrays import *
from linkedlist import *

class StackOrQueue():
    def __init__(self, useLinkedList = False, isQueue=False):
        self.useLinkedList = useLinkedList
        if self.useLinkedList:
            self.data = LinkedList() #for queue
        else:
            self.data = DynamicArray(10) # for stack
        self.isQueue = isQueue # say isQueue exists

    def peek(self):
        if self.isQueue:
            return self.data[0]
        else:
            return self.data[len(self.data)-1]#stack

    def push(self, value): #inserting values
        if self.isQueue:
            self.data.append(value) # makes a linked list (from initializing in the init)
        else:
            self.data.append(value) # into linked list or dynamic array 


    def pop(self):
        if self.isQueue:
            val = self.data[0]
            del self.data[0]
            return val
        else:
            val = self.data[len(self.data)-1]
            del self.data[len(self.data)-1]
            return val      
    
    def __repr__(self):
        pass #Not graded but useful for debugging

##print("queue")
##c = StackOrQueue(isQueue = True, useLinkedList = True)
##c.push(1)
##c.push(2)
##c.push(3)
##print(c.peek())
