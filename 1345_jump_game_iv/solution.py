# LeetCode 1345 - Jump Game Iv

from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        positions = defaultdict(list)
        for i, value in enumerate(arr):
            positions[value].append(i)
        queue, seen, steps = deque([0]), {0}, 0
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if i == len(arr) - 1:
                    return steps
                for j in positions.pop(arr[i], []) + [i - 1, i + 1]:
                    if 0 <= j < len(arr) and j not in seen:
                        seen.add(j); queue.append(j)
            steps += 1
        return -1
