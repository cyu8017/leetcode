# LeetCode 0522 - Longest Uncommon Subsequence II
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        def is_subsequence(target: str, source: str) -> bool:
            index = 0
            for char in source:
                if index < len(target) and target[index] == char:
                    index += 1
            return index == len(target)

        result = -1
        for i, candidate in enumerate(strs):
            if any(i != j and is_subsequence(candidate, strs[j]) for j in range(len(strs))):
                continue
            result = max(result, len(candidate))
        return result
