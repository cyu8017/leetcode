# LeetCode 3169 - Count Days Without Meetings
# https://leetcode.com/problems/count-days-without-meetings/

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda e: e[0])
        last = 0
        ans = 0
        for st, ed in meetings:
            if last < st:
                ans += st - last - 1
            last = max(last, ed)
        ans += days - last
        return ans
