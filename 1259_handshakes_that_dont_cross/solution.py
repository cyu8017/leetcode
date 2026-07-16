class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        mod = 1_000_000_007
        dp = [0] * (numPeople + 1)
        dp[0] = 1
        for people in range(2, numPeople + 1, 2):
            dp[people] = sum(dp[left] * dp[people - 2 - left] for left in range(0, people, 2)) % mod
        return dp[numPeople]
