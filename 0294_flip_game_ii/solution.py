# LeetCode 0294 - Flip Game II
# https://leetcode.com/problems/flip-game-ii/

from functools import lru_cache


class Solution:
    def canWin(self, currentState: str) -> bool:
        @lru_cache(maxsize=None)
        def can_win(state: str) -> bool:
            for index in range(len(state) - 1):
                if state[index : index + 2] == "++":
                    next_state = state[:index] + "--" + state[index + 2 :]
                    if not can_win(next_state):
                        return True
            return False

        return can_win(currentState)
