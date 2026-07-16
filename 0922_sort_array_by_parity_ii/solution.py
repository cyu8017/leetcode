# LeetCode 0922 - Sort Array By Parity II
# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        even = odd = 0
        for x in nums:
            if x % 2 == 0:
                ans[even] = x
                even += 2
            else:
                ans[odd + 1] = x
                odd += 2
        return ans
