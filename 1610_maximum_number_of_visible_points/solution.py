class Solution:
    def visiblePoints(self, points, angle, location):
        import math
        same = 0; a = []
        for x, y in points:
            dx, dy = x - location[0], y - location[1]
            if dx == dy == 0: same += 1
            else: a.append(math.atan2(dy, dx))
        a.sort(); ext = a + [x + 2 * math.pi for x in a]
        width = math.radians(angle) + 1e-12; left = best = 0
        for right, value in enumerate(ext):
            while value - ext[left] > width: left += 1
            best = max(best, min(len(a), right - left + 1))
        return best + same
