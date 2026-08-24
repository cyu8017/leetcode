# LeetCode 2928 - Distribute Candies Among Children I
# https://leetcode.com/problems/distribute-candies-among-children-i/


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                k = n - i - j
                if 0 <= k <= limit:
                    ans += 1
        return ans
