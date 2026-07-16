# LeetCode 0127 - Word Ladder
# https://leetcode.com/problems/word-ladder/

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            chars = list(word)
            for i in range(len(chars)):
                original = chars[i]
                for code in range(ord("a"), ord("z") + 1):
                    chars[i] = chr(code)
                    nxt = "".join(chars)
                    if nxt in word_set and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))
                chars[i] = original
        return 0
