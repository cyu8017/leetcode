# LeetCode 3017 - Count the Number of Houses at a Certain Distance II
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x
        A = [0] * n
        for i in range(1, n + 1):
            A[0] += 2
            A[min(i - 1, abs(i - y) + x)] -= 1
            A[min(n - i, abs(i - x) + 1 + (n - y))] -= 1
            A[min(abs(i - x), abs(y - i) + 1)] += 1
            A[min(abs(i - x) + 1, abs(y - i))] += 1
            r = max(x - i, 0) + max(i - y, 0)
            A[r + ((y - x) // 2)] -= 1
            A[r + ((y - x + 1) // 2)] -= 1
        for i in range(1, n):
            A[i] += A[i - 1]
        return A
