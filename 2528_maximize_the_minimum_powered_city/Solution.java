// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

class Solution {
    public long maxPower(int[] stations, int r, int k) {
        int n = stations.length;
        long[] diff = new long[n + 1];
        for (int i = 0; i < n; i++) {
            int L = Math.max(0, i - r);
            int R = Math.min(n - 1, i + r);
            diff[L] += stations[i];
            diff[R + 1] -= stations[i];
        }
        long[] power = new long[n];
        long cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            power[i] = cur;
        }
        long lo = 0, hi = k;
        for (long p : power) if (p > hi) hi = p;
        hi += k;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (ok(power, r, k, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    private boolean ok(long[] power, int r, long k, long x) {
        int n = power.length;
        long[] extra = new long[n + 1];
        long have = 0, used = 0;
        for (int i = 0; i < n; i++) {
            have += extra[i];
            long need = x - (power[i] + have);
            if (need > 0) {
                used += need;
                if (used > k) return false;
                have += need;
                int end = i + 2 * r;
                if (end + 1 <= n) extra[end + 1] -= need;
            }
        }
        return true;
    }
}
