# LeetCode 1176 - Diet Plan Performance
# https://leetcode.com/problems/diet-plan-performance/

class Solution:
    def dietPlanPerformance(self, calories: list[int], k: int, lower: int, upper: int) -> int:
        window = sum(calories[:k])
        ans = 0
        if window < lower:
            ans -= 1
        elif window > upper:
            ans += 1
        for i in range(k, len(calories)):
            window += calories[i] - calories[i - k]
            if window < lower:
                ans -= 1
            elif window > upper:
                ans += 1
        return ans
