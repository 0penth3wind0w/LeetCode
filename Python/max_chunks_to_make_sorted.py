'''
    2018/07/31
    Max Chunks To Make Sorted: https://leetcode.com/problems/max-chunks-to-make-sorted/description/
'''

class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        last = len(arr)-1
        index = 0
        lastpos = 0
        while index <= last:
            if arr[index] == index:
                #print(arr[lastpos:index+1])
                ans += 1
                index += 1
                lastpos = index
            elif arr[index] > index:
                index = arr[index]
            else: #arr[index] < index
                if max(arr[lastpos:index+1]) == index:
                    #print(arr[lastpos:index+1])
                    ans += 1
                    index += 1
                    lastpos = index
                elif max(arr[lastpos:index+1]) > index:
                    index = max(arr[lastpos:index+1])
        
        return ans
