# LeetCode 2115 - Find All Possible Recipes from Given Supplies
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from typing import List
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        have = set(supplies)
        indeg = {}
        graph = {}
        for i in range(len(recipes)):
            indeg[recipes[i]] = len(ingredients[i])
            for ing in ingredients[i]:
                if ing not in graph:
                    graph[ing] = []
                graph.get(ing).append(recipes[i])
        q = list(have)
        ans = []
        while q:
            cur = q.pop(0)
            if cur not in graph:
                continue
            for nxt in graph.get(cur):
                d = indeg.get(nxt) - 1
                indeg[nxt] = d
                if d == 0:
                    ans.append(nxt)
                    q.append(nxt)
        return ans
