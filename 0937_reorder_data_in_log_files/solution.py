# LeetCode 0937 - Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def key(log: str) -> tuple:
            ident, rest = log.split(" ", 1)
            return (0, rest, ident) if rest[0].isalpha() else (1,)

        return sorted(logs, key=key)
