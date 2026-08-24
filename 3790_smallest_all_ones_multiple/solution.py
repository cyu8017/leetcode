# LeetCode 3790 - Smallest All Ones Multiple
# https://leetcode.com/problems/smallest-all-ones-multiple/

class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if (k & 1) == 0:
            return -1
        x = 1 % k
        ans = 1
        for _ in range(k):
            x = (x * 10 + 1) % k
            ans += 1
            if x == 0:
                return ans
        return -1
