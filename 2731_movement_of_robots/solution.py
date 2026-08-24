# LeetCode 2731 - Movement of Robots
# https://leetcode.com/problems/movement-of-robots/

from typing import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 1000000007
        n = len(nums)
        pos = [nums[i] + (d if s[i] == "R" else -d) for i in range(n)]
        pos.sort()
        ans, pref = 0, 0
        for i in range(n):
            ans = (ans + ((pos[i] * i - pref) % MOD + MOD) % MOD) % MOD
            pref += pos[i]
        return (ans % MOD + MOD) % MOD
