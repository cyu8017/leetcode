# LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

from typing import List


class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def bit_count(x: int) -> int:
            c = 0
            v = x
            while v:
                c += v & 1
                v >>= 1
            return c

        def depth(x: int) -> int:
            v = x
            if v == 1:
                return 0
            d = 0
            while v > 1:
                v = bit_count(v)
                d += 1
            return d

        a = nums[:]
        ans = []
        for q in queries:
            if q[0] == 1:
                l, r, k = q[1], q[2], q[3]
                cnt = 0
                for i in range(l, r + 1):
                    if depth(a[i]) == k:
                        cnt += 1
                ans.append(cnt)
            else:
                a[q[1]] = q[2]
        return ans
