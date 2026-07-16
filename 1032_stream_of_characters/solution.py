# LeetCode 1032 - Stream of Characters
# https://leetcode.com/problems/stream-of-characters/

class StreamChecker:
    def __init__(self, words: list[str]):
        self.trie: dict = {}
        for word in words:
            node = self.trie
            for ch in reversed(word):
                node = node.setdefault(ch, {})
            node["$"] = True
        self.stream: list[str] = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie
        for ch in reversed(self.stream):
            if "$" in node:
                return True
            if ch not in node:
                return False
            node = node[ch]
        return "$" in node
