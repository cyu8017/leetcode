# LeetCode 2059 - Minimum Operations to Convert Number
# https://leetcode.com/problems/minimum-operations-to-convert-number/

from collections import deque
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        if start == goal:
            return 0
        vis = {start}
        q = deque([start])
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for x in nums:
                    for nxt in (cur + x, cur - x, cur ^ x):
                        if nxt == goal:
                            return steps
                        if 0 <= nxt <= 1000 and nxt not in vis:
                            vis.add(nxt)
                            q.append(nxt)
        return -1
