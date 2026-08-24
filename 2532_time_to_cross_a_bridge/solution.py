# LeetCode 2532 - Time to Cross a Bridge
# https://leetcode.com/problems/time-to-cross-a-bridge/

import heapq
from typing import List


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        left = []
        right = []
        ws = []
        for i in range(k):
            t = time[i]
            w = {
                "idx": i,
                "leftToRight": t[0],
                "pickOld": t[1],
                "rightToLeft": t[2],
                "putNew": t[3],
                "efficiency": t[0] + t[2],
            }
            ws.append(w)
            heapq.heappush(left, (-w["efficiency"], -w["idx"], i))
        events = []
        cur = 0
        bridge_free = 0
        remain = n
        done = 0
        while done < n:
            while events and events[0][0] <= cur:
                et, side, idx = heapq.heappop(events)
                w = ws[idx]
                if side == 0:
                    heapq.heappush(left, (-w["efficiency"], -w["idx"], idx))
                else:
                    heapq.heappush(right, (-w["efficiency"], -w["idx"], idx))
            if cur < bridge_free:
                cur = bridge_free
                continue
            if right:
                _, _, idx = heapq.heappop(right)
                w = ws[idx]
                cur += w["rightToLeft"]
                bridge_free = cur
                heapq.heappush(events, (cur + w["putNew"], 0, w["idx"]))
                done += 1
                continue
            if left and remain > 0:
                _, _, idx = heapq.heappop(left)
                w = ws[idx]
                cur += w["leftToRight"]
                bridge_free = cur
                remain -= 1
                heapq.heappush(events, (cur + w["pickOld"], 1, w["idx"]))
                continue
            if not events:
                break
            cur = events[0][0]
        return cur
