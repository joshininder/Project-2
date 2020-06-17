
import hashlib
from datetime import datetime
'''reference - https://thispointer.com/python-how-to-get-current-date-and-time-or-timestamp/'''
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None # pointing to next block
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


# In[2]:


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        if self.head == None:
            self.head = Block(datetime.now(),data,0)
            self.tail = self.head
        else:
            new_block = Block(datetime.now(),data,self.tail.hash)
            self.tail.next = new_block
            self.tail = new_block
            
    def print_hash(self):
        current = self.head
        while current:
            # I have printed values at first 8 indices of sha.
            
            print("Time Stamp : {}\n Data: {}\n SHA : {} Previous SHA : {}\n".format(current.timestamp,current.data,str(current.hash)[:8],str(current.previous_hash)[:8]))
            current = current.next
        if(self.head == None):
            print("Nothing is stored")
#----------------------------------Test Case 1---------------------------#
print("#----------------------------------Test Case 1---------------------------#")
l = LinkedList()
l.append("Hello")
l.append("world")
l.append("Hello World !")
l.print_hash()

#----------------------------------Test Case 2---------------------------#
print("#----------------------------------Test Case 2---------------------------#")
l = LinkedList()
l.print_hash()

#----------------------------------Test Case 3---------------------------#
print("#----------------------------------Test Case 3---------------------------#")
l = LinkedList()
l.append("Stay Safe")
l.append("From")
l.append("Coronavirus")
l.print_hash()

#----------------------------------Test Case 4---------------------------#
print("#----------------------------------Test Case 4---------------------------#")
l = LinkedList()
l.append("6738937039409709217094790317")
l.append("xvvyg%")
l.append("something which has no meaning")
l.print_hash()



