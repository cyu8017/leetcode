# LeetCode 1893 - Check if All the Integers in a Range Are Covered
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        covered = [False] * 51
        for start, end in ranges:
            for value in range(start, end + 1):
                covered[value] = True
        return all(covered[value] for value in range(left, right + 1))
