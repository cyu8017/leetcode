# LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a = "".join(sorted([s1[0], s1[2]]))
        b = "".join(sorted([s2[0], s2[2]]))
        c = "".join(sorted([s1[1], s1[3]]))
        d = "".join(sorted([s2[1], s2[3]]))
        return a == b and c == d
