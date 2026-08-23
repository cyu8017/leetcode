// LeetCode 3733 - Minimum Time to Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

public class Solution {
    public long MinimumTime(int[] d, int[] r) {
        bool Ok(long T) {
            long w0 = T - T / r[0];
            long w1 = T - T / r[1];
            return w0 + w1 >= (long)d[0] + d[1];
        }
        long lo = 1, hi = (long)8e18;
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
