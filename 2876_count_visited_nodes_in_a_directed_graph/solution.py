# LeetCode 2876 - Count Visited Nodes in a Directed Graph
# https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [0] * n
        state = [0] * n
        stack = []

        def dfs(u: int) -> None:
            state[u] = 1
            stack.append(u)
            v = edges[u]
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                idx = len(stack) - 1
                while stack[idx] != v:
                    idx -= 1
                cyc = len(stack) - idx
                for i in range(idx, len(stack)):
                    ans[stack[i]] = cyc
            if ans[u] == 0:
                ans[u] = ans[edges[u]] + 1
            state[u] = 2
            stack.pop()

        for i in range(n):
            if state[i] == 0:
                dfs(i)
        return ans
