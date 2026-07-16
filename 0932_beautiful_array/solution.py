# LeetCode 0932 - Beautiful Array
# https://leetcode.com/problems/beautiful-array/

class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        if n == 1:
            return [1]
        left = self.beautifulArray((n + 1) // 2)
        right = self.beautifulArray(n // 2)
        return [2 * x - 1 for x in left] + [2 * x for x in right]
