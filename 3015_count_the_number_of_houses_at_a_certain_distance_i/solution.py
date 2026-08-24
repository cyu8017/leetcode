# LeetCode 3015 - Count the Number of Houses at a Certain Distance I
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [0] * n
        x -= 1
        y -= 1
        for i in range(n):
            for j in range(i + 1, n):
                a = j - i
                b = abs(x - i) + abs(y - j) + 1
                c = abs(x - j) + abs(y - i) + 1
                ans[min(a, min(b, c)) - 1] += 2
        return ans
