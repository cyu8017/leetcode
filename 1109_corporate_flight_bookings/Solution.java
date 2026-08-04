// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] diff = new int[n + 1];
        for (int[] b : bookings) {
            diff[b[0] - 1] += b[2];
            diff[b[1]] -= b[2];
        }
        int[] ans = new int[n];
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            ans[i] = cur;
        }
        return ans;
    }
}
