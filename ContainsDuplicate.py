''' 
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

#O(N)

def containDuplicates(nums): 
    dic = {} 
    
    for i in nums: 
        if i not in dic: 
            dic[i] = i
        else: 
            return True 
    return False 
            
s = [2,7,11,2] #True 
d = [0] #false 
print(containDuplicates(s))        