// LeetCode 1482 - Minimum Number Of Days To Make M Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        if ((long) m * k > bloomDay.length) return -1;
        int lo = Integer.MAX_VALUE, hi = Integer.MIN_VALUE;
        for (int x : bloomDay) {
            lo = Math.min(lo, x);
            hi = Math.max(hi, x);
        }
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (possible(bloomDay, m, k, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean possible(int[] bloomDay, int m, int k, int day) {
        int bouquets = 0, run = 0;
        for (int x : bloomDay) {
            run = x <= day ? run + 1 : 0;
            if (run == k) {
                bouquets++;
                run = 0;
            }
        }
        return bouquets >= m;
    }
}
