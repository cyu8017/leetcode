# LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

from typing import List
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total1 = 0
        for x in nums:
            total1 += x
        best = total1
        left0 = 0
        right1 = total1
        ans = [0]
        for i in range(n):
            if nums[i] == 0:
                left0 += 1
            else:
                right1 -= 1
            score = left0 + right1
            if score > best:
                best = score
                ans = [i + 1]
            elif score == best:
                ans.append(i + 1)
        return ans
