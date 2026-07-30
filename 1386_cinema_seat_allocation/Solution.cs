// LeetCode 1386 - Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/

using System.Collections.Generic;
public class Solution {
    public int MaxNumberOfFamilies(int n, int[][] reservedSeats) {
        var rows = new Dictionary<int, int>();
        foreach (var seat in reservedSeats) {
            int r = seat[0], c = seat[1];
            if (c >= 2 && c <= 9) {
                if (!rows.ContainsKey(r)) rows[r] = 0;
                rows[r] |= 1 << (c - 2);
            }
        }
        int ans = 2 * (n - rows.Count);
        foreach (int m in rows.Values) {
            bool left = (m & 0b00001111) == 0, right = (m & 0b11110000) == 0, middle = (m & 0b00111100) == 0;
            ans += left && right ? 2 : (left || right || middle ? 1 : 0);
        }
        return ans;
    }
}
