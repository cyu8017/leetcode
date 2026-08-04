// LeetCode 1386 - Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/

import java.util.*;

class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        Map<Integer, Integer> rows = new HashMap<>();
        for (int[] seat : reservedSeats) {
            int r = seat[0], c = seat[1];
            if (c >= 2 && c <= 9) rows.merge(r, 1 << (c - 2), (a, b) -> a | b);
        }
        int ans = 2 * (n - rows.size());
        for (int m : rows.values()) {
            boolean left = (m & 0b00001111) == 0;
            boolean right = (m & 0b11110000) == 0;
            boolean middle = (m & 0b00111100) == 0;
            if (left && right) ans += 2;
            else if (left || right || middle) ans += 1;
        }
        return ans;
    }
}
