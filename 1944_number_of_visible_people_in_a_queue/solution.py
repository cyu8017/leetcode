from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []  # decreasing heights to the right
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            if stack:
                count += 1
            ans[i] = count
            stack.append(heights[i])
        return ans
