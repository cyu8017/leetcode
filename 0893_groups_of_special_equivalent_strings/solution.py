# LeetCode 0893 - Groups of Special-Equivalent Strings
# https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        groups = set()
        for w in words:
            even = "".join(sorted(w[::2]))
            odd = "".join(sorted(w[1::2]))
            groups.add((even, odd))
        return len(groups)
