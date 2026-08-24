# LeetCode 2647 - Color the Triangle Red
# https://leetcode.com/problems/color-the-triangle-red/

from typing import List


class Solution:
    def colorRed(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(1, n + 1):
            ans.append([i, 1])
        for i in range(n % 2 + 2, n + 1, 2):
            for j in range(2, 2 * (n - i) + 3):
                ans.append([i, j])
        return ans
