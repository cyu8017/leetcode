# LeetCode 3841 - Palindromic Path Queries in a Tree
# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

from typing import List


class Solution:
    def palindromicPathQueries(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        parent = [-2] * n
        depth = [0] * n
        parent[0] = -1
        order = [0]
        i = 0
        while i < len(order):
            u = order[i]
            for v in graph[u]:
                if parent[v] == -2:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)
            i += 1
        size = [0] * n
        heavy = [-1] * n
        for i in range(n - 1, -1, -1):
            u = order[i]
            size[u] = 1
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if heavy[u] == -1 or size[v] > size[heavy[u]]:
                        heavy[u] = v
        head = [0] * n
        position = [0] * n
        stack = [[0, 0]]
        nextPosition = 0
        while stack:
            chain = stack.pop()
            u = chain[0]
            while u != -1:
                head[u] = chain[1]
                position[u] = nextPosition
                nextPosition += 1
                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append([v, v])
                u = heavy[u]
        bit = [0] * (n + 1)

        def update(index: int, value: int) -> None:
            index += 1
            while index <= n:
                bit[index] ^= value
                index += index & -index

        def prefix(index: int) -> int:
            result = 0
            while index > 0:
                result ^= bit[index]
                index -= index & -index
            return result

        def pathMask(u: int, v: int) -> int:
            result = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                result ^= prefix(position[u] + 1) ^ prefix(position[head[u]])
                u = parent[head[u]]
            if position[u] > position[v]:
                u, v = v, u
            return result ^ prefix(position[v] + 1) ^ prefix(position[u])

        current = list(s)
        for node in range(n):
            update(position[node], 1 << (ord(current[node]) - 97))
        answer = []
        for query in queries:
            parts = query.split(" ")
            op = parts[0]
            node = int(parts[1])
            if op == "update":
                newCharacter = parts[2][0]
                delta = (1 << (ord(current[node]) - 97)) ^ (1 << (ord(newCharacter) - 97))
                update(position[node], delta)
                current[node] = newCharacter
            else:
                other = int(parts[2])
                mask = pathMask(node, other)
                answer.append((mask & (mask - 1)) == 0)
        return answer
