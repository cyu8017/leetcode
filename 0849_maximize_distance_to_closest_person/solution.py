# LeetCode 0849 - Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        prev = -1
        ans = 0
        for i, occupied in enumerate(seats):
            if occupied:
                if prev == -1:
                    ans = i
                else:
                    ans = max(ans, (i - prev) // 2)
                prev = i
        ans = max(ans, n - 1 - prev)
        return ans
