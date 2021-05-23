'''
    2019/12/28
    Reverse Words in a String: https://leetcode.com/problems/reverse-words-in-a-string/
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
