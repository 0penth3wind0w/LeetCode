"""
    2025/05/04
    Number of Equivalent Domino Pairs: https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
"""

# === First Approach ===
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_count = dict()
        for d in dominoes:
            key = str(sorted(d))
            if key in domino_count:
                domino_count[key] += 1
            else:
                domino_count[key] = 1
        result = 0
        for val in domino_count.values():
            if val > 1:
                result += int(val * (val - 1) / 2)
        return result
    
# === Second Approach ===

# use extra container type
from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_counter = Counter(tuple(sorted(d)) for d in dominoes)
        result = 0
        for val in domino_counter.values():
            result += val * (val - 1) // 2 if val > 1 else 0
        return result
