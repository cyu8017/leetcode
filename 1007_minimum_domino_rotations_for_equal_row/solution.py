# LeetCode 1007 - Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        def check(target: int) -> int:
            rot_top = rot_bot = 0
            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    return float("inf")
                if t != target:
                    rot_top += 1
                if b != target:
                    rot_bot += 1
            return min(rot_top, rot_bot)

        ans = min(check(tops[0]), check(bottoms[0]))
        return -1 if ans == float("inf") else ans
