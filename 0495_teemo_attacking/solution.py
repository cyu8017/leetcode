# LeetCode 0495 - Teemo Attacking
# https://leetcode.com/problems/teemo-attacking/

class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total = duration
        for index in range(1, len(timeSeries)):
            total += min(duration, timeSeries[index] - timeSeries[index - 1])
        return total
