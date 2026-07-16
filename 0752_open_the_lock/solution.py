# LeetCode 0752 - Open the Lock
# https://leetcode.com/problems/open-the-lock/

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = deque([("0000", 0)])
        seen = {"0000"}
        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            for i in range(4):
                digit = int(state[i])
                for delta in (-1, 1):
                    nxt = state[:i] + str((digit + delta) % 10) + state[i + 1 :]
                    if nxt not in seen and nxt not in dead:
                        seen.add(nxt)
                        queue.append((nxt, steps + 1))
        return -1
