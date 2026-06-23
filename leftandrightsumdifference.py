nums = [10,4,8,3]
leftsum = [0]
rightsum = []
ans = list()

for i in range(1, len(nums)):
    n = sum(nums[0:i])
    leftsum.append(n) #--> Left sum compiled


for i in range(0, len(nums)):
    n = sum(nums[i+1: len(nums)])
    rightsum.append(n)

for i in range(0, len(nums)):
    n = abs(leftsum[i] - rightsum[i])
    ans.append(n)

print(ans)

