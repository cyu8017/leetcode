# LeetCode 3991 - Sort Array Using Prefix Reversals
# https://leetcode.com/problems/sort-array-using-prefix-reversals/

from collections import deque
from typing import List


class Solution:
    def sortArray(self, nums: List[int], pre: List[int]) -> int:
        n = len(nums)
        start = tuple(nums)
        target = tuple(range(n))
        if start == target:
            return 0

        # BFS over permutations; each move reverses a prefix whose length is in `pre`.
        lengths = sorted(set(i for i in pre if 2 <= i <= n))
        visited = {start}
        queue = deque([start])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                for i in lengths:
                    nxt = cur[i - 1 :: -1] + cur[i:]
                    if nxt == target:
                        return steps
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
        return -1
