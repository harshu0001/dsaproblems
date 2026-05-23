'''
You are given a 0-indexed 2D integer matrix grid of size n * n with 
values in the range [1, n2]. Each integer appears exactly once except a which appears twice and 
b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

Example 1:

Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
Example 2:

Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
 
'''

#----BRUTE-FORCE METHOD-------

grid = [[9,1,7],[8,9,2],[3,4,6]]
l = list()
ans = list()
for i in grid:
    for j in i:
        l.append(j)

for i in l:
    if l.count(i) == 2:
        ans.append(i)
        break
newlist = set(l)
newlist = list(newlist)
# print(newlist)
n = newlist[len(newlist)-1]

sum = 0
for i in newlist:
    sum+=i
nsum = int((n*(n+1))/2)
# print(nsum)

if sum == nsum:
    ans.append(newlist[len(newlist)-1]+1)

if sum < nsum:
    ans.append(nsum-sum)
print(ans)