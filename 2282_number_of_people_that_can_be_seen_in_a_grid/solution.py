# LeetCode 2282 - Number of People That Can Be Seen in a Grid
# https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

from typing import List


class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            stack = []
            for j in range(n - 1, -1, -1):
                cnt = 0
                while stack and heights[i][stack[-1]] < heights[i][j]:
                    stack.pop()
                    cnt += 1
                if stack:
                    cnt += 1
                ans[i][j] += cnt
                while stack and heights[i][stack[-1]] == heights[i][j]:
                    stack.pop()
                stack.append(j)
        for j in range(n):
            stack = []
            for i in range(m - 1, -1, -1):
                cnt = 0
                while stack and heights[stack[-1]][j] < heights[i][j]:
                    stack.pop()
                    cnt += 1
                if stack:
                    cnt += 1
                ans[i][j] += cnt
                while stack and heights[stack[-1]][j] == heights[i][j]:
                    stack.pop()
                stack.append(i)
        return ans
