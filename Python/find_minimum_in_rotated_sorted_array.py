"""
    2018/08/04
    Find Minimum in Rotated Sorted Array: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minn = nums[0]
        for num in nums:
            if num < minn:
                minn = num
                break
        
        return minn
