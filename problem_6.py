#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    

def union(llist_1, llist_2):
    # Your Solution Here
    list_ = set()
    current_1 = llist_1.head
    current_2 = llist_2.head
    # traverse and store every value of list 1
    while current_1:
        list_.add(current_1.value)
        current_1 = current_1.next
    # traverse and store every value of list 2
    while current_2:
        list_.add(current_2.value)
        current_2 = current_2.next 
        
    result = LinkedList()
    # append all values of sets into new linked list named result
    
    for i in list_:
        result.append(i)
    return result

def intersection(llist_1, llist_2):
    # Your Solution Here
    current_1 = llist_1.head
    current_2 = llist_2.head
    
    list_1 = set()
    list_2 = set()
    # traverse and store values into set datastructure of every node on each list
    while current_1:
        list_1.add(current_1.value)
        current_1 = current_1.next
    
    while current_2:
        list_2.add(current_2.value)
        current_2 = current_2.next 
        
    result = LinkedList()
    for i in list_1.intersection(list_2):# simply append values into linkedlist that we have discovered in intersection of both lists
        result.append(i)
    return result
    
print("# Test case 1:")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("List a = {} \nList b ={}".format(linked_list_1,linked_list_2))
print ("Union",union(linked_list_1,linked_list_2))
print ("Intersection",intersection(linked_list_1,linked_list_2))

print("\n# Test case 2:")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print("List a = {} \nList b ={}".format(linked_list_3,linked_list_4))
print ("Union",union(linked_list_3,linked_list_4))
print ("Intersection",intersection(linked_list_3,linked_list_4))

print("\n# Test case 3:")
print("List a = {} \nList b ={}".format(linked_list_1,linked_list_4))
print ("Union",union(linked_list_1,linked_list_4))
print ("Intersection",intersection(linked_list_1,linked_list_4))



