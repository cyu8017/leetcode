// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

public class Solution {
    public double AverageWaitingTime(int[][] customers) {
        long current = 0;
        long total = 0;
        foreach (var customer in customers) {
            current = System.Math.Max(current, customer[0]) + customer[1];
            total += current - customer[0];
        }
        return (double)total / customers.Length;
    }
}
