# LeetCode 1155 - Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            new = [0] * (target + 1)
            for s in range(target + 1):
                if not dp[s]:
                    continue
                for face in range(1, k + 1):
                    if s + face <= target:
                        new[s + face] = (new[s + face] + dp[s]) % MOD
            dp = new
        return dp[target]
