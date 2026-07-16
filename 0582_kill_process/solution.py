# LeetCode 0582 - Kill Process
# https://leetcode.com/problems/kill-process/

from collections import defaultdict, deque
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children: dict[int, list[int]] = defaultdict(list)
        for child, parent in zip(pid, ppid):
            children[parent].append(child)

        result: list[int] = []
        queue: deque[int] = deque([kill])
        while queue:
            process = queue.popleft()
            result.append(process)
            queue.extend(children[process])
        return result
