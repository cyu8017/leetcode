# LeetCode 3680 - Generate Schedule
# https://leetcode.com/problems/generate-schedule/

from typing import List


class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n < 5:
            return []
        matches = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    matches.append([i, j])
        used = [False] * len(matches)
        sched = []
        last0, last1 = -1, -1

        def dfs() -> bool:
            nonlocal last0, last1
            if len(sched) == len(matches):
                return True
            for i in range(len(matches)):
                if used[i]:
                    continue
                m = matches[i]
                if m[0] == last0 or m[0] == last1 or m[1] == last0 or m[1] == last1:
                    continue
                used[i] = True
                sched.append(m)
                p0, p1 = last0, last1
                last0, last1 = m[0], m[1]
                if dfs():
                    return True
                last0, last1 = p0, p1
                sched.pop()
                used[i] = False
            return False

        if dfs():
            return sched
        return []
