# LeetCode 0126 - Word Ladder II
# https://leetcode.com/problems/word-ladder-ii/

from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        parents: dict[str, list[str]] = defaultdict(list)
        visited = {beginWord}
        queue = deque([beginWord])
        found = False

        while queue and not found:
            level_visited = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                chars = list(word)
                for i in range(len(chars)):
                    original = chars[i]
                    for code in range(ord("a"), ord("z") + 1):
                        chars[i] = chr(code)
                        nxt = "".join(chars)
                        if nxt not in word_set:
                            continue
                        if nxt not in visited:
                            if nxt not in level_visited:
                                level_visited.add(nxt)
                                queue.append(nxt)
                            parents[nxt].append(word)
                            if nxt == endWord:
                                found = True
                    chars[i] = original
            visited |= level_visited

        if not found:
            return []

        results: list[list[str]] = []

        def dfs(word: str, path: list[str]) -> None:
            if word == beginWord:
                results.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()

        dfs(endWord, [endWord])
        results.sort()
        return results
