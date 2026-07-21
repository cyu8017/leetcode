// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

import java.util.PriorityQueue

class SeatManager(n: Int) {
    private val available = PriorityQueue<Int>()

    init {
        for (i in 1..n) available.offer(i)
    }

    fun reserve(): Int {
        return available.poll()
    }

    fun unreserve(seatNumber: Int) {
        available.offer(seatNumber)
    }
}
