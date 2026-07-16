# LeetCode 0985 - Sum of Even Numbers After Queries
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even = sum(x for x in nums if x % 2 == 0)
        ans = []
        for val, i in queries:
            if nums[i] % 2 == 0:
                even -= nums[i]
            nums[i] += val
            if nums[i] % 2 == 0:
                even += nums[i]
            ans.append(even)
        return ans
