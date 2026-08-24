# LeetCode 3043 - Find the Length of the Longest Common Prefix
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s = set()
        for x0 in arr1:
            x = x0
            while x > 0:
                s.add(x)
                x = x // 10
        mx = 0
        for x0 in arr2:
            x = x0
            while x > 0:
                if x in s:
                    mx = max(mx, x)
                    break
                x = x // 10
        return len(str(mx)) if mx > 0 else 0
