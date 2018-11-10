'''
    2018/11/04
    Letter Combinations of a Phone Number: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        results = [""]
        for digit in digits:
            results = [ result+alphabet for result in results for alphabet in num_map[digit]]
        
        if results[0]=="":
            del results[0]

        return results