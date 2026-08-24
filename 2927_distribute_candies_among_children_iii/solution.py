# LeetCode 2927 - Distribute Candies Among Children III
# https://leetcode.com/problems/distribute-candies-among-children-iii/


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(x: int) -> int:
            if x < 2:
                return 0
            return x * (x - 1) // 2

        ans = comb(n + 2)
        ans -= 3 * comb(n - limit + 1)
        ans += 3 * comb(n - 2 * (limit + 1) + 2)
        ans -= comb(n - 3 * (limit + 1) + 2)
        if ans < 0:
            ans = 0
        return ans
