// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

using System.Linq;

public class Solution {
    public long RepairCars(int[] ranks, int cars) {
        bool Ok(long t) {
            long done = 0;
            foreach (int r in ranks) {
                long lo = 0, hi = cars;
                while (lo < hi) {
                    long mid = (lo + hi + 1) / 2;
                    if ((long)r * mid * mid <= t) lo = mid;
                    else hi = mid - 1;
                }
                done += lo;
                if (done >= cars) return true;
            }
            return done >= cars;
        }
        int mn = ranks.Min();
        long lo2 = 1, hi2 = (long)mn * cars * cars;
        while (lo2 < hi2) {
            long mid = (lo2 + hi2) / 2;
            if (Ok(mid)) hi2 = mid;
            else lo2 = mid + 1;
        }
        return lo2;
    }
}
