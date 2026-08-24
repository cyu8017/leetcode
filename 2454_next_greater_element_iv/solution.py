# LeetCode 2454 - Next Greater Element IV
# https://leetcode.com/problems/next-greater-element-iv/

from typing import List


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack1, stack2 = [], []
        for i in range(n):
            x = nums[i]
            while stack2 and nums[stack2[-1]] < x:
                ans[stack2.pop()] = x
            tmp = []
            while stack1 and nums[stack1[-1]] < x:
                tmp.append(stack1.pop())
            for j in range(len(tmp) - 1, -1, -1):
                stack2.append(tmp[j])
            stack1.append(i)
        return ans
