# LeetCode 0165 - Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = [int(part) for part in version1.split(".")]
        parts2 = [int(part) for part in version2.split(".")]
        n = max(len(parts1), len(parts2))
        parts1 += [0] * (n - len(parts1))
        parts2 += [0] * (n - len(parts2))
        for a, b in zip(parts1, parts2):
            if a < b:
                return -1
            if a > b:
                return 1
        return 0
