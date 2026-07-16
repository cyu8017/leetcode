# LeetCode 0851 - Loud and Rich
# https://leetcode.com/problems/loud-and-rich/

from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)

        ans = [-1] * n

        def dfs(person: int) -> int:
            if ans[person] != -1:
                return ans[person]
            best = person
            for richer_person in graph[person]:
                cand = dfs(richer_person)
                if quiet[cand] < quiet[best]:
                    best = cand
            ans[person] = best
            return best

        for i in range(n):
            dfs(i)
        return ans
