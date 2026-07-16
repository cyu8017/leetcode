class Solution:
    def nearestValidPoint(self, x, y, points):
        best = float("inf")
        ans = -1
        for i, (px, py) in enumerate(points):
            if px != x and py != y:
                continue
            dist = abs(px - x) + abs(py - y)
            if dist < best:
                best = dist
                ans = i
        return ans
