# LeetCode 0890 - Find and Replace Pattern
# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def normalize(s: str) -> tuple:
            mapping = {}
            out = []
            for ch in s:
                if ch not in mapping:
                    mapping[ch] = len(mapping)
                out.append(mapping[ch])
            return tuple(out)

        target = normalize(pattern)
        return [w for w in words if normalize(w) == target]
