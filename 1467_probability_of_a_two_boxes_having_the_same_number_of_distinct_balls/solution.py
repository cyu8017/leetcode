from typing import List, Optional

import math

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        half = sum(balls) // 2
        good = total = 0
        def dfs(i, left, dl, ways):
            nonlocal good, total
            if i == len(balls):
                if left == half:
                    total += ways
                    if dl == 0:
                        good += ways
                return
            for x in range(balls[i] + 1):
                if left + x <= half:
                    dfs(i + 1, left + x, dl + (x > 0) - (x < balls[i]),
                        ways * math.comb(balls[i], x))
        dfs(0, 0, 0, 1)
        return good / total
