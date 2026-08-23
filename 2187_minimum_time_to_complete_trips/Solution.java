// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution {
    public long minimumTime(int[] time, int totalTrips) {
        int mn = time[0];
        for (int t : time) mn = Math.min(mn, t);
        long lo = 1, hi = 1L * mn * totalTrips;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            long trips = 0;
            boolean ok = false;
            for (int t : time) {
                trips += mid / t;
                if (trips >= totalTrips) { ok = true; break; }
            }
            if (ok) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
