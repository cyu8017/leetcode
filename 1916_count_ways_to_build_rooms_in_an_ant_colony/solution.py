from typing import List

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)
        children = [[] for _ in range(n)]
        for room, prev in enumerate(prevRoom):
            if prev != -1:
                children[prev].append(room)

        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a: int, b: int) -> int:
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        def dfs(node: int):
            size = 0
            ways = 1
            for child in children[node]:
                child_size, child_ways = dfs(child)
                ways = ways * child_ways % MOD * comb(size + child_size, child_size) % MOD
                size += child_size
            return size + 1, ways

        return dfs(0)[1]
