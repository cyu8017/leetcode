from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        order = sorted(range(len(times)), key=lambda i: times[i][0])
        free = []  # available chair ids
        next_chair = 0
        leaving = []  # (leave_time, chair)
        for i in order:
            arr, leave = times[i]
            while leaving and leaving[0][0] <= arr:
                heapq.heappush(free, heapq.heappop(leaving)[1])
            if free:
                chair = heapq.heappop(free)
            else:
                chair = next_chair
                next_chair += 1
            if i == targetFriend:
                return chair
            heapq.heappush(leaving, (leave, chair))
        return -1
