'''
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.

Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters in word are 'a', 'b', and 'c'.

Example 2:
Input: word = "abc"
Output: 0
Explanation:
No character in word appears in uppercase.
'''
w = "aaAbBcC"

l = list()
count = 0

for i in w:
    if i.islower():
        l.append(i)
    
newl = list(set(l))
print(newl)

for i in newl:
    if chr(ord(i)-32) in w:
        count+=1
    
print(count)







