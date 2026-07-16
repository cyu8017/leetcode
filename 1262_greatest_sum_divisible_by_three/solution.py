from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        impossible = -10**18
        dp = [0, impossible, impossible]
        for value in nums:
            old = dp[:]
            for total in old:
                if total != impossible:
                    remainder = (total + value) % 3
                    dp[remainder] = max(dp[remainder], total + value)
        return dp[0]
