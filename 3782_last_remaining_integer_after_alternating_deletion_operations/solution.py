# LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
# https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

class Solution:
    def lastRemaining(self, n: int) -> int:
        first = 1
        step = 2
        left = True
        while n > 1:
            if not left and n % 2 == 0:
                first += step
            n = (n + 1) // 2
            step *= 2
            left = not left
        return first
