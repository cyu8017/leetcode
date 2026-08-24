# LeetCode 3045 - Count Prefix and Suffix Pairs II
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

from typing import List


class Node:
    def __init__(self):
        self.children = {}
        self.cnt = 0


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Node()
        ans = 0
        for s in words:
            node = trie
            m = len(s)
            for i in range(m):
                p = ord(s[i]) * 32 + ord(s[m - i - 1])
                nxt = node.children.get(p)
                if not nxt:
                    nxt = Node()
                    node.children[p] = nxt
                node = nxt
                ans += node.cnt
            node.cnt += 1
        return ans
