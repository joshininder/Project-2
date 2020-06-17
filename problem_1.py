# class Node is a derived data structure which I have used to store  key, values
from collections import deque
class LRU_Cache:
    def __init__(self, cache_size = 3):# By default size of my cache table would be 3
        print(cache_size)
        self.cache_size = cache_size
        self.key_value_dict = dict()
        self.queue = deque()
        
    def set(self, key,value):
        if self.get(key) != -1:
            self.queue.remove(key)
            del self.key_value_dict[key]
        elif len(self.queue) >= self.cache_size :
            least_recently_used_page = self.queue.popleft()
            del self.key_value_dict[least_recently_used_page]
        self.queue.append(key)
        self.key_value_dict[key] = value
        print(self.key_value_dict)
        
                
    def get(self,key = None):
        ''' returns -1 if key is not present there else return the value specified at the key '''
        if key == None:
            return -1
        result = self.key_value_dict.get(key,-1)
        return result
    
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

test_case_1.get(1)       # returns -1
test_case_1.get(2)       # returns 2
test_case_1.get(9)      # returns -1 because 9 is not present in the cache

print("queue - ",test_case_1.print_cache())


print("\n Second test case \n")
test_case_2 = LRU_Cache(3)

test_case_2.set(1, 1); # 1,1 -> Null
test_case_2.set(2, 2);# 1,1 -> 2,2 -> Null
test_case_2.set(1,2);# 2,2 -> 1,2 -> Null
test_case_2.set(3,2);# 2,2 -> 1,2 -> 3,2 -> NUll
test_case_2.set(4,1) # 1,2 -> 3,2 -> 4,1 ->Null

test_case_2.get(1) # return 2
test_case_2.get(10) # return -1
print("Queue - {}".format(test_case_2.print_cache()))

print("\n Third test case \n")
test_case_3 = LRU_Cache(3)

test_case_3.set('a','b');# a,b -> Null
test_case_3.set('a','c');# a,c -> Null
test_case_3.set('b', 2);# a,c -> b,2 -> Null
test_case_3.set('c', 3);# a,c -> b,2 -> c,3-> NUll

test_case_3.get('a') # return d
test_case_3.get('c') # return 3
test_case_3.get() # return -1
print("queue -", test_case_3.print_cache())

our_cache=LRU_Cache(3)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)
our_cache.get(4)   # Expected Value = 4
our_cache.get(1)   # Expected Value = -1
our_cache.set(2,4)
our_cache.get(2)   # Expected Value = 4
our_cache.set(5,5)
our_cache.get(3)   # Expected Value = -1
our_cache.get(5)   # Expected Value = 5
our_cache.set(2,6)
our_cache.get(2)   # Expected Value = 6
our_cache.set(6,6)
our_cache.get(4)   # Expected Value = -1
our_cache.get(6)   # Expected Value = 6
our_cache.set(5,10)
our_cache.set(7,7)
our_cache.get(2)   # Expected Value = -1
our_cache.get(7)   # Expected Value = 7
our_cache.get(6)   # Expected Value = 6
our_cache.get(5)   # Expected Value = 10
our_cache.get(5)   # Expected Value = 10
our_cache.set(8,8)
print(our_cache.get(7))   # Expected Value = -1 Your Output = 7
