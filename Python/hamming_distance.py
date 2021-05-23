'''
    2018/07/31
    Hamming Distance: https://leetcode.com/problems/hamming-distance/description/
'''

# === First Approach ===  
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        length = max([len(bin_x),len(bin_y)])
        bin_x = bin_x.zfill(length)
        bin_y = bin_y.zfill(length)
        ans = 0
        for i in range(length):
            if bin_x[i] != bin_y[i]:
                ans += 1
        
        return ans

# === Second Approach ===     
# class Solution:
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         ans = bin(x ^ y)[2:].count('1')
        
#         return ans
