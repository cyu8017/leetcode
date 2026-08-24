# LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
# https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/


class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        used = set()
        total = 0
        x = 1
        while len(used) < n:
            if (k - x) not in used:
                used.add(x)
                total += x
            x += 1
        return total
