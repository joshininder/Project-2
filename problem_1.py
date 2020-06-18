#!/usr/bin/env python
# coding: utf-8

# In[40]:


from collections import deque
class LRU_Cache:
    def __init__(self, cache_size = 3):# By default size of my cache table would be 3
        self.cache_size = cache_size
        self.key_value_dict = dict()
        self.queue = deque()
        
    def set(self, key,value):
        search = self.get(key,value)
        if search == -1:
            if len(self.queue) >= self.cache_size :
                least_recently_used_page = self.queue.popleft()
                del self.key_value_dict[least_recently_used_page]
            
            self.queue.append(key)
            self.key_value_dict[key] = value
        print("After set operation set({},{}) queue is {}".format(key, value,self.key_value_dict))
                
    def get(self,key, value = None):
        ''' returns -1 if key is not present there else return the value specified at the key '''
        if key in self.key_value_dict:
            result = self.key_value_dict[key]
            del self.key_value_dict[key]
            self.queue.remove(key)
            if value is None:
                self.key_value_dict[key] = result
                print("After get operation get({}) value = {} and updated queue is {}".format(key, result,self.key_value_dict))
            else : 
                self.key_value_dict[key] = value
            self.queue.append(key)
            return result
        return -1
    
    def print_cache(self):
        return  "Queue = {}".format(self.key_value_dict)

print("\n First test case \n")
test_case_1 = LRU_Cache(5)
test_case_1.set(1, 1)# 1,1 -> None
test_case_1.set(2, 2)# 1,1 -> 2,2 -> None
test_case_1.set(3, 3)# 1,1 -> 2,2 -> 3,3 -> None
test_case_1.set(4, 4)# 1,1 -> 2,2 -> 3,3-> 4,4 ->  None
test_case_1.set(5, 5)# 1,1 -> 2,2 -> 3,3 -> 4,4 -> 5,5None
test_case_1.set(6, 6)# 2,2 -> 3,3 -> 4,4 -> 5,5 -> 6,6 -> None
test_case_1.get(1)       # returns -1 and queue is unchanged
test_case_1.get(2)       # returns 2 and update queue to 3,3 -> 4,4 -> 5,5 -> 6,6 -> 2,2
test_case_1.get(9)      # returns -1 because 9 is not present in the cache
print("queue - ",test_case_1.print_cache())


print("\n Second test case \n")
test_case_2 = LRU_Cache(3)
test_case_2.set(1, 1); # 1,1 -> Null
test_case_2.set(2, 2);# 1,1 -> 2,2 -> Null
test_case_2.set(1,2);# 2,2 -> 1,2 -> Null
test_case_2.set(3,2);# 2,2 -> 1,2 -> 3,2 -> NUll
test_case_2.set(4,1) # 1,2 -> 3,2 -> 4,1 ->Null
test_case_2.get(3) # return 2 and set 1,2-> 4,1 -> 3,2
test_case_2.get(10) # return -1 and queue unchanged
test_case_2.print_cache()

print("\n Third test case \n")
test_case_3 = LRU_Cache(3)
test_case_3.set('a','b');# a,b -> Null
test_case_3.set('a','c');# a,c -> Null
test_case_3.set('b', 2);# a,c -> b,2 -> Null
test_case_3.set('c', 3);# a,c -> b,2 -> c,3-> NUll
test_case_3.get('a') # return d and set b,2 -> c,3 -> a,c
test_case_3.get('c') # return 3 and set b,2 -> a,c -> c,3
print("queue -", test_case_3.print_cache())

print("\n Fourth test case \n")
our_cache=LRU_Cache(3)
our_cache.set(1,1) # 1,1 
our_cache.set(2,2) # 1,1->2,2
our_cache.set(3,3) # 1,1 -> 2,2 -> 3,3
our_cache.set(4,4) # 2,2 -> 3,3 -> 4,4
our_cache.get(4)   # Expected Value = 4 and queue unchanged as the most recently used page is 4 only
our_cache.get(1)   # Expected Value = -1 and queue unchangedbecause page is not present
our_cache.set(2,4) # 3,3 -> 4,4 -> 2,4
our_cache.get(2)   # Expected Value = 4 and queue unchanged as the most recently used page is 2 only
our_cache.set(5,5) # 4,4 -> 2,4 -> 5,5
our_cache.get(3)   # Expected Value = -1 and queue unchanged
our_cache.get(5)   # Expected Value = 5 and queue unchanged as the most recently used page is 5 only
our_cache.set(2,6) # 4,4 -> 5,5 -> 2,6
our_cache.get(2)   # Expected Value = 6 and queue unchanged as the most recently used page is 2 only
our_cache.set(6,6) # 5,5 -> 2,6 -> 6,6
our_cache.get(4)   # Expected Value = -1 and queue unchanged because page is not present
our_cache.get(6)   # Expected Value = 6 and queue unchanged as the most recently used page is 6 only
our_cache.set(5,10)#  2,6 -> 6,6 -> 5,10
our_cache.set(7,7) # 6,6 -> 5,10 -> 7,7
our_cache.get(2)   # Expected Value = -1 and queue unchanged because page is not present
our_cache.get(7)   # Expected Value = 7 and queue unchanged as the most recently used page is 7 only
our_cache.get(6)   # Expected Value = 6 and queue updated to 5,10 -> 7,7 ->6,6
our_cache.get(5)   # Expected Value = 10 and queue updated to 7,7 -> 6,6 -> 5,10
our_cache.get(5)   # Expected Value = 10 and queue unchanged because page is not present
our_cache.set(8,8) # 6,6->5,10->8,8
our_cache.get(6)   # return 6 and queue updated to 5,10->8,8->6,6
our_cache.get(5)   # return 10 and queue updated to 8,8 -> 6,6 -> 5,10
print(our_cache.get(7)) # Output = -1 as our cache dont contain key = 7
print(our_cache.print_cache()) # print 8,8 -> 6,6 -> 5,10




