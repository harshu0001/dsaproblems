'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
'''
chars = ['?', ',', "'","!", '"', ".", " ", ' ']
s="Was it a car or a cat I saw?"
cleanS = ''.join(char for char in s if char.isalnum())
sub = cleanS.lower()
l1 = list(sub)
l2 = l1.copy()
l2.reverse()
if l1 == l2:
    print("true")
else:
    print("false")



