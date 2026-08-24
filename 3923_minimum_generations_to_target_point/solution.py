# LeetCode 3923 - Minimum Generations to Target Point
# https://leetcode.com/problems/minimum-generations-to-target-point/

from typing import Dict, List


class P:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def key(self) -> str:
        return f"{self.a},{self.b},{self.c}"


class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        target_key = f"{target[0]},{target[1]},{target[2]}"
        generation: Dict[str, int] = {}
        all_pts: List[P] = []
        for values in points:
            p = P(values[0], values[1], values[2])
            generation[p.key()] = 0
            all_pts.append(p)
        if target_key in generation:
            return generation[target_key]
        current = 1
        while True:
            limit = len(all_pts)
            added: List[P] = []
            for i in range(limit):
                for j in range(i + 1, limit):
                    pi = all_pts[i]
                    pj = all_pts[j]
                    if pi.a == pj.a and pi.b == pj.b and pi.c == pj.c:
                        continue
                    p = P((pi.a + pj.a) // 2, (pi.b + pj.b) // 2, (pi.c + pj.c) // 2)
                    key = p.key()
                    if key not in generation:
                        generation[key] = current
                        added.append(p)
            if target_key in generation:
                return generation[target_key]
            if len(added) == 0:
                return -1
            for p in added:
                all_pts.append(p)
            current += 1
