// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

using System;

public class Solution {
    public int MinMovesToSeat(int[] seats, int[] students) {
        Array.Sort(seats);
        Array.Sort(students);
        int ans = 0;
        for (int i = 0; i < seats.Length; i++) ans += Math.Abs(seats[i] - students[i]);
        return ans;
    }
}
