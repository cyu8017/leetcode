# LeetCode 3476 - Maximize Profit from Task Assignment
# https://leetcode.com/problems/maximize-profit-from-task-assignment/

from typing import List


class Solution:
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
        workers = sorted(workers)
        tasks = sorted(tasks, key=lambda t: t[0])
        ans = 0
        used = [False] * len(tasks)
        for w in workers:
            best, bi = -1, -1
            for i in range(len(tasks)):
                if used[i]:
                    continue
                if tasks[i][0] > w:
                    break
                if tasks[i][1] > best:
                    best = tasks[i][1]
                    bi = i
            if bi >= 0:
                used[bi] = True
                ans += best
        return ans
