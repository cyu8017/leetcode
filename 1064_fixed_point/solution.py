# LeetCode 1064 - Fixed Point
# https://leetcode.com/problems/fixed-point/

class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        lo, hi = 0, len(arr) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == mid:
                ans = mid
                hi = mid - 1
            elif arr[mid] < mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
