'''
    2018/11/09
    Isomorphic Strings: https://leetcode.com/problems/isomorphic-strings/
'''

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for i,c in enumerate(s):
            if c in dict:
                if dict[c] != t[i]:
                    return False
            elif t[i] in list(dict.values()):
                return False
            else:
                dict[c] = t[i]
        
        return True