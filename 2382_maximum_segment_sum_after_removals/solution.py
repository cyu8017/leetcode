# LeetCode 2382 - Maximum Segment Sum After Removals
# https://leetcode.com/problems/maximum-segment-sum-after-removals/

from typing import List


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = list(range(n))
        ssum = [0] * n
        active = [False] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            parent[rb] = ra
            ssum[ra] += ssum[rb]

        ans = [0] * n
        best = 0
        for i in range(n - 1, -1, -1):
            ans[i] = best
            idx = removeQueries[i]
            active[idx] = True
            ssum[idx] = nums[idx]
            if idx > 0 and active[idx - 1]:
                unite(idx, idx - 1)
            if idx + 1 < n and active[idx + 1]:
                unite(idx, idx + 1)
            best = max(best, ssum[find(idx)])
        return ans
