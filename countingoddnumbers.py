low = int(input("Enter the low number:"))
high = int(input("Enter the high number:"))

ans = list()

for i in range(low, high+1):
    if i%2 != 0:
        ans.append(i)


print(len(ans))

