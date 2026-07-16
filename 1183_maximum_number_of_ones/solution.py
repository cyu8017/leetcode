# LeetCode 1183 - Maximum Number of Ones
# https://leetcode.com/problems/maximum-number-of-ones/

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        counts = []
        for r in range(sideLength):
            for c in range(sideLength):
                rows = (height - r + sideLength - 1) // sideLength
                cols = (width - c + sideLength - 1) // sideLength
                counts.append(rows * cols)
        counts.sort(reverse=True)
        return sum(counts[:maxOnes])
