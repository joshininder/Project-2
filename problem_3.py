import heapq
import sys

def cal_freq (data):
    '''
    The function is to calculate the frequency of characters in string.
    
    params: 
        data (str) : inputted string
    
    returns:
        sorted_dictionary : Dictionary containing character as key and its frequency as value.
    
    '''
    dictionary = dict()
    for i in data:
        if i not in dictionary:
            dictionary[i] = data.count(i)
    '''
    source for sorting method - 
    https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
    '''
    sorted_dictionary = [[k, v] for k, v in sorted(dictionary.items(), key=lambda item: item[1])]
    return sorted_dictionary
    


def huffman_encoding(data):
    '''
    The function is to encode the data .
    
    params: 
        data (str) : data which needs to be encoded
    
    returns:
        orginal_data (str) : encoded data
    
    '''
    frequencies = cal_freq(data) # frequencies are calculated.
    # create a list which will store priority , then list containning letter and ''
    # here I have used '' just for appending 0,1 or we can say it will contain encoding of the character 
    heap = [[priority,[letter,'']] for letter, priority in frequencies ]
    
    heapq.heapify(heap) # transform list into heap
    
    encoded_string = "" # encoded data

    if len(heap) ==  1:
        encoded_string = "".join(['0' for x in range(len(data))])
        tree = {data[0]: '0'}
    else:
        while len(heap) > 1: # base condition -  if your heap contains one node then return because we have got our tree 
            first_node = heapq.heappop(heap) # pop out first node
            second_node = heapq.heappop(heap) # pop out second node. Here second node is used in context with the above pop operation.
            
            for value in first_node[1:]: # add 0 as it the left node 
                value[1] = '0' + value[1] 
            
            for value in second_node[1:]: # add 0 as it the right node 
                value[1] = '1'+ value[1]
            
            new_priority = first_node[0] + second_node[0] # Add priorities
            heapq.heappush(heap ,[new_priority]+first_node[1:]+ second_node[1:]) # append new priority with first and second as left and right nodes
        
        value = heapq.heappop(heap)[1:] # pop up char with code
        
        tree = {x : y for x, y in value}
        for i in data : # perform encoding using tree 
            encoded_string += tree[i]
        
    return encoded_string, tree

def huffman_decoding(data,tree):
    '''
    The function is to find the original data out of the coded string.
    
    params: 
        data (str) : data which is encoded
        tree (dict) : it contains charcter as key and its code as value
    
    returns:
        orginal_data (str) : return the orginal data
    
    '''
    tree = { y:x for x, y in tree.items() }# changed character, code to code , character
    print("this ",tree)
    current = '' 
    original_data = "" # original data
    previous = ''
    print(f'Character with code {tree}')
    for idx,i in enumerate(data):
        current += i # update current code
        if idx == len(data)-1 :# if this is last index then update the original data
            if current in tree:
                original_data += tree[current]
            else:
                original_data += tree[previous]
                original_data += tree[current[-1]]
        elif current not in tree and previous in tree: # if my current data is not tree then add character at previous-key in tree

            original_data += tree[previous] 
            current =  i
        previous = current
    return original_data

#-------------------------------------------------------------------------------------------------------#
a_great_sentence = "I loved Data Structure and Algorithm Nanodegree Program. I learned so many things and it helped me in recursion."

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format("aaaaaaaa"))

encoded_data, tree = huffman_encoding("aaaaaaaa")

#print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))
print("#-------------------------------------------------------------------------------------------------------#")
#-------------------------------------------------------------------------------------------------------#
a_great_sentence = "Stay united. Together we'll fight covid-19."

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))
print("#-------------------------------------------------------------------------------------------------------#")
#--------------------------------------------------------------------------------------------------------#

a_great_sentence = "I think someone is playing Jumanji."

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))
print("#-------------------------------------------------------------------------------------------------------#")
#-------------------------------------------------------------------------------------------------------#
a_great_sentence = "abaababababa"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))
#-------------------------------------------------------------------------------------------------------#
