// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

import java.util.PriorityQueue;

class SeatManager {
    private final PriorityQueue<Integer> available;

    public SeatManager(int n) {
        available = new PriorityQueue<>();
        for (int i = 1; i <= n; i++) {
            available.offer(i);
        }
    }

    public int reserve() {
        return available.poll();
    }

    public void unreserve(int seatNumber) {
        available.offer(seatNumber);
    }
}
