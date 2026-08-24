# LeetCode 3100 - Water Bottles II
# https://leetcode.com/problems/water-bottles-ii/


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            numExchange += 1
            ans += 1
            numBottles += 1
        return ans
