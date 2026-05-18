'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

'''
def hasDuplicates(nums):
    if(len(set(nums)) == len(nums)):
        return False
    else:
        return True
    

nums = [1,2,3,3]
print(hasDuplicates(nums))

    
