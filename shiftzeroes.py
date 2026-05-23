'''
Given an integer array arr, rearrange the elements so that every occurrence of 0 is shifted to the end of the array. 
The relative order of all non‑zero elements must remain unchanged.

Example 1
Input: arr = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: The three zeros are moved after all other numbers while the order 1, 2, 4, 3, 5 stays the same.

Example 2
Input: arr = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No zeros are present, so the array remains unchanged.
'''

arr = [1, 2, 0, 4,0, 3, 0, 5, 0]
# ----BRUTE-FORCE METHOD-----
# zeros = [x for x in arr if x == 0]
# nozeros = [x for x in arr if x != 0]

# result = nozeros+zeros
# print(result)

# -----TRYING TO OPTIMIZE----

import_pos = 0

for i in arr:
    if i != 0:
        arr[import_pos] = i
        import_pos+=1

while import_pos<len(arr):
    arr[import_pos] = 0
    import_pos+=1

print(arr)










