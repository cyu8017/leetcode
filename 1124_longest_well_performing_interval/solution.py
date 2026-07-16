# LeetCode 1124 - Longest Well-Performing Interval
# https://leetcode.com/problems/longest-well-performing-interval/

class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        score = 0
        first_seen: dict[int, int] = {0: -1}
        ans = 0
        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            if score > 0:
                ans = i + 1
            elif score - 1 in first_seen:
                ans = max(ans, i - first_seen[score - 1])
            first_seen.setdefault(score, i)
        return ans
