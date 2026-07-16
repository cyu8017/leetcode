# LeetCode 0977 - Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        i, j = 0, n - 1
        for k in range(n - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                ans[k] = nums[i] * nums[i]
                i += 1
            else:
                ans[k] = nums[j] * nums[j]
                j -= 1
        return ans
