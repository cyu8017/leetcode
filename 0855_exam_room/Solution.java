// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

import java.util.*;

class ExamRoom {
    private final int n;
    private final TreeSet<Integer> seats = new TreeSet<>();

    public ExamRoom(int n) {
        this.n = n;
    }

    public int seat() {
        if (seats.isEmpty()) {
            seats.add(0);
            return 0;
        }
        int bestSeat = 0;
        int bestDist = seats.first();
        int prev = seats.first();
        for (int cur : seats) {
            if (cur == prev) continue;
            int dist = (cur - prev) / 2;
            if (dist > bestDist) {
                bestDist = dist;
                bestSeat = prev + dist;
            }
            prev = cur;
        }
        if (n - 1 - seats.last() > bestDist) bestSeat = n - 1;
        seats.add(bestSeat);
        return bestSeat;
    }

    public void leave(int p) {
        seats.remove(p);
    }
}
