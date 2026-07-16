# LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        count = [0] * 60
        ans = 0
        for t in time:
            ans += count[-t % 60]
            count[t % 60] += 1
        return ans
