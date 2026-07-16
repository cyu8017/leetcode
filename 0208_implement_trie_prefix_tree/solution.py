# LeetCode 0208 - Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return bool(node and node.is_word)

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, text: str) -> TrieNode | None:
        node = self.root
        for char in text:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
