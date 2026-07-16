class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m: n, m = m, n
        heights, best = [0] * m, n * m
        def search(used):
            nonlocal best
            if used >= best: return
            low = min(heights)
            if low == n:
                best = used
                return
            left = heights.index(low)
            right = left
            while right < m and heights[right] == low: right += 1
            max_size = min(n - low, right - left)
            for size in range(max_size, 0, -1):
                heights[left:left + size] = [low + size] * size
                search(used + 1)
                heights[left:left + size] = [low] * size
        search(0)
        return best
