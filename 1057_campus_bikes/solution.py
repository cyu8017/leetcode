# LeetCode 1057 - Campus Bikes
# https://leetcode.com/problems/campus-bikes/

class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> list[int]:
        triples = sorted(
            (abs(wx - bx) + abs(wy - by), w, b)
            for w, (wx, wy) in enumerate(workers)
            for b, (bx, by) in enumerate(bikes)
        )
        ans = [-1] * len(workers)
        used_bikes = set()
        assigned = 0
        for _, w, b in triples:
            if ans[w] == -1 and b not in used_bikes:
                ans[w] = b
                used_bikes.add(b)
                assigned += 1
                if assigned == len(workers):
                    break
        return ans
