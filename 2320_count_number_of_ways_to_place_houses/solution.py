# LeetCode 2320 - Count Number of Ways to Place Houses
# https://leetcode.com/problems/count-number-of-ways-to-place-houses/


class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 1000000007
        a = b = 1
        for _ in range(n):
            na = (a + b) % mod
            b = a
            a = na
        ways = (a + b) % mod
        return ways * ways % mod
