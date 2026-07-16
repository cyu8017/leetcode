class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        lo, hi = 1, sum(sweetness) // (k + 1)
        while lo <= hi:
            mid, pieces, current = (lo + hi) // 2, 0, 0
            for value in sweetness:
                current += value
                if current >= mid:
                    pieces += 1
                    current = 0
            if pieces >= k + 1: lo = mid + 1
            else: hi = mid - 1
        return hi
