from typing import List, Optional

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int,
                n: int, target: int) -> int:
        inf = 10**15
        dp = {(0, 0): 0}
        for i, painted in enumerate(houses):
            nxt = {}
            colors = [painted] if painted else range(1, n + 1)
            for (prev, groups), value in dp.items():
                for color in colors:
                    ng = groups + (color != prev)
                    if ng <= target:
                        nv = value + (0 if painted else cost[i][color-1])
                        nxt[color, ng] = min(nxt.get((color, ng), inf), nv)
            dp = nxt
        ans = min((v for (c, g), v in dp.items() if g == target), default=inf)
        return -1 if ans == inf else ans
