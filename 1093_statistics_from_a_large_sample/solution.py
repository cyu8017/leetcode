# LeetCode 1093 - Statistics from a Large Sample
# https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:
        total = sum(count)
        minimum = next(i for i, c in enumerate(count) if c)
        maximum = next(i for i in range(255, -1, -1) if count[i])
        mean = sum(i * c for i, c in enumerate(count)) / total
        mode = max(range(256), key=lambda i: count[i])
        mid1 = (total + 1) // 2
        mid2 = (total + 2) // 2
        seen = 0
        first = second = None
        for i, c in enumerate(count):
            seen += c
            if first is None and seen >= mid1:
                first = i
            if second is None and seen >= mid2:
                second = i
                break
        median = (first + second) / 2
        return [float(minimum), float(maximum), float(mean), float(median), float(mode)]
