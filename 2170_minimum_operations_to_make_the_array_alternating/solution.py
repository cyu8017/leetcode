# LeetCode 2170 - Minimum Operations to Make the Array Alternating
# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        def top2(idxs):
            freq = {}
            for i in idxs:
                freq[nums[i]] = (freq.get(nums[i]) or 0) + 1
            a = 0
            ac = 0
            b = 0
            bc = 0
            for v, c in freq.items():
                if c > ac:
                    b = a
                    bc = ac
                    a = v
                    ac = c
                elif c > bc:
                    b = v
                    bc = c
            return [a, ac, b, bc]

        even = []
        odd = []
        for i in range(n):
            (even if i % 2 == 0 else odd).append(i)
        e = top2(even)
        o = top2(odd)
        if e[0] != o[0]:
            return n - e[1] - o[1]
        return min(n - e[1] - o[3], n - e[3] - o[1])
