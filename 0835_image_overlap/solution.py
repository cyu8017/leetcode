# LeetCode 0835 - Image Overlap
# https://leetcode.com/problems/image-overlap/

from collections import Counter


class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        if not ones1 or not ones2:
            return 0
        shifts = Counter((x1 - x2, y1 - y2) for x1, y1 in ones1 for x2, y2 in ones2)
        return max(shifts.values())
