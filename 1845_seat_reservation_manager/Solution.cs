// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

using System.Collections.Generic;

public class SeatManager {
    private readonly PriorityQueue<int, int> available = new();

    public SeatManager(int n) {
        for (int i = 1; i <= n; i++) available.Enqueue(i, i);
    }

    public int Reserve() {
        return available.Dequeue();
    }

    public void Unreserve(int seatNumber) {
        available.Enqueue(seatNumber, seatNumber);
    }
}
