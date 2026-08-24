# LeetCode 3141 - Maximum Hamming Distances
# https://leetcode.com/problems/maximum-hamming-distances/

from typing import List


class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        dist = [-1] * (1 << m)
        q = []
        for x in nums:
            dist[x] = 0
            q.append(x)
        k = 1
        while q:
            t = []
            for x in q:
                for i in range(m):
                    y = x ^ (1 << i)
                    if dist[y] == -1:
                        dist[y] = k
                        t.append(y)
            q = t
            k += 1
        ans = list(nums)
        for i in range(len(ans)):
            x = ans[i]
            ans[i] = m - dist[x ^ ((1 << m) - 1)]
        return ans
