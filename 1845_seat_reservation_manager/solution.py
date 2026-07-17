# LeetCode 1845 - Seat Reservation Manager
# https://leetcode.com/problems/seat-reservation-manager/

import heapq


class SeatManager:
    def __init__(self, n: int):
        self.available = list(range(1, n + 1))
        heapq.heapify(self.available)

    def reserve(self) -> int:
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)
