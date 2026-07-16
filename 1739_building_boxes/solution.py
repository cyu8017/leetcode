class Solution:
    def minimumBoxes(self, n: int) -> int:
        height = 0
        used = 0
        base = 0
        while used + (height + 1) * (height + 2) // 2 <= n:
            height += 1
            layer = height * (height + 1) // 2
            used += layer
            base += height
        extra = 0
        while used < n:
            extra += 1
            used += extra
        return base + extra
