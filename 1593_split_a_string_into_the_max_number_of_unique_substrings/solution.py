from typing import List

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        used, answer = set(), 0
        def dfs(i):
            nonlocal answer
            if len(used) + len(s) - i <= answer:
                return
            if i == len(s):
                answer = max(answer, len(used))
                return
            for j in range(i + 1, len(s) + 1):
                part = s[i:j]
                if part not in used:
                    used.add(part); dfs(j); used.remove(part)
        dfs(0)
        return answer
