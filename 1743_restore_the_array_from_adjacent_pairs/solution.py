from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        start = next(node for node, neighbors in graph.items() if len(neighbors) == 1)
        ans = [start]
        prev = None
        while len(ans) < len(graph):
            cur = ans[-1]
            nxt = graph[cur][0] if graph[cur][0] != prev else graph[cur][1]
            ans.append(nxt)
            prev = cur
        return ans
