from typing import List, Optional

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        ans, stack, seen = 0, [0], {0}
        while stack:
            node = stack.pop()
            for nei, cost in graph[node]:
                if nei not in seen:
                    seen.add(nei); stack.append(nei); ans += cost
        return ans
