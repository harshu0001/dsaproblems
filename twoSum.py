'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
'''

# BRUTE-FORCE METHOD

nums = [5,5]
target = 10
n = len(nums)

for i in range(n):
    for j in range(i+1, n):
        if nums[i]+nums[j] == target:
            print([i,j])

# HASHMAP Method - I'll use this once I learn this : )

    
