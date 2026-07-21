from typing import List

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        possible = {0}
        for row in mat:
            nxt: set[int] = set()
            for s in possible:
                for x in set(row):
                    nxt.add(s + x)
            # keep all <= target and the smallest > target
            kept = {v for v in nxt if v <= target}
            above = [v for v in nxt if v > target]
            if above:
                kept.add(min(above))
            possible = kept if kept else {min(nxt)}
        return min(abs(v - target) for v in possible)
