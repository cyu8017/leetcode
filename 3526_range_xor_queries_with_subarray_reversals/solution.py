# LeetCode 3526 - Range XOR Queries with Subarray Reversals
# https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

from typing import List


class Solution:
    def getResults(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        a = nums[:]
        ans = []

        def at(i: int) -> int:
            return a[i] if 0 <= i < len(a) else 0

        def set_at(i: int, val: int) -> None:
            if i < 0:
                return
            while len(a) <= i:
                a.append(0)
            a[i] = val

        for q in queries:
            typ = q[0]
            if typ == 1:
                l, r = q[1], q[2]
                while l < r:
                    left, right = at(l), at(r)
                    set_at(l, right)
                    set_at(r, left)
                    l += 1
                    r -= 1
            elif typ == 2:
                x = 0
                for i in range(q[1], q[2] + 1):
                    x ^= at(i)
                ans.append(x)
            else:
                set_at(q[1], q[2])
        return ans
