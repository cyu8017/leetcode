# LeetCode 0956 - Tallest Billboard
# https://leetcode.com/problems/tallest-billboard/

class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            for diff, taller in list(dp.items()):
                dp[diff + rod] = max(dp.get(diff + rod, 0), taller + rod)
                nd = abs(diff - rod)
                dp[nd] = max(dp.get(nd, 0), taller if diff >= rod else taller - diff + rod)
        return dp.get(0, 0)
