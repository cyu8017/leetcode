from typing import List

class TrieNode:
    __slots__ = ("child", "cnt")
    def __init__(self):
        self.child = [None, None]
        self.cnt = 0

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        children = [[] for _ in range(n)]
        root = 0
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        qmap = [[] for _ in range(n)]
        for i, (node, val) in enumerate(queries):
            qmap[node].append((i, val))

        ans = [0] * len(queries)
        trie_root = TrieNode()
        BITS = 17  # values up to 1e5

        def trie_update(num: int, delta: int) -> None:
            node = trie_root
            for b in range(BITS, -1, -1):
                bit = (num >> b) & 1
                if node.child[bit] is None:
                    node.child[bit] = TrieNode()
                node = node.child[bit]
                node.cnt += delta

        def trie_max_xor(num: int) -> int:
            node = trie_root
            res = 0
            for b in range(BITS, -1, -1):
                bit = (num >> b) & 1
                want = 1 - bit
                if node.child[want] and node.child[want].cnt > 0:
                    res |= 1 << b
                    node = node.child[want]
                else:
                    node = node.child[bit]
            return res

        def dfs(u: int) -> None:
            trie_update(u, 1)
            for qi, val in qmap[u]:
                ans[qi] = trie_max_xor(val)
            for v in children[u]:
                dfs(v)
            trie_update(u, -1)

        dfs(root)
        return ans
