// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution {
    public long repairCars(int[] ranks, int cars) {
        int mn = Integer.MAX_VALUE;
        for (int r : ranks) if (r < mn) mn = r;
        long lo = 1, hi = (long) mn * cars * cars;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (ok(ranks, cars, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean ok(int[] ranks, int cars, long t) {
        long done = 0;
        for (int r : ranks) {
            long lo = 0, hi = cars;
            while (lo < hi) {
                long mid = (lo + hi + 1) / 2;
                if ((long) r * mid * mid <= t) lo = mid;
                else hi = mid - 1;
            }
            done += lo;
            if (done >= cars) return true;
        }
        return done >= cars;
    }
}
