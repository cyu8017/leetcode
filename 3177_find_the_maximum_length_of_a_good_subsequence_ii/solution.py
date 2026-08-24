# LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[0] * (k + 1) for _ in range(n)]
        mp = [{} for _ in range(k + 1)]
        g = [[0, 0, 0] for _ in range(k + 1)]
        ans = 0
        for i in range(n):
            for h in range(k + 1):
                f[i][h] = mp[h].get(nums[i], 0)
                if h > 0:
                    if g[h - 1][0] != nums[i]:
                        f[i][h] = max(f[i][h], g[h - 1][1])
                    else:
                        f[i][h] = max(f[i][h], g[h - 1][2])
                f[i][h] += 1
                mp[h][nums[i]] = max(mp[h].get(nums[i], 0), f[i][h])
                if g[h][0] != nums[i]:
                    if f[i][h] >= g[h][1]:
                        g[h][2] = g[h][1]
                        g[h][1] = f[i][h]
                        g[h][0] = nums[i]
                    elif f[i][h] > g[h][2]:
                        g[h][2] = f[i][h]
                elif f[i][h] > g[h][1]:
                    g[h][1] = f[i][h]
                ans = max(ans, f[i][h])
        return ans
