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
s = "racecar"
t = "carrace"

out = []
t_list = list(t)
for i in s:
    if i in t_list:
        out.append("true")
        t_list.remove(i)
    else:
        out.append("false")
if "false" in out or len(s) != len(t):
    print("False")
else:
    print("True")
    
