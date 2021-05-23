'''
    2018/08/06
    Majority Element: https://leetcode.com/problems/majority-element/description/
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        elements = list(set(nums))
        counts = [nums.count(x) for x in elements]
        idx = [counts.index(c) for c in counts if c > total/2][0]
        
        return elements[idx]
