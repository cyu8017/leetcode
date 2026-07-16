from typing import List, Optional

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        seen = {(0, 0)}
        move = {"N": (0,1), "S": (0,-1), "E": (1,0), "W": (-1,0)}
        for c in path:
            dx, dy = move[c]; x += dx; y += dy
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False
