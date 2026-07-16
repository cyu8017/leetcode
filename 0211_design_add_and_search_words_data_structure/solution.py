# LeetCode 0211 - Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_word
            char = word[index]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            if char not in node.children:
                return False
            return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)
