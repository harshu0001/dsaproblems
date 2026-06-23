l = [1,2,3,4,1,1,3,2,4,4,4]
newset = set()
count = 0
n = len(l)
for i in l:
    newset.add(i)

for i in range(0,n):
    if l[i] in newset:
        count+=1
    print({l[i]: count})

