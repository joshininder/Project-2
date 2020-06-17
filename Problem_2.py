#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if len(os.listdir(path)) == 0:
        return []
    if suffix == '':
        return []
    
    items = os.listdir(path)# It works like ls command on linux terminal
    
    required_files = [x for x in items if x.endswith(suffix)]# Storing everything having suffix as specified during method call
    folders = [x for x in items if '.' not in x]# stores every folder in the path specified in parameter during call
    
    for folder in folders:# look for every folder in folder
        required_files.extend(find_files(suffix,path+folder+'\\'))#look into every folder and then append the results
            
    return required_files  
            
    

print("Test case 1 : tell every files which have .c extension in testdir \n{}".format(find_files(suffix='.c', path=os.getcwd()+'\\testdir\\')))

print("Test case 2 : tell every files which have .h extension in subdir1 \n{}".format(find_files(suffix='.h', path=os.getcwd()+'\\testdir\\subdir1')))
print("Test case 3 : tell every files which have 1 suffix in testdir \n{}".format(find_files(suffix='1', path=os.getcwd()+'\\testdir\\')))




