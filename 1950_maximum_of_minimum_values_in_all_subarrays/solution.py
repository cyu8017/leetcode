from typing import List

class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stack = []
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] >= x:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = [0] * n
        for i, x in enumerate(nums):
            length = right[i] - left[i] - 1
            ans[length - 1] = max(ans[length - 1], x)
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i], ans[i + 1])
        return ans
