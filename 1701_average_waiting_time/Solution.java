// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

class Solution {
    public double averageWaitingTime(int[][] customers) {
        long current = 0;
        long total = 0;
        for (int[] customer : customers) {
            current = Math.max(current, customer[0]) + customer[1];
            total += current - customer[0];
        }
        return (double) total / customers.length;
    }
}
