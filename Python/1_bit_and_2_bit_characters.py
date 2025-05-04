"""
    2018/08/06
    1-bit and 2-bit Characters: https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
"""

# === First Approach ===  
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        index = len(bits)-1
        i = 0
        while i < index-1 and index > 1:
            if bits[i] == 0: # one bit
                i += 1
            else: # two bits
                i += 2
        
        return True if bits[i] == 0 else False

# === Second Approach ===  
# class Solution:
#     def isOneBitCharacter(self, bits):
#         """
#         :type bits: List[int]
#         :rtype: bool
#         """
#         while len(bits) > 2:
#             if bits[0] == 0: # one bit
#                 bits = bits[1:]
#             else: # two bits
#                 bits = bits[2:]
        
#         return True if bits[0] == 0 else False
