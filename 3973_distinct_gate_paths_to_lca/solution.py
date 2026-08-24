# LeetCode 3973 - Distinct Gate Paths to LCA
# https://leetcode.com/problems/distinct-gate-paths-to-lca/

from typing import List

MOD = 1000000007


def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD
    return c


class Solution:
    def gatePathXor(self, n: int, parent: List[int], gates: List[List[int]], queries: List[List[int]]) -> int:
        logn = 1
        while (1 << logn) <= n:
            logn += 1
        up = [[0] * n for _ in range(logn)]
        product = [[None] * n for _ in range(logn)]
        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[parent[node]].append(node)
        depth = [0] * n
        order = [0]
        i = 0
        while i < len(order):
            u = order[i]
            for v in children[u]:
                depth[v] = depth[u] + 1
                order.append(v)
            i += 1
        for u in range(n):
            up[0][u] = 0 if u == 0 else parent[u]
            product[0][u] = [
                [gates[u][1], gates[u][2]],
                [gates[u][2], gates[u][0]],
            ]
        for level in range(1, logn):
            for u in range(n):
                mid = up[level - 1][u]
                up[level][u] = up[level - 1][mid]
                product[level][u] = multiply(product[level - 1][u], product[level - 1][mid])
        answer = 0
        for query in queries:
            ancestor = self.lca(query[0], query[2], depth, up, logn)
            alice = self.ways(query[0], query[1], depth[query[0]] - depth[ancestor], up, product)
            bob = self.ways(query[2], query[3], depth[query[2]] - depth[ancestor], up, product)
            total = (alice * bob) % MOD
            answer ^= total
        return answer

    def liftNode(self, node: int, distance: int, up: List[List[int]]) -> int:
        level = 0
        while distance > 0:
            if (distance & 1) != 0:
                node = up[level][node]
            distance >>= 1
            level += 1
        return node

    def lca(self, a: int, b: int, depth: List[int], up: List[List[int]], logn: int) -> int:
        if depth[a] > depth[b]:
            a = self.liftNode(a, depth[a] - depth[b], up)
        elif depth[b] > depth[a]:
            b = self.liftNode(b, depth[b] - depth[a], up)
        if a == b:
            return a
        for level in range(logn - 1, -1, -1):
            if up[level][a] != up[level][b]:
                a = up[level][a]
                b = up[level][b]
        return up[0][a]

    def ways(self, node: int, card: int, distance: int, up: List[List[int]], product: List[List[List[List[int]]]]) -> int:
        vector = [0, 0]
        vector[card] = 1
        level = 0
        while distance > 0:
            if (distance & 1) != 0:
                matrix = product[level][node]
                vector = [
                    (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % MOD,
                    (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % MOD,
                ]
                node = up[level][node]
            distance >>= 1
            level += 1
        return (vector[0] + vector[1]) % MOD
