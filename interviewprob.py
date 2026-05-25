s = "cbacdcbc"
l = list(s)
l.sort()

newlist = list()
for i in l:
    if i not in newlist:
        newlist.append(i)

print(min(['abcd', 'acdb']))
