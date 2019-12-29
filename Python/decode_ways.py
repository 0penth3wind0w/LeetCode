'''
2019/12/29

Decode Ways: https://leetcode.com/problems/decode-ways/
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        rev_s = s[::-1]
        result = [1]
        for i, n in enumerate(rev_s):
            if i==0:
                result.append(self.single_handler(int(n)))
            else:
                single = self.single_handler(int(n)) * result[-1]
                double = self.double_handler(int(n+rev_s[i-1])) * result[-2]
                result.append(single+double)
        return result[-1]

    def single_handler(self, n: int) -> int:
        if n==0:
            return 0
        return 1
    
    def double_handler(self, n: int) -> int:
        if n>26 or n<10:
            return 0
        return 1