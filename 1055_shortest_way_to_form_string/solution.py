# LeetCode 1055 - Shortest Way to Form String
# https://leetcode.com/problems/shortest-way-to-form-string/

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set = set(source)
        if any(ch not in source_set for ch in target):
            return -1
        ans = 0
        i = 0
        n = len(target)
        while i < n:
            ans += 1
            for ch in source:
                if i < n and target[i] == ch:
                    i += 1
        return ans
