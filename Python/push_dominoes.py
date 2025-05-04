"""
    2025/05/04
    Push Dominoes: https://leetcode.com/problems/push-dominoes/description/
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        last_index = len(dominoes) -1
        if last_index == 0:
            return dominoes
        state = list(dominoes)
        while True:
            changed = False
            prevoius = None
            # check the prevoius and the next domino to decide falling direction
            # only need to consider standing dominos
            for i, d in enumerate(state):
                if d == '.':
                    if i != 0 and i != last_index:
                        if prevoius == 'R' and state[i + 1] != 'L':
                            prevoius = state[i]
                            state[i] = 'R'
                            changed = True
                            continue
                        if state[i + 1] == 'L' and prevoius != 'R':
                            prevoius = state[i]
                            state[i] = 'L'
                            changed = True
                            continue
                    if i == 0 and state[1] == 'L':
                        prevoius = state[0]
                        state[0] = 'L'
                        changed = True
                        continue
                    if i == last_index and prevoius == 'R':
                        prevoius = state[last_index]
                        state[i] = 'R'
                        changed = True
                        continue
                prevoius = d
            if not changed:
                return ''.join(state)