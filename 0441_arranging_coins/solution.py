# LeetCode 0441 - Arranging Coins
# https://leetcode.com/problems/arranging-coins/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            mid = (low + high) // 2
            if mid * (mid + 1) // 2 <= n:
                low = mid + 1
            else:
                high = mid - 1
        return high
