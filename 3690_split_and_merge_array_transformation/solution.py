# LeetCode 3690 - Split and Merge Array Transformation
# https://leetcode.com/problems/split-and-merge-array-transformation/

from typing import List, Tuple


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        def to_arr(nums: List[int]) -> Tuple[int, ...]:
            t = [0] * 6
            for i in range(n):
                t[i] = nums[i]
            return tuple(t)

        start = to_arr(nums1)
        target = to_arr(nums2)
        vis = {start}
        q = [start]
        ans = 0
        while True:
            nq = []
            for cur in q:
                if cur == target:
                    return ans
                for l in range(n):
                    for r in range(l, n):
                        remain = list(cur[:l]) + list(cur[r + 1 : n])
                        sub = list(cur[l : r + 1])
                        for pos in range(len(remain) + 1):
                            nxt_slice = remain[:pos] + sub + remain[pos:]
                            nxt = to_arr(nxt_slice)
                            if nxt not in vis:
                                vis.add(nxt)
                                nq.append(nxt)
            q = nq
            ans += 1
