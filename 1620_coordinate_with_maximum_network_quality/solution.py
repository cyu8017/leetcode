class Solution:
    def bestCoordinate(self, towers, radius):
        import math
        best, quality = [0, 0], -1
        for x in range(51):
            for y in range(51):
                q = sum(int(v / (1 + math.hypot(x-a, y-b))) for a,b,v in towers if math.hypot(x-a,y-b) <= radius)
                if q > quality: quality, best = q, [x, y]
        return best
