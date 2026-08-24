# LeetCode 3093 - Longest Common Suffix Queries
# https://leetcode.com/problems/longest-common-suffix-queries/

from typing import List

INF = 1 << 30


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.length = INF
        self.idx = INF


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        def insert(t: Trie, w: str, i: int) -> None:
            node = t
            if node.length > len(w):
                node.length = len(w)
                node.idx = i
            for k in range(len(w) - 1, -1, -1):
                cid = ord(w[k]) - 97
                if node.children[cid] is None:
                    node.children[cid] = Trie()
                node = node.children[cid]
                if node.length > len(w):
                    node.length = len(w)
                    node.idx = i

        def query(t: Trie, w: str) -> int:
            node = t
            for k in range(len(w) - 1, -1, -1):
                cid = ord(w[k]) - 97
                if node.children[cid] is None:
                    break
                node = node.children[cid]
            return node.idx

        trie = Trie()
        for i, w in enumerate(wordsContainer):
            insert(trie, w, i)
        return [query(trie, w) for w in wordsQuery]
