# LeetCode 2345 - Finding the Number of Visible Mountains
# https://leetcode.com/problems/finding-the-number-of-visible-mountains/

from typing import List


class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        arr = [[p[0] - p[1], p[0] + p[1]] for p in peaks]
        arr.sort(key=lambda a: (a[0], -a[1]))
        ans = 0
        max_r = float("-inf")
        i = 0
        while i < len(arr):
            j = i
            while j < len(arr) and arr[j][0] == arr[i][0] and arr[j][1] == arr[i][1]:
                j += 1
            if arr[i][1] > max_r:
                if j - i == 1:
                    ans += 1
                max_r = arr[i][1]
            i = j
        return ans
