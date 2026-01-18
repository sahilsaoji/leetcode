class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.frontPointer = 0 
        self.rearPointer = -1
        self.size = 0 
        self.capacity = k
        self.mylist = [None] * k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        #Check if full
        if self.size == self.capacity:
            return False

        #Move RearPointer
        self.rearPointer = (self.rearPointer + 1) % self.capacity

        #and then add the value
        self.mylist[self.rearPointer] = value

        #increment
        self.size += 1

        return True
            

    def deQueue(self):
        """
        :rtype: bool
        """
        #Check if empty
        if self.size == 0:
            return False

        # have to do this first and then remove the value
        self.mylist[self.frontPointer] = None

        #Move frontPointer
        self.frontPointer = (self.frontPointer + 1) % self.capacity



        #decrement
        self.size -= 1

        return True

        

    def Front(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.mylist[self.frontPointer]

        

    def Rear(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        return self.mylist[self.rearPointer]

        
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True
        return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.size == self.capacity:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()