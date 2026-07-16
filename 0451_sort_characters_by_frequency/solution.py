# LeetCode 0451 - Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        return "".join(char * count for char, count in ordered)
