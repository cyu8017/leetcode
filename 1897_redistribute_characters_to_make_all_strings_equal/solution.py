# LeetCode 1897 - Redistribute Characters to Make All Strings Equal
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

from collections import Counter


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        counts = Counter("".join(words))
        n = len(words)
        return all(total % n == 0 for total in counts.values())
