# LeetCode 1109 - Corporate Flight Bookings
# https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats
        ans = []
        cur = 0
        for i in range(n):
            cur += diff[i]
            ans.append(cur)
        return ans
