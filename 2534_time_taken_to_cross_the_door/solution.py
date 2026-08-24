# LeetCode 2534 - Time Taken to Cross the Door
# https://leetcode.com/problems/time-taken-to-cross-the-door/

from collections import deque
from typing import List


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        ans = [0] * n
        enter = deque()
        exitq = deque()
        i = 0
        t = 0
        prev = 1
        while i < n or enter or exitq:
            while i < n and arrival[i] <= t:
                if state[i] == 0:
                    enter.append(i)
                else:
                    exitq.append(i)
                i += 1
            if not enter and not exitq:
                if i < n:
                    t = arrival[i]
                    prev = 1
                continue
            if prev == 1:
                if exitq:
                    ans[exitq.popleft()] = t
                    prev = 1
                else:
                    ans[enter.popleft()] = t
                    prev = 0
            else:
                if enter:
                    ans[enter.popleft()] = t
                    prev = 0
                else:
                    ans[exitq.popleft()] = t
                    prev = 1
            t += 1
        return ans
