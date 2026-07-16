class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts = {}
        for value in range(lowLimit, highLimit + 1):
            box = sum(map(int, str(value)))
            counts[box] = counts.get(box, 0) + 1
        return max(counts.values())
