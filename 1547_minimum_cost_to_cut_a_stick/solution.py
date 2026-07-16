# LeetCode 1547

class Solution:
    def minCost(self, n, cuts):
        points = [0] + sorted(cuts) + [n]
        size = len(points)
        dp = [[0] * size for _ in range(size)]
        for width in range(2, size):
            for left in range(size - width):
                right = left + width
                dp[left][right] = min((dp[left][mid] + dp[mid][right] for mid in range(left + 1, right)), default=0)
                if right > left + 1:
                    dp[left][right] += points[right] - points[left]
        return dp[0][-1]
