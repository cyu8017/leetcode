class Solution:
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        dp = [1.0] + [0.0] * target
        for p in prob:
            for heads in range(target, -1, -1):
                dp[heads] = dp[heads] * (1 - p) + (dp[heads - 1] * p if heads else 0)
        return dp[target]
