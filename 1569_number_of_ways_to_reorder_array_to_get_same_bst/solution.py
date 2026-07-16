from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        choose = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            choose[i][0] = choose[i][i] = 1
            for j in range(1, i):
                choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % MOD
        def ways(values):
            if len(values) < 3:
                return 1
            left = [x for x in values[1:] if x < values[0]]
            right = [x for x in values[1:] if x > values[0]]
            return choose[len(values) - 1][len(left)] * ways(left) * ways(right) % MOD
        return (ways(nums) - 1) % MOD
