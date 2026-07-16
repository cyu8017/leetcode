# LeetCode 1087 - Brace Expansion
# https://leetcode.com/problems/brace-expansion/

class Solution:
    def expand(self, s: str) -> list[str]:
        groups: list[list[str]] = []
        i = 0
        while i < len(s):
            if s[i] == "{":
                j = s.index("}", i)
                groups.append(sorted(s[i + 1 : j].split(",")))
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1
        ans = [""]
        for group in groups:
            ans = [prefix + ch for prefix in ans for ch in group]
        return ans
