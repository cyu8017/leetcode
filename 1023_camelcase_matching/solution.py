# LeetCode 1023 - Camelcase Matching
# https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        def matches(q: str) -> bool:
            i = 0
            for ch in q:
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                elif ch.isupper():
                    return False
            return i == len(pattern)

        return [matches(q) for q in queries]
