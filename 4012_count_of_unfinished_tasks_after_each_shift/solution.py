# LeetCode 4012 - Count of Unfinished Tasks After Each Shift
# https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

from typing import List


class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        m, n = len(tasks), len(shifts)
        s = [0] * (m + 1)
        for i in range(m):
            s[i + 1] = s[i] + tasks[i]
        ans = [0] * n
        i_idx = 0
        cur = 0
        for j in range(n):
            if shifts[j] < tasks[i_idx] - cur:
                cur += shifts[j]
                ans[j] = m - i_idx
            else:
                t = shifts[j] - (tasks[i_idx] - cur)
                if t >= s[m] - s[i_idx + 1]:
                    i_idx = 0
                    cur = 0
                else:
                    l, r = i_idx + 1, m
                    while l < r:
                        mid = (l + r) >> 1
                        if t < s[mid + 1] - s[i_idx + 1]:
                            r = mid
                        else:
                            l = mid + 1
                    cur = t - (s[l] - s[i_idx + 1])
                    i_idx = l
                    ans[j] = m - i_idx
        return ans
