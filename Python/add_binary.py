"""
    2019/05/07
    Add Binary: https://leetcode.com/problems/add-binary/
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxl = max(len(a),len(b))
        a ,b = a.zfill(maxl), b.zfill(maxl)
        
        result = ''
        carry = False
        
        i = maxl - 1
        while i >= 0:
            if a[i] != b[i]:
                if carry:
                    result = '0' + result
                else:
                    result = '1' + result
            else:
                if carry:
                    result = '1' + result
                else:
                    result = '0' + result
                carry = True if a[i] == '1' else False
            i -= 1
        if carry:
            result = '1' + result
            
        return result
