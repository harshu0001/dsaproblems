'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

'''
#Brute force approch

# def hasDuplicates(nums):
#     if(len(set(nums)) == len(nums)):
#         return False
#     else:
#         return True
    

# nums = [1,2,3,3]
# print(hasDuplicates(nums))

## --------HASHMAP or HASHSET METHOD----------------

nums = [1,2,3,4]

hashset = set()

for i in nums:
    if i in hashset:
        print("True")
    hashset.add(i)

if len(hashset) == len(nums):
    print("No duplicates")

    