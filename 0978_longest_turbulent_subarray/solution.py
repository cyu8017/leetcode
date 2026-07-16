# LeetCode 0978 - Longest Turbulent Subarray
# https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        ans = cur = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                cur = 1
            elif i == 1 or (arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0:
                cur += 1
            else:
                cur = 2
            ans = max(ans, cur)
        return ans
