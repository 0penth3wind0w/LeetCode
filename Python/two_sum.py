'''
    2018/07/27
    Two Sum: https://leetcode.com/problems/two-sum/description/
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_num = sorted(nums)
        candidates = [None, None]
        for i,j in enumerate(sorted_num):
            if (target-j) in sorted_num[i+1:]:
                candidates = [j, target-j]
                break
        
        return sorted([i for i,j in enumerate(nums) if j == candidates[0]]) if candidates[0] == candidates[1] else sorted([nums.index(i) for i in candidates])
