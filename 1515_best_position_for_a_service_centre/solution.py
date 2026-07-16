# LeetCode 1515

class Solution:
    def getMinDistSum(self, positions):
        import math
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)
        def distance(a, b):
            return sum(math.hypot(a - px, b - py) for px, py in positions)
        for _ in range(10000):
            numerator_x = numerator_y = denominator = 0.0
            coincident = None
            for px, py in positions:
                d = math.hypot(x - px, y - py)
                if d < 1e-12:
                    coincident = (px, py)
                    break
                numerator_x += px / d
                numerator_y += py / d
                denominator += 1 / d
            nx, ny = coincident if coincident else (numerator_x / denominator, numerator_y / denominator)
            if math.hypot(nx - x, ny - y) < 1e-8:
                x, y = nx, ny
                break
            x, y = nx, ny
        return distance(x, y)
