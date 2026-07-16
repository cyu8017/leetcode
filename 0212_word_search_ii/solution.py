# LeetCode 0212 - Word Search II
# https://leetcode.com/problems/word-search-ii/

from typing import List


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.word: str | None = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result: set[str] = set()

        def dfs(r: int, c: int, node: TrieNode) -> None:
            char = board[r][c]
            if char not in node.children:
                return
            nxt = node.children[char]
            if nxt.word:
                result.add(nxt.word)
                nxt.word = None
            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = char
            if not nxt.children:
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return list(result)
