# LeetCode 0886 - Possible Bipartition
# https://leetcode.com/problems/possible-bipartition/

from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color = {}
        for start in range(1, n + 1):
            if start in color:
                continue
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in color:
                        color[nei] = color[node] ^ 1
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False
        return True
