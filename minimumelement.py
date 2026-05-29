'''
You are given an integer array nums.
You replace each element in nums with the sum of its digits.
Return the minimum element in nums after all replacements.

Example 1:
Input: nums = [10,12,13,14]
Output: 1

Explanation:
nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.
'''
nums = [10,12,13,14]

nums2 = list()
sums = list()
for i in nums:
    nums2.append(str(i))
print(nums2)

for i in nums2:
    sums.append(sum(int(x) for x in i))
sums.sort()
print(sums)
print(sums[0])


