# LeetCode 1049 - Last Stone Weight II
# https://leetcode.com/problems/last-stone-weight-ii/

class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        reachable = {0}
        for stone in stones:
            reachable = {s + stone for s in reachable} | {s for s in reachable}
        best = min(abs(total - 2 * s) for s in reachable)
        return best
