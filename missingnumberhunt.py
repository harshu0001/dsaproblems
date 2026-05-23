'''
Missing Number Hunt

Given an integer array arr of length n - 1 that contains distinct numbers taken from the range [1, n], exactly one number from this range is absent. The task is to identify and return the missing integer.

Input: An array arr of size n‑1 with distinct values, each between 1 and n inclusive.
Output: The single integer from 1 to n that does not appear in arr.

Example
Input: arr = [5, 1, 3, 4]
Output: 2
Explanation: The numbers should be 1 through 5. The array lacks the value 2, so the answer is 2.
'''
arr = [9,7,6,5,4,3,2,1,8]
sum = 0
arr.sort()

n = arr[len(arr)-1]
nsum = (n*(n+1))/2
for i in arr:
    sum+=i

if sum == nsum:
    print(n+1)
else:
    print(int(nsum-sum))