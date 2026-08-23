// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

using System.Collections.Generic;

public class ExamRoom {
    private readonly int n;
    private readonly SortedSet<int> seats = new SortedSet<int>();

    public ExamRoom(int n) {
        this.n = n;
    }

    public int Seat() {
        if (seats.Count == 0) {
            seats.Add(0);
            return 0;
        }
        int bestSeat = 0;
        int bestDist = seats.Min;
        int prev = seats.Min;
        foreach (int cur in seats) {
            if (cur == prev) continue;
            int dist = (cur - prev) / 2;
            if (dist > bestDist) {
                bestDist = dist;
                bestSeat = prev + dist;
            }
            prev = cur;
        }
        if (n - 1 - seats.Max > bestDist) bestSeat = n - 1;
        seats.Add(bestSeat);
        return bestSeat;
    }

    public void Leave(int p) {
        seats.Remove(p);
    }
}
