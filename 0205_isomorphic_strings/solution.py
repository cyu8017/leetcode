# LeetCode 0205 - Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s: dict[str, str] = {}
        map_t: dict[str, str] = {}
        for a, b in zip(s, t):
            if map_s.get(a, b) != b or map_t.get(b, a) != a:
                return False
            map_s[a] = b
            map_t[b] = a
        return True
