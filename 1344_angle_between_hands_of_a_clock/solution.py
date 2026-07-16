# LeetCode 1344 - Angle Between Hands Of A Clock

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        difference = abs((hour % 12) * 30 + minutes * 0.5 - minutes * 6)
        return min(difference, 360 - difference)
