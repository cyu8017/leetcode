# LeetCode 2015 - Average Height of Buildings in Each Segment
# https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

from typing import List


class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, h in buildings:
            events.append((left, 1, h))
            events.append((right, -1, h))
        events.sort(key=lambda e: (e[0], e[1]))
        ans = []
        count = 0
        total = 0
        prev = events[0][0]
        for pos, typ, h in events:
            if pos != prev and count > 0:
                avg = total // count
                if ans and ans[-1][1] == prev and ans[-1][2] == avg:
                    ans[-1][1] = pos
                else:
                    ans.append([prev, pos, avg])
            count += typ
            total += typ * h
            prev = pos
        return ans
