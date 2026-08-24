# LeetCode 2951 - Find the Peaks
# https://leetcode.com/problems/find-the-peaks/

from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                ans.append(i)
        return ans
