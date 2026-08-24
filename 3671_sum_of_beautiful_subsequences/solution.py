# LeetCode 3671 - Sum of Beautiful Subsequences
# https://leetcode.com/problems/sum-of-beautiful-subsequences/

from typing import List


class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        MOD = 1000000007
        mx = max(nums)
        pos = [[] for _ in range(mx + 1)]
        for i, v in enumerate(nums):
            pos[v].append(i)
        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            seq = []
            for m in range(g, mx + 1, g):
                seq.extend(pos[m])
            if not seq:
                continue
            seq.sort()
            ways = 1
            for _ in range(len(seq)):
                ways = (ways * 2) % MOD
            cnt[g] = (ways - 1 + MOD) % MOD
        ans = 0
        for g in range(mx, 0, -1):
            for m in range(2 * g, mx + 1, g):
                cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD
            ans = (ans + cnt[g] * g) % MOD
        return ans
