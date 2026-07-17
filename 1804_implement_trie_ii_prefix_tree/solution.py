# LeetCode 1804 - Implement Trie II (Prefix Tree)
# https://leetcode.com/problems/implement-trie-ii-prefix-tree/


class TrieNode:
    __slots__ = ("children", "word_count", "prefix_count")

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word_count = 0
        self.prefix_count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1
        node.word_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self._find(word)
        return node.word_count if node else 0

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self._find(prefix)
        return node.prefix_count if node else 0

    def erase(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.prefix_count -= 1
        node.word_count -= 1

    def _find(self, text: str) -> TrieNode | None:
        node = self.root
        for ch in text:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
