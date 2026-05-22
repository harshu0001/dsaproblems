'''
Valid Anagram
Easy
Topics
Company Tags
Hints
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
'''

#-----BRUTE-FORCE METHOD------
# s = "racecar"
# t = "carrace"

# out = []
# t_list = list(t)
# for i in s:
#     if i in t_list:
#         out.append("true")
#         t_list.remove(i)
#     else:
#         out.append("false")
# if "false" in out or len(s) != len(t):
#     print("False")
# else:
#     print("True")
    
#-----HASHMAP METHOD------

s = "racecar"
t = "carrace"

map_s = {}
map_t = {}

if len(s) != len(t):
    print("False")

for char in s:
    map_s[char] = map_s.get(char, 0)

for char in t:
    map_t[char] = map_t.get(char, 0)

for key in map_s:
    if map_s[key] != map_t.get(key, 0):
        print("False")
    else:
        print("True")
