'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''


strs = ["act","pots","tops","cat","stop","hat"]
newlist = []

for i in strs:
    new = list(i)
    new.sort()
    newlist.append(new)
print(newlist)
sublist = list()

# for i in range(len(newlist)):
        
# x = ["a", "c", "t"]
# y = "".join(x)
# print(y)
# print(type(y))
