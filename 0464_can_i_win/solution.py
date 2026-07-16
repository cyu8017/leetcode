# LeetCode 0464 - Can I Win
# https://leetcode.com/problems/can-i-win/


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total < desiredTotal:
            return False

        memo: dict[int, bool | None] = {}

        def can_win(state: int, current_total: int) -> bool:
            if state in memo:
                return memo[state]
            for pick in range(1, maxChoosableInteger + 1):
                bit = 1 << (pick - 1)
                if state & bit:
                    continue
                if current_total + pick >= desiredTotal:
                    memo[state] = True
                    return True
                if not can_win(state | bit, current_total + pick):
                    memo[state] = True
                    return True
            memo[state] = False
            return False

        return can_win(0, 0)
