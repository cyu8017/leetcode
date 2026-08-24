# LeetCode 2833 - Furthest Point From Origin
# https://leetcode.com/problems/furthest-point-from-origin/


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = right = u = 0
        for c in moves:
            if c == "L":
                left += 1
            elif c == "R":
                right += 1
            else:
                u += 1
        return abs(left - right) + u
