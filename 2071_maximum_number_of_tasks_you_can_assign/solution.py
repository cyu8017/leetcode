# LeetCode 2071 - Maximum Number of Tasks You Can Assign
# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

from typing import List
from collections import Counter


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def remove(ws: Counter, x: int) -> None:
            ws[x] -= 1
            if ws[x] == 0:
                del ws[x]

        def can(k: int) -> bool:
            if k == 0:
                return True
            ws = Counter(workers[len(workers) - k :])
            p = pills
            for i in range(k - 1, -1, -1):
                task = tasks[i]
                ks = sorted(ws.keys())
                strongest = ks[-1]
                if strongest >= task:
                    remove(ws, strongest)
                    continue
                if p == 0:
                    return False
                need = task - strength
                found = None
                for key in ks:
                    if key >= need:
                        found = key
                        break
                if found is None:
                    return False
                remove(ws, found)
                p -= 1
            return True

        lo, hi = 0, min(len(tasks), len(workers))
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
