# Question: From Static Array class implement a Dynamic Array
from utils import StaticArray

class DynamicArray(StaticArray):
    def __init__(self, size, isSet = False):
        super(DynamicArray,self).__init__(size)
        self.isSet = isSet #initialize set property 
        #pass
        
##    def __getitem__(self, index):
##        pass

    def __setitem__(self, index, value):
        # set the set property
        if self.isSet:
            for i in self:
                if i == value:
                    return

        # adding a new value into array (shifting)

        if self[index] == None: #if the index has a None value already
            for i, v in enumerate(self): 
                if v == None:
                    super().__setitem__(i,value) #set the new value to the index that had None 
                    break
        else: # shift values from left to right left to right (from where deleting is happening)
            for i in range(self.get_size()-1, index,-1):
                super().__setitem__(i, self[i-1])
            super().__setitem__(index,value)

        if len(self)>0.8*self.get_size(): # resizing bigger double
            self.reallocate(self.get_size()*2)
        

    def __delitem__(self, index):
        if self[index] == None: #deleting item that is already None
            return
        elif index == self.size-1: # deleting at the end of the array 
            del super[index]
        else: # shift values from right to left from index (the place the deleting happens)
            for i in range(index, self.get_size()-1):
                super().__setitem__(i, self[i+1])
            super().__setitem__(self.get_size()-1,None)
            
        if len(self)<0.2*self.get_size(): #resizing smaller 1/2
            self.reallocate(self.get_size()//2)
            
            

    def append(self, value): #append values at the end of the array using size 
        self[self.size-1]=value

##    def remove(self, value):
##        pass
##
##    def argwhere(self, value):
##        pass
##
##    def __len__(self):
##        pass
##
##    def get_size(self):
##        pass

    def __eq__(self, arr):
        # check if Dynamic Array equal to Static Array
        # make copy of equal from parent class and edit
        if type(arr) == DynamicArray:
            for v1,v2 in zip(self, arr):
                if v1!=v2:
                    return False
            return True
        return False

##    def __repr__(self):
##        pass #Not required but useful for debugging
##
##    def __iter__(self):
##        pass

    def reallocate(self, size): #allows for resizing by making a clone and extending the array
        clone = self.copy() 
        self.resize(size)
        self.extend(clone)

    def resize(self, size):
        """
        Do not modify this function.
        This function will enable you to resize your structure.
        This function is destructive! Be careful.
        """
        self.data = [None]*size
        self.size = size
