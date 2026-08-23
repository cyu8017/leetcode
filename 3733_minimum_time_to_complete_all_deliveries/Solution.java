// LeetCode 3733 - Minimum Time To Complete All Deliveries
// https://leetcode.com/problems/minimum_time_to_complete_all_deliveries/

class Solution {
    public long minimumTime(int[] d, int[] r) {
        long lo = 1, hi = (long) 8e18;
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (ok(mid, d, r)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean ok(long T, int[] d, int[] r) {
        long w0 = T - T / r[0];
        long w1 = T - T / r[1];
        return w0 + w1 >= (long) d[0] + d[1];
    }
}
