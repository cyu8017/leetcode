# LeetCode 1885 - Count Pairs in Two Arrays
# https://leetcode.com/problems/count-pairs-in-two-arrays/

import bisect
from typing import List


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sorted(a - b for a, b in zip(nums1, nums2))
        answer = 0
        n = len(diff)

        for i in range(n):
            target = -diff[i]
            answer += len(diff) - bisect.bisect_right(diff, target, lo=i + 1)

        return answer
