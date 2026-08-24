# LeetCode 2933 - High-Access Employees
# https://leetcode.com/problems/high-access-employees/

from typing import List


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        m = {}
        for name, t in access_times:
            hh = (ord(t[0]) - 48) * 10 + (ord(t[1]) - 48)
            mm = (ord(t[2]) - 48) * 10 + (ord(t[3]) - 48)
            if name not in m:
                m[name] = []
            m[name].append(hh * 60 + mm)
        ans = []
        for name, times in m.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] < 60:
                    ans.append(name)
                    break
        ans.sort()
        return ans
