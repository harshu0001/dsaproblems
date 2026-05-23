
arr= [1, 4, 3, 2, 6, 5]
rev_arr = list()
n = len(arr)
for i in range(n-1, -1, -1):
    rev_arr.append(arr[i])

print(rev_arr)