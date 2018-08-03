'''
    2018/08/03
    Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = 0
        length = 0
        clist = []
        for c in s:
            if c in clist:
                clist = clist[clist.index(c)+1:]
                clist.append(c)
                length = len(clist)
            else:
                clist.append(c)
                length += 1
                if length > maximum:
                    maximum = length
        
        return maximum
