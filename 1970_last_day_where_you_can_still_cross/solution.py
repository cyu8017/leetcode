from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can(day: int) -> bool:
            blocked = {(r - 1, c - 1) for r, c in cells[:day]}
            stack = [(0, c) for c in range(col) if (0, c) not in blocked]
            seen = set(stack)
            while stack:
                r, c = stack.pop()
                if r == row - 1:
                    return True
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in blocked and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            return False

        lo, hi, ans = 1, len(cells), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
