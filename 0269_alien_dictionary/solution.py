# LeetCode 0269 - Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/

from collections import Counter, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph: dict[str, set[str]] = {char: set() for word in words for char in word}
        indegree = Counter({char: 0 for char in graph})

        for first, second in zip(words, words[1:]):
            if len(first) > len(second) and first.startswith(second):
                return ""
            for left, right in zip(first, second):
                if left != right:
                    if right not in graph[left]:
                        graph[left].add(right)
                        indegree[right] += 1
                    break

        queue = deque(char for char in indegree if indegree[char] == 0)
        order: list[str] = []
        while queue:
            char = queue.popleft()
            order.append(char)
            for nxt in graph[char]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        if len(order) != len(indegree):
            return ""
        return "".join(order)
