# LeetCode 0390 - Elimination Game
# https://leetcode.com/problems/elimination-game/


class Solution:
    def lastRemaining(self, n: int) -> int:
        left = 1
        right = n
        step = 1
        remaining = n
        from_left = True

        while left < right:
            if from_left or remaining % 2 == 1:
                left += step
            right -= step
            step *= 2
            remaining //= 2
            from_left = not from_left

        return left
