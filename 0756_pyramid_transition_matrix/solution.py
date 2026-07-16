# LeetCode 0756 - Pyramid Transition Matrix
# https://leetcode.com/problems/pyramid-transition-matrix/

from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        transitions: dict[str, list[str]] = defaultdict(list)
        for triple in allowed:
            transitions[triple[:2]].append(triple[2])

        @lru_cache(None)
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            options: list[list[str]] = []
            for i in range(len(row) - 1):
                choices = transitions.get(row[i : i + 2])
                if not choices:
                    return False
                options.append(choices)

            def build(index: int, path: list[str]) -> bool:
                if index == len(options):
                    return dfs("".join(path))
                for ch in options[index]:
                    path.append(ch)
                    if build(index + 1, path):
                        return True
                    path.pop()
                return False

            return build(0, [])

        return dfs(bottom)
