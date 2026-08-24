# LeetCode 3200 - Maximum Height of a Triangle
# https://leetcode.com/problems/maximum-height-of-a-triangle/

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        ans = 0
        for k in range(2):
            c = [red, blue]
            i, j = 1, k
            while i <= c[j]:
                c[j] -= i
                ans = max(ans, i)
                i += 1
                j ^= 1
        return ans
