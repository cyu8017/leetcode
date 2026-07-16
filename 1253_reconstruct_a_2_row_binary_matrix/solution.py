from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        top, bottom = [0] * len(colsum), [0] * len(colsum)
        for i, value in enumerate(colsum):
            if value == 2:
                top[i] = bottom[i] = 1
                upper -= 1
                lower -= 1
        if upper < 0 or lower < 0:
            return []
        for i, value in enumerate(colsum):
            if value == 1:
                if upper:
                    top[i] = 1
                    upper -= 1
                elif lower:
                    bottom[i] = 1
                    lower -= 1
                else:
                    return []
        return [top, bottom] if upper == lower == 0 else []
