# LeetCode 0832 - Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        return [[1 - x for x in reversed(row)] for row in image]
