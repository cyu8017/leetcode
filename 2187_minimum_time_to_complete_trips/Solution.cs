// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

public class Solution {
    public long MinimumTime(int[] time, int totalTrips) {
        int mn = time.Min();
        long lo = 1, hi = 1L * mn * totalTrips;
        bool Can(long mid) {
            long trips = 0;
            foreach (int t in time) {
                trips += mid / t;
                if (trips >= totalTrips) return true;
            }
            return false;
        }
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (Can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
